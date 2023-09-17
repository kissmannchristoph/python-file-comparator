import base64
import os
import sys
from typing import List

import root
from src.config.storage import Storage, StorageData
from array import array
import numpy as np
import src.file.file
from src.config.storage import StorageData
import src.cmd.cmd
from src.file.template import copyTemplates


print("start")


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

    if src.cmd.cmd.getArg('run') is not None:
        print('run')
        Storage.getConfig().getStorages()[0].getStorage().proceedComparation(comp)




for arg in sys.argv:
    print("ARG: " + arg)

for tpl in copyTemplates(root.getMainPath()):
    print("PACKAGE Template: " + tpl)

if src.cmd.cmd.getArg('compare') is not None:
    print('compare')
    compTest()

print("watchInput")
