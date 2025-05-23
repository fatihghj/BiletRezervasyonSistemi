from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
from database import rezervasyonlari_getir, rezervasyon_sil  

class Rezervasyonlar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rezervasyonlarım")
        self.setGeometry(100, 100, 500, 400)
        self.setStyleSheet("background-color: IndianRed;")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        self.label = QLabel("Kayıtlı Rezervasyonlar")
        self.label.setFont(QFont("Arial", 16, QFont.Bold))
        self.label.setStyleSheet("color: white; margin-bottom: 10px;")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.listWidget = QListWidget()
        self.listWidget.setStyleSheet("""
            QListWidget {
                background-color: white;
                border-radius: 12px;
                padding: 10px;
                font-size: 14px;
            }
        """)
        self.yukle_rezervasyonlar()
        layout.addWidget(self.listWidget)

        self.button_sil = QPushButton("Seçili Rezervasyonu Sil")
        self.button_sil.setFont(QFont("Arial", 11, QFont.Bold))
        self.button_sil.setStyleSheet("""
            QPushButton {
                background-color: #E74C3C;
                color: white;
                border: none;
                border-radius: 20px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #C0392B;
            }
        """)
        self.button_sil.clicked.connect(self.sil_rezervasyon)
        layout.addWidget(self.button_sil)

        central_widget.setLayout(layout)

    def yukle_rezervasyonlar(self):
        rezervasyonlar = rezervasyonlari_getir()
        for rezervasyon in rezervasyonlar:
            self.listWidget.addItem(f"{rezervasyon[1]} - Koltuk: {rezervasyon[2]}")

    def sil_rezervasyon(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            reply = QMessageBox.question(self, "Sil", "Seçili rezervasyonu silmek istiyor musunuz?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                rezervasyon_text = selected_item.text().split(" - Koltuk: ")
                rezervasyon_sil(rezervasyon_text[0], rezervasyon_text[1])
                self.listWidget.takeItem(self.listWidget.row(selected_item))
        else:
            QMessageBox.warning(self, "Hata", "Lütfen bir rezervasyon seçin!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Rezervasyonlar()
    window.show()
    sys.exit(app.exec_())
