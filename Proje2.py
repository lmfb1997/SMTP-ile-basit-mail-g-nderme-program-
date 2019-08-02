import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit
import sys


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.epostaLabel = QLabel("Alıcı")
        self.epostaKime  = QLineEdit()

        self.konuLabel = QLabel("Konu")
        self.konuLineEdit = QLineEdit()


        self.yazi_alani  = QTextEdit()
        self.buton = QPushButton("Gönder")

        h_box = QHBoxLayout()
        h_box.addWidget(self.epostaLabel)
        h_box.addWidget(self.epostaKime)


        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        h_box.addWidget(self.konuLabel)
        h_box.addWidget(self.konuLineEdit)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)
        self.buton.clicked.connect(self.click)
        self.show()
    def click(self):
        mesaj = MIMEMultipart()

        mesaj["From"] = "brkklc1934@gmail.com"
        mesaj["To"] = self.epostaKime.text()
        mesaj["Subject"] = self.konuLineEdit.text()
        yazi = self.yazi_alani.toPlainText()

        mesaj_govdesi = MIMEText(yazi, "plain")
        mesaj.attach(mesaj_govdesi)
        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)

            mail.ehlo()

            mail.starttls()

            mail.login("brkklc1934@gmail.com", "*************")
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            print("Mail başarıyla gönderildi....")

            mail.close()
        except:
            sys.stderr.write("Bir sorun oluştu!")
            sys.stderr.flush()

app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())


