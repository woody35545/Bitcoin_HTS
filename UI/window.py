###### Import_part ######
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyupbit
import sys
LOGIN_STATUS = 0
ACCESS_KEY = ""
SECRET_KEY = ""
###### Update part ######
updates = open("../Data/updates.txt", "r", encoding='UTF8')
updates_str = ""
while True:
    text = updates.readline()
    if not text:
        break
    updates_str = updates_str + text
updates.close()

####### Form_initialize_part ########
mainwindow_form = uic.loadUiType("../UI/gui.ui")[0]

###### WindowClass_Initialize #######

class WindowClass(QMainWindow, mainwindow_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.textEdit_console.setText(updates_str)
        self.btn_bitcoinPrice.clicked.connect(self.btn_bitcoinPrice_action)
        self.btn_balance.clicked.connect(self.btn_balance_action)
        self.btn_update.clicked.connect(self.btn_update_action)
        self.lineEdit.returnPressed.connect(self.lineEdit_returnPressed_action)
    def btn_bitcoinPrice_action(self):
        txt = str(pyupbit.get_current_price("KRW-BTC")) + "₩"
        self.textEdit_console.setText(txt)
    def lineEdit_returnPressed_action(self):
        # 커맨드를 입력하기 위한 lineEdit 컴포넌트
        bringText = self.lineEdit.text()
        self.textEdit_console.append(str("> ")+str(bringText))
        self.lineEdit.setText("")
    def btn_balance_action(self):
        global myAccount
        myAccount = pyupbit.Upbit(ACCESS_KEY,SECRET_KEY)
        self.textEdit_console.setText(str(myAccount.get_balances()))
        res = myAccount.get_balances()
        if(res['error']['name'] == str("invalid_access_key")):
            print ("잘못된 키값입니다.")
    def btn_update_action(self):
        self.textEdit_console.setText(updates_str)
##########################
app = QApplication(sys.argv)
mainWindow = WindowClass()
app.exec_()

##########################