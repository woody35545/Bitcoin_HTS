###### Import_part ######
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyupbit
import sys
from Modules import functions, tools
from Modules.tools import p
from Data import data as db
LOGIN_STATUS = 0
access_key = ""
secret_key = ""
###### Update part ######
updates = open("Data/updates.txt", "r", encoding='UTF8')
updates_str = ""
while True:
    text = updates.readline()
    if not text:
        break
    updates_str = updates_str + text
updates.close()

####### Form_initialize_part ########
loginwindow_form = uic.loadUiType("UI/login.ui")[0]
mainwindow_form = uic.loadUiType("UI/gui.ui")[0]

###### WindowClass_Initialize #######
class LoginWindow(QWidget, loginwindow_form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.show()
        self.btn_login.clicked.connect(self.btn_login_action)

    def btn_login_action(self):

        response = ""
        access_key = str(self.lineEdit_accessKey.text())
        secret_key = str(self.lineEdit_secretKey.text())
        reply=  QMessageBox.question(self, 'Message', '해당 정보로 로그인 하시겠습니까?',
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            None

        elif reply == QMessageBox.Yes and (ACCESS_KEY != "") :

            print("ACCESS_KEY = " + access_key)
            print("SECRET_KEY = " + secret_key)
            mainWindow.show()
            self.hide
        else:
            QMessageBox.question(self, 'Message', '옳바른 키값이 아닙니다.',QMessageBox.Yes)
class WindowClass(QMainWindow, mainwindow_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hide()
        #self.lineEdit_accessKey= QLineEdit()
        #self.lineEdit_accessKey.setEchoMode(QLineEdit.Password)

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
       # self.textEdit_console.moveCursor(QtGui.QTextCursor.End) # 자동 스크롤 내림 기능 구현중 ..

        self.lineEdit.setText("")


    def btn_balance_action(self):
        global myAccount
        myAccount = pyupbit.Upbit(ACCESS_KEY,SECRET_KEY)
        self.textEdit_console.setText(str(myAccount.get_balances()))

        res = myAccount.get_balances()
        if(res['error']['name'] == str("invalid_access_key")):
            print ("잘못된 키값입니다.")
        #print(res['error']['name'])

    def btn_update_action(self):
        self.textEdit_console.setText(updates_str)
##########################
app = QApplication(sys.argv)
mainWindow = WindowClass()
loginWindow = LoginWindow()
#mainWindow.hide()
#loginWindow.show()
app.exec_()

##########################