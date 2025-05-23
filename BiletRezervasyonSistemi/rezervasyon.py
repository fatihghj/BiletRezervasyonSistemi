from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
from database import rezervasyon_ekle

class Rezervasyon(QMainWindow):
    def __init__(self, sefer):
        super().__init__()
        self.setWindowTitle("Koltuk Seçimi")
        self.setGeometry(100, 100, 1200, 400)
        self.setStyleSheet("background-color: IndianRed;")

        self.secilen_sefer = sefer
        self.koltuklar = []

        self.card = QWidget()
        self.card.setStyleSheet("""
            background-color: white;
            border-radius: 20px;
            padding: 20px;
        """)
        self.card.setFixedSize(1150, 350)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        self.label = QLabel("Koltuk Seçimi")
        self.label.setFont(QFont("Arial", 14, QFont.Bold))
        self.label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(self.label, alignment=Qt.AlignCenter)

        grid = QGridLayout()
        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(20)

        koltuk_no = 1
        for row in [0, 2]:  
            for col in range(17): 
                if col == 0 or col == 16:
                    spacer = QLabel("")  
                    grid.addWidget(spacer, row, col)
                elif col == 8:
                    spacer = QLabel("") 
                    grid.addWidget(spacer, row, col)
                else:
                    btn = QPushButton(str(koltuk_no))
                    btn.setCheckable(True)
                    btn.setFixedSize(60, 60)
                    btn.setFont(QFont("Arial", 12, QFont.Bold))
                    btn.setStyleSheet("""
                        QPushButton {
                            background-color: #e74c3c;
                            color: white;
                            border-radius: 15px;
                        }
                        QPushButton:hover {
                            background-color: #c0392b;
                        }
                        QPushButton:checked {
                            background-color: #27ae60;
                        }
                    """)
                    self.koltuklar.append(btn)
                    grid.addWidget(btn, row, col)
                    koltuk_no += 1

        layout.addLayout(grid)

        btn_onayla = QPushButton("Onayla")
        btn_onayla.setFont(QFont("Arial", 11, QFont.Bold))
        btn_onayla.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border-radius: 20px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        btn_onayla.clicked.connect(self.onayla)
        layout.addWidget(btn_onayla, alignment=Qt.AlignCenter)

        self.card.setLayout(layout)

        outer_layout = QVBoxLayout()
        outer_layout.addWidget(self.card, alignment=Qt.AlignCenter)

        central = QWidget()
        central.setLayout(outer_layout)
        self.setCentralWidget(central)

    def onayla(self):
        secilen = [k.text() for k in self.koltuklar if k.isChecked()]
        if secilen:
            for koltuk in secilen:
                rezervasyon_ekle(self.secilen_sefer, koltuk)
            QMessageBox.information(self, "Başarılı", f"Seçilen Koltuklar: {', '.join(secilen)}")
            self.close()
        else:
            QMessageBox.warning(self, "Hata", "Lütfen en az bir koltuk seçin!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Rezervasyon("İstanbul → Ankara - 10:00")
    window.show()
    sys.exit(app.exec_())
