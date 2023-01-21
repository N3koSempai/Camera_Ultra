from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from module.image import image_man as imn
# Import kivy UX components
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.logger import Logger

# Import other dependencies
import cv2
#import tensorflow as tf
#from layers import L1Dist
import os
import numpy as np

class CameraUltra(App):


    def build(self):
        # Main layout components 
        self.im = imn()
        self.button = Button(text="capture", size_hint=(1,.1))


        # Add items to layout
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.im.web_cam)
        layout.add_widget(self.button)

        
        
        return layout
        
if __name__ == "__main__":
    CameraUltra().run()
