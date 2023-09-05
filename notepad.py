from PyQt6.QtWidgets import QWidget, QApplication, QFileDialog, QCheckBox, QLabel, QPushButton, QMainWindow, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QGroupBox, QRadioButton
from PyQt6 import QtWidgets
import sys
import os

class Notepad(QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.textplace = QTextEdit()
        self.clr = QPushButton("Clear")
        self.open = QPushButton("Open")
        self.save = QPushButton("Save")

        self.textplace.setStyleSheet("background-color: white")
        self.clr.setStyleSheet("background-color:#5f978f")
        self.open.setStyleSheet("background-color:#5f978f")
        self.save.setStyleSheet("background-color:#5f978f")

        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.clr)
        h_box.addWidget(self.open)
        h_box.addWidget(self.save)
        h_box.addStretch()

        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.textplace)
        v_box.addLayout(h_box)
        v_box.addStretch()

        self.clr.clicked.connect(self.temizle)
        self.open.clicked.connect(self.ac)
        self.save.clicked.connect(self.kaydet)

        self.setLayout(v_box)
        self.setWindowTitle("Notepad")
        self.setStyleSheet("background-color:#bae1ff")
        self.setGeometry(600, 200, 400, 300)
        self.setWindowTitle("Notepad")

        self.show()

    def temizle(self):
        self.textplace.clear()

    def ac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self, "Open File", os.getenv("HOME"))
        with open(dosya_ismi[0], "r+") as file:
            self.textplace.setText(file.read())


    def kaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self, "Save File", os.getenv("HOME"))
        with open(dosya_ismi[0], "w") as file:

            file.write(self.textplace.toPlainText())

app = QApplication(sys.argv)
notepad = Notepad()
sys.exit(app.exec())