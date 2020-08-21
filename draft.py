from PyQt5.QtWidgets import * 
from PyQt5 import QtCore 
from PyQt5.QtGui import * 
from PyQt5 import QtGui
import sys 
  
  
class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 

        self.setGeometry(0, 0, 600, 800) 
  
        self.setStyleSheet("background-color: #BBE1FA;") 
  
        self.setWindowTitle("My App") 

        button = QPushButton('Attendance', self)

        font=QtGui.QFont()
        font.setFamily('Roboto')
        font.setWeight(QFont.Bold)
        font.setPixelSize(50)

        button.setFont(font)
        button.setStyleSheet("background-color: #3282B8; width:26px; height:17px;")
        # pybutton.clicked.connect(self.clickMethod)
        button.resize(300,100)
        button.move(70, 250)   


        self.label = QLabel("Cyan", self) 
  
        self.label.move(100, 100) 
  
        self.label.setStyleSheet("border: 1px solid black;"
                                "background-color:  #0F4C75;" )
        self.show() 
  

App = QApplication(sys.argv) 
        
window = Window() 

sys.exit(App.exec()) 