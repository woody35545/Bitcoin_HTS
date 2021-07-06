import sys
from PyQt5.QtWidgets import *
from UI import window
import time
import threading
import os
import datetime
import pyupbit
from Modules import api
import openpyxl
access_key = ""
secret_key = ""
myAccount = pyupbit.Upbit(access_key,secret_key)
trading_stradegy = 0
hold = False
trademode = True
targetPrice = 0
show = 1
#Test
#exel1 = openpyxl.Workbook()
#sheet1 = exel1.active
#sheet1['A1'] = "A1"
#exel1.save("Data/data.xlsx")

# Threads
class thr_console(threading.Thread):
    def run(self):
        print_console()
class thr_trade (threading.Thread):
    def run(self):
        trade()
class thr_trade_vbos (threading.Thread):
    def run(self):

        while True:
            n1 = datetime.datetime.now()
            cur = get_current_price("KRW-XRP")
            sell_vbos("KRW-XRP")
            buy_vbos("KRW-XRP")
            print(f":::RUNNING::: [ " + get_today()+ f" {n1.hour}시{n1.minute}분{int(n1.second)}초]  | 보유자금: {get_my_KRW_balance()}원 | 목표매수가: {get_targetPrice()}원 | + 현재가: {cur} 원 | 보유상태: {isHold()} | 자동거래: {isTradeModeON()} |")
            time.sleep(1)
class thr_test (threading.Thread):
    def run(self):
        test()

def test():
     i=0
     while True:

        if show == 1:
            a = api.get_coin_current_data().json()

            print("["+str(i)+"]"+str(a[0]['trade_price']))
            time.sleep(1)
            i += 1
        else:
            None

def get_targetPrice():
    return targetPrice
def update_targetPirce(ticker):
    global targetPrice
    targetPrice = calculate_target_price(ticker)
def calculate_target_price (ticker):
    ticker_dataFrame = pyupbit.get_ohlcv(ticker)
    today_data = ticker_dataFrame.iloc[-1]
    yesterday_data =  ticker_dataFrame.iloc[-2]
    data_range = yesterday_data['high'] -  yesterday_data['low']
    target_price = today_data['open'] + data_range * 0.5
    return target_price

def trade():
    None
def setAccessKey(data):
    global access_key
    access_key = data
def setSecretKey(data):
    global secret_key
    secret_key = data
def isMarketOpenTime():
    now = datetime.datetime.now()
    if now.hour == 9 and now.minute and (20<= now.second <= 30):
        return True
    else:
        return False
def isMarketCloseTime():
    now = datetime.datetime.now()
    if now.hour == 8 and now.minute == 59 and (50 <= now.second <= 59):
        return True
    else:
        return False
def isTradeModeON():
    if trademode == True :
        return True
    else:
        return False
def isHold():
    if hold == True:
        return True
    else:
        return False
def setHold(bool):
    global hold
    hold = bool
def get_my_KRW_balance():
    global myAccount
    return myAccount.get_balance("KRW")
def get_current_price(ticker):
    pyupbit.get_current_price(ticker)
def buy_vbos(ticker):
    coin_current_price = get_current_price(ticker)
    if isTradeModeON() and int(coin_current_price) >= int(get_targetPrice()) and isHold() == False:
        myAccount.buy_market_order(ticker, myAccount.get_balance("KRW"))
        setHold(False)
def sell_vbos(ticker):
    if isTradeModeON() and isMarketCloseTime() and isHold():
        coin_balance = myAccount.get_balance(ticker)
        myAccount.sell_market_order(ticker, coin_balance)
        setHold(False)
def get_today():
    n = datetime.datetime.now()
    year =str(n.year)
    month = str(n.month)
    day = str(n.day)
    return str(year +"."+month+"."+day+" " )
def get_time_now():
    n = datetime.datetime.now()
    h = str(n.hour)
    m = str(n.minute)
    s = str(int(n.second))
    return str()
def getAccessKey():
    return access_key
def getSecretKey():
    return secret_key
def isValidKey():
    if (pyupbit.Upbit(access_key,secret_key).get_balances()['error']['name'] == "invalid_access_key"):

        return False
    else:
        return True
def sleepAndCls():
    time.sleep(0.5)
    os.system("cls")
def sleep(time):
    time.sleep(time)
def isInt(data):
    if     str(type(data)) == "<class ='int'>":
        return True
    else :
        return False
def print_console():
    _status_print_mode = 0
    _gui_mode = 0

    def clp():
        print(">", end = '')
    def print_trade_mode():
        print("* Trading Modes *")
        print("[1] VBOS")
        print("[2] short")
    while True:

        while True:
            print("[Login] ACCESS_KEY > " ,end="")
            setAccessKey(input())
            print("[Login] SECRET_KEY > " ,end="")
            setSecretKey(input())
            if not isValidKey():
                print("[console] 유효하지 않은 key값 입니다.")
            else:
                print("[console] 로그인 성공!")
                api.set_keys(getAccessKey(),getSecretKey())
                api.get_myBalance()
                sleepAndCls()
                break
        print("[setting] gui mode > " ,end = '')
        _gui_mode= input()

        if _gui_mode == "1":
            print("[console] gui on!")
            app = QApplication(sys.argv)
            mainWindow = window.WindowClass()
            app.exec_()
            time.sleep(0.5)

        else:
            print("[console] GUI_MODE off!" ,end = '')
        sleepAndCls()

        print("[setting] status print mode > " ,end = '')
        _status_print_mode = input()
        if _status_print_mode == "1":
            print("[console] STATUS_PRINT_MODE on!")
            time.sleep(0.5)
            os.system("cls")
        else:
            print("[console] STATUS_PRINT_MODE off!")
            time.sleep(0.5)
            os.system("cls")
        print_trade_mode()
        print("[setting] select trading stradegy > " ,end = '')
        trade_stradegy = input()
        if trade_stradegy == "1":
            thr = thr_trade_vbos()
            thr.start()
        else:
            ("Wrong!")
testing_Thr = thr_test()
testing_Thr.start()

console = thr_console()
console.start()
