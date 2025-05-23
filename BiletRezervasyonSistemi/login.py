from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys
from main_menu import MainMenu

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kullanıcı Girişi")
        self.setGeometry(100, 100, 500, 350)
        self.setStyleSheet("background-color: IndianRed;")

        
        self.card = QWidget()
        self.card.setFixedSize(350, 300)
        self.card.setStyleSheet("""
            background-color: #ffffff;
            border-radius: 15px;
            padding: 30px;
            border: 1px solid #ddd;
        """)

        card_layout = QVBoxLayout()
        card_layout.setAlignment(Qt.AlignCenter)

        # Başlık
        self.title_label = QLabel("Giriş Yap")
        self.title_label.setFont(QFont('Arial', 18, QFont.Bold))
        self.title_label.setStyleSheet("color: #333333; margin-bottom: 20px;")
        self.title_label.setAlignment(Qt.AlignCenter)

        # Kullanıcı adı
        self.input_user = QLineEdit()
        self.input_user.setPlaceholderText("Kullanıcı Adı")
        self.input_user.setFont(QFont('Arial', 11))
        self.input_user.setStyleSheet("""
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 8px;
        """)

        # Şifre
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password)
        self.input_pass.setPlaceholderText("Şifre")
        self.input_pass.setFont(QFont('Arial', 11))
        self.input_pass.setStyleSheet("""
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 8px;
        """)

        # Buton
        self.button_login = QPushButton("Giriş Yap")
        self.button_login.setFont(QFont('Arial', 12, QFont.Bold))
        self.button_login.setStyleSheet("""
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
        self.button_login.clicked.connect(self.check_login)

        # Widgetlar
        card_layout.addWidget(self.title_label)
        card_layout.addWidget(self.input_user)
        card_layout.addWidget(self.input_pass)
        card_layout.addWidget(self.button_login)
        card_layout.setSpacing(15)
        self.card.setLayout(card_layout)

        # Ana layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.card, alignment=Qt.AlignCenter)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    

    def check_login(self):
        username = self.input_user.text()
        password = self.input_pass.text()

        if username == "FatihM" and password == "Fatih1234":
            self.open_main_menu()
        else:
            QMessageBox.warning(self, "Hata", "Hatalı Kullanıcı Adı veya Şifre!")

    def open_main_menu(self):
        self.main_menu = MainMenu()
        self.main_menu.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
