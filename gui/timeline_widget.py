from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem, QApplication
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

print("Timeline widget başlatılıyor...")  # Bu satırı ekle

class TimelineView(QGraphicsView):
    def __init__(self):
        super().__init__()
        print("TimelineView başlatılıyor...")  # Bu satırı ekle
        self.setScene(TimelineScene())

        self.setRenderHint(QPainter.Antialiasing)
        
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.setBackgroundBrush(QBrush(QColor(30, 30, 30)))
        self.setWindowTitle("Timeline Editor")
        self.resize(800, 200)


class TimelineScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.setSceneRect(0, 0, 2000, 150)
        self.init_grid()

    def init_grid(self):
        """Zaman çizelgesi arka plan ızgarası oluşturulur."""
        pen = QPen(QColor(50, 50, 50), 0.5)
        for x in range(0, 2000, 10):
            self.addLine(x, 0, x, 150, pen)
        for y in range(0, 150, 10):
            self.addLine(0, y, 2000, y, pen)


class TrackItem(QGraphicsItem):
    def __init__(self, x, y, width, height, color=QColor(70, 130, 180)):
        super().__init__()
        self.rect = QRectF(x, y, width, height)
        self.color = color
        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

    def boundingRect(self) -> QRectF:
        return self.rect

    def paint(self, painter, option, widget=None):
        painter.setBrush(QBrush(self.color))
        painter.setPen(QPen(Qt.NoPen))
        painter.drawRect(self.rect)


if __name__ == "__main__":
    print("Uygulama başlatılıyor...")
    app = QApplication(sys.argv)
    view = TimelineView()

    # Örnek Track ekleyelim
    scene = view.scene()
    scene.addItem(TrackItem(50, 20, 150, 40))
    scene.addItem(TrackItem(250, 20, 150, 40))
    scene.addItem(TrackItem(450, 20, 150, 40))

    view.show()
    sys.exit(app.exec_())
