import sys
from PyQt5.QtWidgets import *

from Modules import tools, tools as t
from UI import window
from Data.data import uuids_dataIn
from Data import data as db
from Modules.tools import p, textReplace, get_fileContents
from Modules import api
#p(str(t.textReplace(t.get_fileContents("UI/window.py"),"textEdit_secretKey","lineEdit_secretKey")))

#ACCESS_KEY = str(self.textEdit_accessKey.toPlainText())
#SECRET_KEY = str(self.textEdit_secretKey.toPlainText())

api.get_myBalance()