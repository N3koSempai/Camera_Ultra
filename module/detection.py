import cv2

class Classifier:
    """class for manage al IA things like capture, detection, recognition"""
    
    def __init__(self):
        # start capture image with camera 1. number 0.1..2.3.. are index for diferent camera device in your enviroment
        self.capture = cv2.VideoCapture(0)
        # set detection model
        self.FaceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
        
