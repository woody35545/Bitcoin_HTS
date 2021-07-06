import sys
from PyQt5.QtWidgets import *
from UI import window
import time
import threading
import os
import datetime
import pyupbit
access_key = ""
secret_key = ""
myAccount = pyupbit.Upbit(access_key,secret_key)
trading_stradegy = 0
hold = False
trademode = False
targetPrice = 0
# Threads
class thr_console(threading.Thread):
    def run(self):
        print_console()
def calculate_target_price (ticker):
    ticker_dataFrame = pyupbit.get_ohlcv(ticker)
    today_data = ticker_dataFrame.iloc[-1]
    yesterday_data =  ticker_dataFrame.iloc[-2]
    data_range = yesterday_data['high'] -  yesterday_data['low']
    target_price = today_data['open'] + data_range * 0.5
    return target_price
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
            print(f":::RUNNING::: [{n1.year}.{n1.month}.{n1.day} {n1.hour}시{n1.minute}분{int(n1.second)}초]  | 보유자금: {get_my_KRW_balance()}원 | 목표매수가: {get_targetPrice()}원 | + 현재가: {cur} 원 | 보유상태: {isHold()} | 자동거래: {isTradeModeON()} |")

            time.sleep(1)
def get_targetPrice():
    return targetPrice
def update_targetPirce(ticker):
    global targetPrice
    targetPrice = calculate_target_price(ticker)
def trade():
    None

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
    if isTradeModeON() and coin_current_price >= targetPrice and isHold() == False:
        myAccount.buy_market_order(ticker, myAccount.get_balance("KRW"))
        setHold(False)
def sell_vbos(ticker):
    if isTradeModeON() and isMarketCloseTime() and isHold():
        coin_balance = myAccount.get_balance(ticker)
        myAccount.sell_market_order(ticker, coin_balance)
        setHold(False)
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
        print("[setting] gui mode > " ,end = '')
        _gui_mode= input()
        if _gui_mode == "1":
            print("[console] gui on!")
            app = QApplication(sys.argv)
            mainWindow = window.WindowClass()
            app.exec_()
            time.sleep(0.5)

        else:
            print("[console] GUI_MODE off!")
        time.sleep(0.5)
        os.system("cls")
        print("[setting] status print mode > ")
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
        print("[setting] select trading stradegy > ")
        trade_stradegy = input()
        if trade_stradegy == "1":
            thr = thr_trade_vbos()
            thr.start()
        else:
            ("Wrong!")



console = thr_console()
console.start()