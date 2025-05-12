import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qt_material import apply_stylesheet
from moviepy.editor import VideoFileClip
import cv2
import numpy as np

class videoeditor2(QMainWindow):
    def __init__(self):
        super().__init__()
        # Diğer metodlarınız burada

    # Yeni bir metod ekleyin
    def apply_effect(self, effect):
        if self.video_clip:
            self.video_clip = effect(self.video_clip)


    