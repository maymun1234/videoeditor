import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from ui_main import Ui_MainWindow  # Oluşturulan UI sınıfını içeri aktarıyoruz
from timeline_widget import TimelineView  # TimelineView'i içeri aktarıyoruz


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Timeline'ı oluştur ve arayüze ekle
        self.timeline_view = TimelineView()
        
        # QGraphicsView olan timeline widget'inin yerine yerleştir
        layout = QVBoxLayout(self.timeline)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.timeline_view)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
