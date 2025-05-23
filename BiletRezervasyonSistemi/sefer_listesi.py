from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
from rezervasyon import Rezervasyon  

class SeferListesi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sefer Listesi")
        self.setGeometry(100, 100, 500, 400)
        self.setStyleSheet("background-color: IndianRed;")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        self.label = QLabel("Mevcut Seferler")
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
        self.listWidget.addItems([
            "İstanbul → Ankara - 10:00",
            "Ankara → İzmir - 10:30",
            "İzmir → Antalya - 11:00",
            "Antalya → İstanbul - 11:30",
            "Balıkesir → Bursa - 12:00",
            "Kayseri → Ankara - 12:30",
            "Bolu → Sinop - 13:00",
            "Nevşehir → Manisa - 13:30",
            "Erzincan → Çorum - 14:00",
            "Isparta → Bursa - 14:30",
        ])
        layout.addWidget(self.listWidget)

        self.button_koltuk = QPushButton("Koltuk Seç")
        self.button_koltuk.setFont(QFont("Arial", 11, QFont.Bold))
        self.button_koltuk.setStyleSheet("""
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
        self.button_koltuk.clicked.connect(self.open_rezervasyon)
        layout.addWidget(self.button_koltuk)

        central_widget.setLayout(layout)

    def open_rezervasyon(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            self.rezervasyon = Rezervasyon(selected_item.text())
            self.rezervasyon.show()
        else:
            QMessageBox.warning(self, "Hata", "Lütfen bir sefer seçin!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SeferListesi()
    window.show()
    sys.exit(app.exec_())
