import os
import sys

MAIN_PATH = os.path.dirname(os.path.realpath(__file__))

argsString = ""

for arg in sys.argv:
    argsString += " " + arg

os.system("python main.py '" + MAIN_PATH + "' --fromstart" + argsString)