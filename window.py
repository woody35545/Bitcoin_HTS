from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyupbit


updates = open("updates.txt","r",encoding='UTF8')
updates_str = ""
while True:
    text = updates.readline()
    if not text:
        break
    updates_str = updates_str + text
updates.close()

form_class = uic.loadUiType("gui.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textEdit_console.setText(updates_str)
        self.btn_bitcoinPrice.clicked.connect(self.btn_bitcoinPrice_action)
        self.btn_login.clicked.connect(self.btn_login_action)
        self.btn_balance.clicked.connect(self.btn_balance_action)
        self.btn_update.clicked.connect(self.btn_update_action)
    def btn_bitcoinPrice_action(self):
        txt = str(pyupbit.get_current_price("KRW-BTC")) + "₩"
        self.textEdit_console.setText(txt)

    def btn_login_action(self):
        global ACCESS_KEY
        global SECRET_KEY
        ACCESS_KEY = str(self.textEdit_accessKey.toPlainText())
        SECRET_KEY = str(self.textEdit_secretKey.toPlainText())
        print ("ACCESS_KEY = " + ACCESS_KEY)
        print ("SECRET_KEY = " + SECRET_KEY)
        self.textEdit_console.setText("ACCESS_KEY = " + ACCESS_KEY +"\n"+ "SECRET_KEY = " + SECRET_KEY)

    def btn_balance_action(self):
        global myAccount
        myAccount = pyupbit.Upbit(ACCESS_KEY,SECRET_KEY)
        self.textEdit_console.setText(str(myAccount.get_balances()))
        print(myAccount.get_balances())

    def btn_update_action(self):
        self.textEdit_console.setText(updates_str)
