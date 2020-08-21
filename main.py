from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import sys 


app = QApplication([])

# app.setStyleSheet("QPushButton { margin: 20ex; color: blue; }")
button = QPushButton('Attendance')



button.show()
app.exec_()