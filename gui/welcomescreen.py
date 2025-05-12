import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt

# MainWindow import
from main_window import MainWindow  # MainWindow arayüzü buraya import ediliyor.

class WelcomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # .ui dosyasını yükle
        ui_path = os.path.join(os.path.dirname(__file__), 'ui', 'welcomeui.ui')
        uic.loadUi(ui_path, self)

        # Buton referansları
        self.new_button = self.findChild(type(self.pushButton_3), 'pushButton_3')
        self.open_button = self.findChild(type(self.pushButton_2), 'pushButton_2')

        # Buton bağlantıları
        self.new_button.clicked.connect(self.create_new_project)
        self.open_button.clicked.connect(self.open_existing_project)

    def create_new_project(self):
        """Yeni proje oluştur ve MainWindow'u başlat."""        
        try:
            # Direkt yeni bir proje başlat, kullanıcıdan proje adı isteme
            self.main_window = MainWindow()
            self.main_window.showMaximized()  # Tam ekran aç
            self.close()  # WelcomeScreen'i kapat

        except Exception as e:
            QMessageBox.critical(self, 'Hata', f'Yeni proje başlatılırken hata:\n{e}')

    def open_existing_project(self):
        """Mevcut proje dosyasını aç ve MainWindow'u başlat."""        
        project_path, _ = QFileDialog.getOpenFileName(
            self,
            "Proje Aç",
            os.path.expanduser('~') + '/Documents/VideoEditorApp/Projects/',
            "Video Project Files (*.aydiv)"
        )
        if project_path:
            # Burada Project yükleme mantığını çağırabilirsin
            # from core.models.project import Project
            # project = Project.load(project_path)

            try:
                # Mevcut projeyi aç ve editörü başlat
                self.main_window = MainWindow()
                self.main_window.showMaximized()  # Tam ekran aç
                self.close()  # WelcomeScreen'i kapat

            except Exception as e:
                QMessageBox.critical(self, 'Hata', f'Proje açılırken hata:\n{e}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WelcomeScreen()
    window.show()
    sys.exit(app.exec_())
