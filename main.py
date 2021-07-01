import sys
from PyQt5.QtWidgets import *
import window

app = QApplication(sys.argv)
mainWindow = window.WindowClass()
mainWindow.show()
app.exec_()



