import sys
from PyQt5.QtWidgets import *

import tools
from UI import window
from data import uuids_dataIn
import data as db
import tools as t
from tools import p, textReplace, get_fileContents
#TESTING


for i in  range (5):
    uuids_dataIn(f"data[{i}]")
