import cv2
import gtuner
import torch
import torch.backends.cudnn as cudnn
import numpy as np
import os
import random
import settings

class Phantom:
    def __init__(self):
        # Initialize the Phantom object with settings from the settings module.
        self.confidence = settings.confidence
        self.IoUThreshold = settings.IoUThreshold
        self.speedX = settings.speedX
        self.speedY = settings.speedY
        self.aimSmoothing = settings.aimSmoothing
        self.manualOveride = settings.manualOveride
        self.dataCollectionMode = settings.dataCollectionMode
        self.boundingBoxX1 = settings.boundingBoxX1
        self.boundingBoxX2 = settings.boundingBoxX2
        self.boundingBoxY1 = settings.boundingBoxY1
        self.boundingBoxY2 = settings.boundingBoxY2
        self.showBoundingBox = settings.showBoundingBox
        self.color = [settings.boundingBoxColor[0], settings.boundingBoxColor[1],settings.boundingBoxColor[2]]
        self.adaptiveBoundingBox = settings.adaptiveBoundingBox
        self.currentFrame = 0

    @staticmethod
    def seed_everything(seed):
        # Set the seeds for all relevant libraries for reproducible results.
        random.seed(seed)
        os.environ["PYTHONHASHSEED"] = str(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = True
        torch.backends.cudnn.enabled = False

    def load_model(self, modelName):
        # Load a YOLOv5 model with the specified model name, set up the model configuration, and return the model.
        global model
        SEED = 42
        Phantom.seed_everything(SEED)
        cudnn.benchmark = True
        model = torch.hub.load('ultralytics/yolov5', 'custom', _verbose=False, path=os.path.dirname(__file__) + '\\' + modelName + '.pt')
        img_size = 416
        model.conf = self.confidence
        model.iou = self.IoUThreshold
        model.agnostic = True
        model.multi_label = False
        model.classes = None
        model.max_det = 10
        model.amp = False
        model.cuda()

        return model

    def rectangleScaling(x1, y1, x2, y2):
        # Calculate the center point of a rectangle for targeting based on the provided coordinates.
        distanceX = abs((x1 - x2)) / 2
        distanceY = abs((y1 - y2)) / 3
        centerX = int(distanceX) + x1
        headshotY = int(distanceY) + y1
        return (centerX, headshotY)

    def draw_border(self, img, pt1, pt2, thickness, r, d):
        # Draw a border around a rectangular region in an image.
        x1,y1 = pt1
        x2,y2 = pt2

        # Top left
        cv2.line(img, (x1 + r, y1), (x1 + r + d, y1), self.color, thickness)
        cv2.line(img, (x1, y1 + r), (x1, y1 + r + d), self.color, thickness)
        cv2.ellipse(img, (x1 + r, y1 + r), (r, r), 180, 0, 90, self.color, thickness)

        # Top right
        cv2.line(img, (x2 - r, y1), (x2 - r - d, y1), self.color, thickness)
        cv2.line(img, (x2, y1 + r), (x2, y1 + r + d), self.color, thickness)
        cv2.ellipse(img, (x2 - r, y1 + r), (r, r), 270, 0, 90, self.color, thickness)

        # Bottom left
        cv2.line(img, (x1 + r, y2), (x1 + r + d, y2), self.color, thickness)
        cv2.line(img, (x1, y2 - r), (x1, y2 - r - d), self.color, thickness)
        cv2.ellipse(img, (x1 + r, y2 - r), (r, r), 90, 0, 90, self.color, thickness)

        # Bottom right
        cv2.line(img, (x2 - r, y2), (x2 - r - d, y2), self.color, thickness)
        cv2.line(img, (x2, y2 - r), (x2, y2 - r - d), self.color, thickness)
        cv2.ellipse(img, (x2 - r, y2 - r), (r, r), 0, 0, 90, self.color, thickness)
        return img
        

    def predict(self, frame, button_5, button_8, button_9):
        global model
        # Process an input frame, run the model for object detection, and return the processed frame and right stick coordinates for aiming.
        rx, ry = 0, 0
        final = frame
        x1, y1, x2, y2 = 960, 540, 960, 540
        X1, Y1, X2, Y2 = self.boundingBoxX1, self.boundingBoxY1, self.boundingBoxX2, self.boundingBoxY2

        if self.adaptiveBoundingBox and button_8 > 0:
            X1, Y1, X2, Y2 = 400, 180, 1500, 900

        ROI = {"X1":X1, "Y1":Y1, "X2":X2, "Y2":Y2}
        img0 = frame[ROI["Y1"]:ROI["Y2"], ROI["X1"]:ROI["X2"], :]
        
        

        if self.showBoundingBox:
            img_bounding = Phantom.draw_border(self, frame, (x1, y1), (x2,y2), 8, 15, 30)
            img_bounding = Phantom.draw_border(self, img_bounding, (0, 0), (1920,1080), 8, 15, 30)

        results = model(img0, size=416)
        
        for box in results.xyxy[0]:
            x1, y1, x2, y2, conf = int(box[0]), int(box[1]), int(box[2]), int(box[3]), int(box[4])
            label = f"Player {conf:.2f}"
            if box[5]==0: #If Player Detected
                x1, y1, x2, y2 = (x1 + X1), (y1 + Y1), (x2 + X1), (y2 + Y1)
                
                rx, ry = Phantom.trajectory(self, x1, y1, x2, y2)
                if self.manualOveride and button_9 > 0:
                    rx, ry = 0, 0
                print(str(rx) + ' ' + str(ry))
                if button_5 > 0:
                    if self.dataCollectMode: print('Player Detected on Screen! Skipping Frame')
                if(self.showBoundingBox):
                    draw1 = Phantom.draw_border(self, img_bounding, (x1, y1), (x2,y2), 4, 15, 30)
                    draw2 = cv2.putText(draw1,label,(x1, y1 - 20),cv2.FONT_HERSHEY_PLAIN,2,((self.color)),2,)
                    draw3 = cv2.putText(draw2,str(Phantom.rectangleScaling(x1,y1,x2,y2)),(x1, y1 - 50),cv2.FONT_HERSHEY_PLAIN,2,((self.color)),2,)
                    draw4 = cv2.circle(draw3,Phantom.rectangleScaling(x1,y1,x2,y2), 15, (0,0,255), -1)
                    final = cv2.line(draw4,(960, 540),(Phantom.rectangleScaling(x1, y1, x2, y2)),(0, 0, 255),3,)
            elif self.dataCollectionMode:
                    if button_5 > 0: save_data()

        return (final, rx, ry)

    def save_data(self):
        # Save the current frame as an image file for data collection.
        print('Player Not Detected!')
        name = './data/frame' + str(self.currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, img_path)
        currentFrame += 1

    def trajectory(self, x1, y1, x2, y2):
        # Calculate the trajectory required to move the aim from the current position to the target position.
        global distance
        rx, ry = 0, 0
        crosshairPositionX, crosshairPositionY = 960, 540
        playerCoordX, playerCoordY = Phantom.rectangleScaling(x1, y1, x2, y2)
        distance = (((playerCoordX - crosshairPositionX) ** 2) + ((playerCoordY - crosshairPositionY) ** 2)) ** 0.5

        deltaX = playerCoordX - crosshairPositionX
        deltaY = playerCoordY - crosshairPositionY

        pForceX = deltaX / 1920
        pForceY = deltaY / 1080

        dX, dY = (pForceX * self.speedX) * 100, (pForceY * self.speedY) * 100
        
        if (self.aimSmoothing):
            dX, dY = apply_aim_smoothing(distance, dX, dY)
        rx, ry = dX, dY
        return (rx, ry)
        
    def apply_aim_smoothing(distance, rx, ry):
        # Apply smoothing to the calculated trajectory based on the distance between the current position and target position.
        speed = 1.171429 + (5.851389000000001e-20) * distance + 0.000002380952*x^2
        return (rx*speed), (ry*speed)
        
    def process(self, frame, gcvdata):
        ### Main processing function: get controller button states, process the frame using the predict function, and update gcvdata with new right stick coordinates. ###
        ### INITIALIZE TITAN TWO BYTE ARRAY AND UPDATE CONTROLLER VALUES ###        
        button_5 = gtuner.get_actual(gtuner.BUTTON_5) #RT
        button_8 = gtuner.get_actual(gtuner.BUTTON_8) #LT
        button_9 = gtuner.get_actual(gtuner.BUTTON_9) #LS           
        
        ### PREDICT AND MODIFY FRAMES ###
        frame_text = cv2.putText(frame,"Phantom CV v0.7",(30, 30),cv2.FONT_HERSHEY_PLAIN,2,(102,51,153),2,)
        frame_process, rightStickX, rightStickY = Phantom.predict(self, frame, button_5, button_8, button_9)
        frame_process = cv2.circle(frame_process,(960,540), 70, (self.color), 2)
        #print('calculating trajectory ')
        
        #print('calculating autofire')
        #autoFire = Phantom.AutoFire(x1, y1, x2, y2)
        #print('auto fire done')
        #print(gcvdata)
        ### SEND DATA TO GPC SCRIPT FOR INTERPRETATION ###
        #print('sending gcv data rx = ' +str(rightStickX)+ ' + ' +str(rightStickY))
        gcvdata.extend(int(float(rightStickX) * 0x10000).to_bytes(4, byteorder="big", signed=True))
        gcvdata.extend(int(float(rightStickY) * 0x10000).to_bytes(4, byteorder="big", signed=True))
        # gcvdata.extend(int(float(autoFire)*0x10000).to_bytes(4, byteorder='big', signed=True))
        #gcvdata.extend(int(autoFire).to_bytes(2, byteorder="big", signed=True))
        #print('gcvdata sent')
        return frame_process, gcvdata
        
        
def PyInit_phantomcv_helper():
    # Initialize the helper function for the PhantomCV module.
    return None

