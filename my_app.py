#my_app.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
 
from instr import *
from second_win import *
     
class MainWin(QWidget):
   def __init__(self):
       ''' окно, в котором располагается приветствие '''
       super().__init__()
def  initUI(self):
    self.hello_text = QLabel(txt_hello)
    self.instruction = QLabel(txt_instruction)
    self.button = QPushButton(txt_next)
    self.layout = QVBoxLayout()
    self.hello_text.addWidget(self.layout)
    self.instruction.addWidget(self.layout)
    self.button.addWidget(self.layout)

    
    #my_app.py
from instr import *
class MainWin(QWidget):
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
    def connects(self):
        self.btn_next,clicked.connect(self.next_click)
    def next_click(self):
        #Обработка нажатия на кнопку: спрятать текущее окно и создать следущее
