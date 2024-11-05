import sys
from cProfile import label
import random

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QGridLayout, QStackedLayout)

from CajaColor import CajaColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ejemplo QStackLayout')
        self.setFixedSize(400, 400)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("purple"))
        self.setPalette(paleta)

        caja_central = QVBoxLayout()
        caja_superior = QVBoxLayout()
        self.button_cambio = QPushButton("cambio aleatorio")
        self.button_cambio.clicked.connect(self.cambioAleatorio)
        self.stack_layout = QStackedLayout()
        self.stack_layout.addWidget(CajaColor("red"))
        self.stack_layout.addWidget(CajaColor("blue"))
        self.stack_layout.addWidget(CajaColor("orange"))
        self.stack_layout.addWidget(CajaColor("yellow"))
        self.stack_layout.addWidget(CajaColor("pink"))
        self.stack_layout.addWidget(CajaColor("gray"))
        self.stack_layout.addWidget(CajaColor("white"))

        caja_superior.addWidget(self.button_cambio)
        caja_central.addLayout(self.stack_layout)
        caja_central.addLayout(caja_superior)



        self.stack_layout.setCurrentIndex(1)

        container = QWidget()
        container.setLayout(caja_central)
        self.setCentralWidget(container)
        self.show()

    def cambioAleatorio(self):
        numero = random.randint(0, 6)
        self.stack_layout.setCurrentIndex(numero)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()

