from module.detection import Classifier as classif
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
import cv2
class image_man:

    def __init__(self):
        Clock.schedule_interval(self.update, 1.0/33.0)
        self.classif = classif()
        self.web_cam = Image(size_hint=(1,.8))
    def update(self, *args):
        """read frame from opencv"""
        rect, frame = self.classif.capture.read()
        frame = frame[:, :, :]
        
        #change color to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()
        faces = self.classif.FaceClassif.detectMultiScale(gray,1.3,5)

        
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h), (0,255,0),2)
            
        
        # Flip horizontall and convert image to texture
        buf = cv2.flip(frame, -1).tobytes()
        img_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        img_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        #print(dir(img_texture))
        self.web_cam.texture = img_texture
        
    

