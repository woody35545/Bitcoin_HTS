import sys
from PyQt5.QtWidgets import *

import tools
import window
from data import uuids_dataIn
import data as db
from tools import p
#TESTING


for i in  range (5):
    uuids_dataIn(f"data[{i}]")
    db.save_uuidsToTxtFile()
tools.listp(db.uuids,"uuids")


