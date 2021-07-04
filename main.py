import sys
from PyQt5.QtWidgets import *
import window

app = QApplication(sys.argv)
mainWindow = window.WindowClass()
loginWindow = window.LoginWindow()
#mainWindow.hide()
#loginWindow.show()
app.exec_()



