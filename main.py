import sys
from PyQt5.QtWidgets import *
import window
import data

#TESTING


for i in  range (5):
    data.uuids_dataIn(f"data[{i}]")
    print(f"{data.get_uuid(i)}")
data.save_uuidsToTxtFile()