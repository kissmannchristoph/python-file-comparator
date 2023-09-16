
import base64
import sys
from typing import List

from src.config.storage import Storage, StorageData
from array import array
import numpy as np
import src.file.file
from src.config.storage import StorageData


for arg in sys.argv:
    print('ARG ' + arg)

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

#x = g[0].getStorage().proceedComparation(comp)

#print(x)
