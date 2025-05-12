import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

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
        # Kullanıcıdan proje adı ve kaydetme dizini al
        project_name, ok = QFileDialog.getSaveFileName(
            self,
            "Yeni Proje Oluştur",
            os.path.expanduser('~') + '/Documents/VideoEditorApp/Projects/',
            "Video Project Files (*.aydiv)"
        )
        if ok and project_name:
            try:
                project_dir = os.path.dirname(project_name)
                os.makedirs(project_dir, exist_ok=True)
                # Boş proje dosyası oluştur
                with open(project_name, 'w', encoding='utf-8') as f:
                    f.write('')
                QMessageBox.information(self, 'Başarılı', f'Yeni proje oluşturuldu:\n{project_name}')
            except Exception as e:
                QMessageBox.critical(self, 'Hata', f'Proje oluşturulurken hata:\n{e}')

    def open_existing_project(self):
        # Mevcut proje dosyasını aç
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
            QMessageBox.information(self, 'Proje Açıldı', f'Proje açıldı:\n{project_path}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WelcomeScreen()
    window.show()
    sys.exit(app.exec_())
