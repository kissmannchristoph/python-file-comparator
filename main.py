
import base64
import os
import sys
from typing import List

from src.config.storage import Storage, StorageData
from array import array
import numpy as np
import src.file.file
from src.config.storage import StorageData
import src.cmd.cmd
from src.file.template import copyTemplates

ROOT_PATH = sys.argv[0]
MAIN_PATH = os.path.dirname(os.path.realpath(__file__))

print("start")
print("MAIN_PATH: " + MAIN_PATH)

if not MAIN_PATH is sys.argv[0]:
    print("set new MAIN_PATH: " + os.path.dirname(sys.argv[0]))
    MAIN_PATH = os.path.dirname(sys.argv[0])

for arg in sys.argv:
    print("ARG: " + arg)

for tpl in copyTemplates(ROOT_PATH):
    print("Template: " + tpl)

for tpl in copyTemplates(MAIN_PATH):
    print("PACKAGE Template: " + tpl)

def compTest():
    g = Storage.getConfig().getStorages()
    comp = g[0].getStorage().compare()

    for d in comp:
        oldFile = 'None'
        newFile = 'None'

        if not d.oldFile is None:
            oldFile = d.oldFile.path

        if not d.newFile is None:
            newFile = d.newFile.path

        print("Action: " + d.changedFileType.name + " newFile: " + newFile + " oldFile: " + oldFile)

    if len(comp) == 0:
        print('NO CHANGES')

