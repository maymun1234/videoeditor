import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qt_material import apply_stylesheet
from moviepy.editor import VideoFileClip
import cv2
import numpy as np
from videoeditor2_2 import videoeditor2

class TimelineView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setScene(QGraphicsScene(self))
        self.setRenderHint(QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.init_timeline()

    def init_timeline(self):
        self.scene().setBackgroundBrush(QBrush(QColor(30, 30, 30)))
        for i in range(0, 1000, 100):
            self.scene().addLine(i, 0, i, 50, QPen(Qt.white))
        self.playhead = self.scene().addLine(0, 0, 0, 50, QPen(QColor(255, 0, 0), 2))

    def update_playhead(self, pos):
        if self.playhead:
            self.playhead.setLine(pos, 0, pos, 50)

class VideoEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Video Editor")
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.open_button = QPushButton(QIcon("open.png"), "", self)
        self.open_button.setToolTip("Open Video")
        self.open_button.clicked.connect(self.open_video)
        self.layout.addWidget(self.open_button)

        self.play_button = QPushButton(QIcon("play.png"), "", self)
        self.play_button.setEnabled(False)
        self.play_button.setToolTip("Play")
        self.play_button.clicked.connect(self.play_video)
        self.layout.addWidget(self.play_button)

        self.stop_button = QPushButton(QIcon("stop.png"), "", self)
        self.stop_button.setEnabled(False)
        self.stop_button.setToolTip("Stop")
        self.stop_button.clicked.connect(self.stop_video)
        self.layout.addWidget(self.stop_button)


        self.effect_button = QPushButton("Apply Effect", self)
        self.effect_button.setEnabled(False)
        self.effect_button.clicked.connect(self.apply_effect)
        self.layout.addWidget(self.effect_button)

        self.label = QLabel("Video will be displayed here", self)
        self.layout.addWidget(self.label)

        self.timeline_view = TimelineView(self)
        self.layout.addWidget(self.timeline_view)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        self.video_clip = None
        self.video_capture = None
        self.frame_pos = 0

    def open_video(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Video File", "", "Video Files (*.mp4 *.avi *.mov);;All Files (*)", options=options)
        if file_name:
            self.video_clip = VideoFileClip(file_name)
            self.video_capture = cv2.VideoCapture(file_name)
            self.play_button.setEnabled(True)
            self.stop_button.setEnabled(True)
            self.effect_button.setEnabled(True)

    def play_video(self):
        self.timer.start(30)  # roughly 30 frames per second

    def stop_video(self):
        self.timer.stop()


    

    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            self.label.setPixmap(pixmap)
            self.frame_pos += 1
            self.timeline_view.update_playhead(self.frame_pos * 2)
        else:
            self.stop_video()

            
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Tema dosyalarını yükle
    apply_stylesheet(app, theme='dark_pink.xml')

    window = VideoEditor()
    window.show()
    sys.exit(app.exec_())
