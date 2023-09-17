import os.path
import sys
from os import path

from src.cmd import cmd

MAIN_PATH = os.path.dirname(os.path.realpath(__file__))

def getMainPathJ(*paths: str):
    return path.join(MAIN_PATH, *paths)

def getSysPath():
    if cmd.getArg('fromstart') is None:
        return sys.argv[0].replace("'", "")
    else:
        return sys.argv[1].replace("'", "")

def getMainPath(*paths: str):
    if MAIN_PATH != getSysPath():
        print("set new MAIN_PATH: " + os.path.dirname(getSysPath()))
        return getMainPathJ(os.path.dirname(getSysPath()), *paths)
    else:
        return getMainPathJ(MAIN_PATH, *paths)
