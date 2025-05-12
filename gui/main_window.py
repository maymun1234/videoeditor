import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from ui_main import Ui_MainWindow  # UI sınıfını import ediyoruz
from timeline_widget import TimelineView  # Timeline widget'ini import ediyoruz


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # UI dosyasını yükle
        ui_path = os.path.join(os.path.dirname(__file__), 'ui', 'main.ui')
        uic.loadUi(ui_path, self)  # UI dosyasını yükle

        # Timeline widget'ını oluştur ve layout'a ekle
        self.timeline_view = TimelineView()

        # QGraphicsView widget'inin yerine TimelineView yerleştir
        timeline_widget = self.findChild(QWidget, 'timeline')  # timeline widget'ini bul
        layout = QVBoxLayout(timeline_widget)  # timeline widget'ine yeni layout ekle
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.timeline_view)  # TimelineView'i ekle


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
