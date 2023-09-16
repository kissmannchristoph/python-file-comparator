from typing import List

import numpy

from src.config.config import MAIN_PATH
import json
from array import array
import numpy as np
from enum import Enum

from src.file.file import FileUtils

STORAGE_PATH = MAIN_PATH + 'storage\\'
CONFIG_FILE = STORAGE_PATH + 'config.json'
DEFAULT_STORAGE = 'main'


class ChangedFileType(Enum):
    CHANGED_FILE_TYPE_CREATE = 1
    CHANGED_FILE_TYPE_DELETE = 2
    CHANGED_FILE_TYPE_UPDATE = 3


class ChangedFileAction(Enum):
    CHANGED_FILE_ACTION_REPLACE = 1
    CHANGED_FILE_ACTION_NEW_VERSION = 2
    CHANGED_FILE_ACTION_HOLD = 3


class File(object):
    name: str
    path: str

    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path


class ChangedFile(object):
    changedFileType: ChangedFileType
    changedFileAction: None | ChangedFileAction
    changed: int
    oldFile: File | None
    newFile: File | None

    def __init__(self, changedFileType: ChangedFileType, oldFile: File | None, newFile: File | None):
        self.changedFileAction = ChangedFileAction.CHANGED_FILE_ACTION_REPLACE

        self.changedFileType = changedFileType
        self.changed = 0
        self.oldFile = oldFile
        self.newFile = newFile


class Storage:
    name: str
    teamsDir: str

    def __init__(self, name: str, teamsDir: str):
        self.name = name
        self.teamsDir = teamsDir

    @staticmethod
    def getConfig():
        # open text file in read mode
        text_file = open(CONFIG_FILE, "r")

        # read whole file to a string
        data = text_file.read()

        # close file
        text_file.close()

        return StorageConfiguration(**json.loads(data))

    def getPath(self):
        return STORAGE_PATH + self.name

    def getTeamsPath(self):
        return self.teamsDir

    def compare(self) -> List[ChangedFile]:
        list = []

        storageFileList = FileUtils.getFilesRecursive(self.getPath(), 0)
        teamsFileList = FileUtils.getFilesRecursive(self.teamsDir, 0)

        for teamsFile in teamsFileList:
            if not FileUtils.existsFile(self.getPath() + ('\\' + teamsFile.replace('C:\\', '')).replace('\\\\', '\\')):
                list.append(ChangedFile(
                    ChangedFileType.CHANGED_FILE_TYPE_CREATE,
                    None,
                    File(
                        teamsFile,
                        teamsFile
                    )
                ))

            elif not FileUtils.compareFile(teamsFile.replace('\\\\', '\\'),
                                           self.getPath() + ('\\' + teamsFile.replace('C:\\', '')).replace('\\\\',
                                                                                                           '\\')):
                list.append(ChangedFile(
                    ChangedFileType.CHANGED_FILE_TYPE_UPDATE,
                    File(
                        self.getPath() + teamsFile.replace('C:\\', ''),
                        self.getPath() + teamsFile.replace('C:\\', '')
                    ),
                    File(
                        teamsFile,
                        teamsFile
                    )
                ))

                storageFileList.remove(self.getPath() + ('\\' + teamsFile.replace('C:\\', '')).replace('\\\\', '\\'))
            else:
                storageFileList.remove(self.getPath() + ('\\' + teamsFile.replace('C:\\', '')).replace('\\\\', '\\'))

        for removedFile in storageFileList:
            list.append(ChangedFile(
                ChangedFileType.CHANGED_FILE_TYPE_DELETE,
                File(
                    removedFile,
                    removedFile
                ),
                None
            ))

        return list

    def proceedComparation(self, changedFiles: List[ChangedFile]):

        for changedFile in changedFiles:
            if changedFile.changedFileAction is ChangedFileAction.CHANGED_FILE_ACTION_REPLACE:
                if changedFile.changedFileType is ChangedFileType.CHANGED_FILE_TYPE_DELETE:
                    FileUtils.deleteFile(changedFile.oldFile.path)
                    changedFile.changed = 1

                if changedFile.changedFileType is ChangedFileType.CHANGED_FILE_TYPE_UPDATE:
                    FileUtils.copyFile(changedFile.newFile.path,
                                       self.getPath() + '\\' + changedFile.newFile.path.replace('C:\\', '').replace(
                                           '\\\\',
                                           '\\'))
                    changedFile.changed = 1

                if changedFile.changedFileType is ChangedFileType.CHANGED_FILE_TYPE_CREATE:
                    FileUtils.copyFile(changedFile.newFile.path,
                                       self.getPath() + '\\' + changedFile.newFile.path.replace('C:\\', '').replace(
                                           '\\\\', '\\'))
                    changedFile.changed = 1

            if changedFile.changedFileAction is ChangedFileAction.CHANGED_FILE_ACTION_NEW_VERSION:
                if changedFile.changedFileType is ChangedFileType.CHANGED_FILE_TYPE_UPDATE:
                    found = 0
                    v = 2

                    while found != 0:
                        if FileUtils.existsFile(self.getPath() + '\\' + changedFile.newFile.path.replace('C:\\', '').replace(
                                           '\\\\',
                                           '\\') + "_" + v):
                            v = v + 1

                        else:
                            found = 1
                            break

                    FileUtils.copyFile(changedFile.newFile.path,
                                       self.getPath() + '\\' + changedFile.newFile.path.replace('C:\\', '').replace(
                                           '\\\\',
                                           '\\') + "_" + str(v))
                    changedFile.changed = 1

            if changedFile.changedFileAction is ChangedFileAction.CHANGED_FILE_ACTION_HOLD:
                changedFile.changed = 1

        return changedFiles


class StorageData(object):
    teamsDir: str
    name: str

    def __init__(self, teamsDir: str, name: str):
        self.name = name
        self.teamsDir = teamsDir

    def getStorage(self):
        return Storage(self.name, self.teamsDir)


class StorageConfiguration(object):
    currentStorage: str
    storages: List[StorageData]

    def __init__(self, currentStorage: str, storages: List[StorageData]):
        self.currentStorage = currentStorage
        self.storages = []

        for i, val in enumerate(storages):
            self.storages.append(StorageData(val['teamsDir'], val['name']))

    def getStorages(self):
        return self.storages
