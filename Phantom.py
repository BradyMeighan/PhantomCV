import os
import platform
import settings

hp = "phantomcv_helper"

def getFile():
    if platform.system() == "Windows": return "phantomcv_helper.cp38-win_amd64.pyd"
    else: return "phantomcv_helper.cp38-win_amd64.pyd"
    
file = getFile()

class GCVWorker:
    def __init__(self, width, height):
        global hp
        os.chdir(os.path.dirname(__file__))
        
        hp = __import__(hp)
        
        # Create an instance of the Phantom class
        self.phantom_instance = hp.Phantom()
        if settings.aimAssist: self.phantom_instance.load_model(settings.modelName)
    def __del__(self):
        del self

    def process(self, frame):
        global hp
        gcvdata = bytearray()
        if settings.aimAssist:
            # Call the process method using the phantom_instance
            frame, gcvdata = self.phantom_instance.process(frame, gcvdata)
        return (frame, gcvdata)
