import sys
from PyQt5 import QtCore 
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My App")

        self.setGeometry(0, 0, 640, 360) 
  
        self.setStyleSheet("background-color: #BBE1FA;") 
  
        self.setWindowTitle("My App") 

        self.font_button = QtGui.QFont()
        self.font_button.setFamily('Roboto')
        self.font_button.setWeight(QFont.Bold)
        self.font_button.setPixelSize(20)

        font_time = QtGui.QFont()
        font_time.setFamily('Roboto')
        font_time.setWeight(QFont.Bold)
        font_time.setPixelSize(40)

        font_date = QtGui.QFont()
        font_date.setFamily('Roboto')
        font_date.setWeight(QFont.Bold)
        font_date.setPixelSize(15)

        self.label = QLabel(self) 
        self.label.setGeometry(0, 0, 375, 360) 
        self.label.setStyleSheet("background-color:  #0F4C75; ")

        self.label_small = QLabel(self)
        self.label_small.setGeometry(27, 25, 320, 240) 
        self.label_small.setStyleSheet("background-color:  #BBE1FA; border-radius: 20px;")

        
        self.button = QPushButton('Attendance', self)
        self.button.setFont(self.font_button)
        self.button.setStyleSheet("background-color: #3282B8; border-radius: 20px;color: #FFFFFF")
        self.button.resize(150,50)
        self.button.move(127, 290)   

        self.button.clicked.connect(self.say_hi)

#=================Group 1=============================
        self.group_1 = QWidget(self)
        self.group_1.setGeometry(400, 42, 220, 250)
        layout_1 = QVBoxLayout()

        button_yes = QPushButton("Yes")
        button_yes.setGeometry(410, 205, 200, 35)
        button_yes.setFont(self.font_button)
        button_yes.setStyleSheet("background-color: #0F4C75; color: #FFFFFF; border-radius: 10px")
        button_yes.clicked.connect(self.clicked_yes)

        button_no = QPushButton("No")
        button_no.setGeometry(410, 255, 200, 35)
        button_no.setFont(self.font_button)
        button_no.setStyleSheet("background-color: #FFFFFF; color: #0F4C75; border-radius: 10px")
        button_no.clicked.connect(self.clicked_no)

        label_id = QLabel()
        label_id.setGeometry(410, 42, 200, 100) 
        label_id.setStyleSheet("background-color: #0F4C75; border-radius: 10px")

        label_hello = QLabel("Hello, is this you?")
        label_hello.setAlignment(QtCore.Qt.AlignCenter)
        label_hello.setFont(self.font_button)
        label_hello.setGeometry(414, 157, 200, 30) 
        label_hello.setStyleSheet("color:  #0F4C75;")

        layout_1.addWidget(label_id)
        layout_1.addWidget(label_hello)
        layout_1.addWidget(button_yes)
        layout_1.addWidget(button_no)

        self.group_1.setLayout(layout_1)
#==============END of GROUP 1===================

#==============GROUP 2==========================
        self.group_2 = QWidget(self)
        self.group_2.setGeometry(390, 100, 240, 160)
        layout_2 = QVBoxLayout()

        timer = QTimer(self) 
        timer.timeout.connect(self.setTime) 
        timer.start(500) 
        
        self.label_time = QLabel()
        self.label_time.setGeometry(400, 100, 230, 60)
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setFont(font_time)
        self.label_time.setStyleSheet("color:  #0F4C75;")

        date = QDate.currentDate()
        label_date = QLabel(date.toString('ddd, MMM dd yyyy')) 
        label_date.setGeometry(427, 160, 165, 25)
        label_date.setAlignment(QtCore.Qt.AlignCenter)
        label_date.setFont(font_date)
        label_date.setStyleSheet("color:  #0F4C75;")

        label_Welcome = QLabel("Welcome!") 
        label_Welcome.setGeometry(400, 200, 222, 60)
        label_Welcome.setAlignment(QtCore.Qt.AlignCenter)
        label_Welcome.setFont(font_time)
        label_Welcome.setStyleSheet("color:  #0F4C75;")

        layout_2.addWidget(self.label_time)
        layout_2.addWidget(label_date)
        layout_2.addWidget(label_Welcome)

        self.group_2.setLayout(layout_2)
# =======END of GROUP 2==================

        self.group_1.hide()

    def say_hi(self):

        print("Clicked on Attendace.")
        self.group_1.show()
        self.group_2.hide()

    def setTime(self): 

        current_time = QTime.currentTime() 
        time = current_time.toString('hh:mm') 
        self.label_time.setText(time) 

    def clicked_yes(self):
        print("clicked to button yes!")

    def clicked_no(self):
        print("clicked to button no!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()