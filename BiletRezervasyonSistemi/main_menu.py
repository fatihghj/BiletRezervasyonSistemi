from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
from sefer_listesi import SeferListesi
from rezervasyonlar import Rezervasyonlar  

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ana Menü")
        self.setGeometry(100, 100, 500, 350)
        self.setStyleSheet("background-color: IndianRed;")

        self.card = QWidget()
        self.card.setFixedSize(350, 250)
        self.card.setStyleSheet("""
            background-color: #ffffff;
            border-radius: 15px;
            padding: 30px;
            border: 1px solid #ddd;
        """)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        self.label = QLabel("Ana Menüye Hoş Geldiniz!")
        self.label.setFont(QFont("Arial", 16, QFont.Bold))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: #333; margin-bottom: 20px;")

        self.button_sefer = QPushButton("Sefer Ara")
        self.button_rezervasyon = QPushButton("Rezervasyonlarım")
        self.button_exit = QPushButton("Çıkış")

        for btn in [self.button_sefer, self.button_rezervasyon, self.button_exit]:
            btn.setFont(QFont("Arial", 11))
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #e74c3c;
                    color: white;
                    border-radius: 20px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #c0392b;
                }
            """)
            layout.addWidget(btn)

        self.button_exit.clicked.connect(self.close)  
        self.button_sefer.clicked.connect(self.open_sefer_listesi)  
        self.button_rezervasyon.clicked.connect(self.open_rezervasyonlar)  

        self.card.setLayout(layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.card, alignment=Qt.AlignCenter)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def open_sefer_listesi(self):
        self.sefer_listesi = SeferListesi()
        self.sefer_listesi.show()

    def open_rezervasyonlar(self):
        self.rezervasyonlar = Rezervasyonlar()
        self.rezervasyonlar.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec_())
