##########################################################################################################
#                                                                                                        #
#  $$$$$$$\  $$\                            $$\                                    $$$$$$\  $$\    $$\   #
#  $$  __$$\ $$ |                           $$ |                                  $$  __$$\ $$ |   $$ |  #
#  $$ |  $$ |$$$$$$$\   $$$$$$\  $$$$$$$\ $$$$$$\    $$$$$$\  $$$$$$\$$$$\        $$ /  \__|$$ |   $$ |  #
#  $$$$$$$  |$$  __$$\  \____$$\ $$  __$$\\_$$  _|  $$  __$$\ $$  _$$  _$$\       $$ |      \$$\  $$  |  #
#  $$  ____/ $$ |  $$ | $$$$$$$ |$$ |  $$ | $$ |    $$ /  $$ |$$ / $$ / $$ |      $$ |       \$$\$$  /   #
#  $$ |      $$ |  $$ |$$  __$$ |$$ |  $$ | $$ |$$\ $$ |  $$ |$$ | $$ | $$ |      $$ |  $$\   \$$$  /    #
#  $$ |      $$ |  $$ |\$$$$$$$ |$$ |  $$ | \$$$$  |\$$$$$$  |$$ | $$ | $$ |      \$$$$$$  |   \$  /     #
#  \__|      \__|  \__| \_______|\__|  \__|  \____/  \______/ \__| \__| \__|       \______/     \_/      #
#                                                                                                        #
##########################################################################################################
#                                                                                                        #
#                                  Hello, Welcome to Phantom CV!                                         #
#                                                                                                        #
#                Please consider donating, this took a lot of research and development                   #
#                                                                                                        #
#                      BIG thanks to YOLOv5 🚀 by Ultralytics and Chaotic                                #
#                                                                                                        #
##########################################################################################################
#                                                                                                        #
# Bitcoin - 1Fwdk5fkhZ1Y3uyb2HKywHyHQuddiik6Xu     Ethereum - 0x794067Aa418A6bBe774eE313140cCDFd35C2a148 #
#                                                                                                        #
# Dogecoin - DS8q14xNtRD3FZAzpmTrGfJ88Ain61wXor    Ripple - rMVLwS4A5onNvcCPYAeqS2fq3DQg6DRr7L           #
#                                                                                                        #
##########################################################################################################
###     GENERAL SETTINGS    ###
dataCollectionMode = False # Captures training data as you play. 
showBoundingBox = True # Enable / Disable the drawing of bounding boxes on the screen

###     AIM ASSIST SETTINGS    ###
aimAssist = True # Enable / Disable Advanced Aim Assist
autoFireDistance = 0 # How close you want the target to be (in pixels) before the script will automatically fire. Set to 0 to disable.
confidence = 0.6 # How confident you want the AI to be in its prediction before taking over. Values range from 0-1.
IoUThreshold = 0.45 #Intersection over Union. Anything over 0.5 is generaally considered a good prediction. Values range from 0-1.
speedX, speedY = 9, 9 # Speed modifier that affects how fast your aim will be on the X and Y axis.
aimSmoothing = False # Will pull harder towards targets closer to the center
boundingBoxX1, boundingBoxY1, boundingBoxX2, boundingBoxY2 = 0, 0, 1920, 1080#400, 180, 1500, 900 # [] 0, 0, 1920, 1080 #Dimensions of the screen that you want the AI to scan. The model was trained on 1920x1080 images but if you are experiencing range drop off you may want to find a bounding box that works for you. A smaller bounding box may also result in higher accuracy.
boundingBoxColor = [102,51,153] # RGB Setting for Bounding Boxes
adaptiveBoundingBox = False # Will automatically resize bounding box when aiming in
manualOveride = True # Manually overides any inputs from the model while clicking down on the left stick.
modelName = 'warzone' # Name of model you would like to use. More to come soon... Will only work with files from our Telegram. Everything is Encrypted.
