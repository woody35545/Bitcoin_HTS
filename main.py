import sys
from PyQt5.QtWidgets import *
import window
from data import uuids_dataIn
import data as db
from tools import p
#TESTING


for i in  range (5):
    uuids_dataIn(f"data[{i}]")
    p(f"{db.get_uuid(i)}")
    db.save_uuidsToTxtFile()