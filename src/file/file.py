import os
from typing import List
import filecmp
import shutil
import hashlib

class FileUtils:

    @staticmethod
    def existsFile(path: str) -> bool:
        return os.path.isfile(path)

    @staticmethod
    def deleteFile(path: str):
        os.remove(path)

    @staticmethod
    def copyFile(firstPath: str, secondPath: str):
        secondPathDir = secondPath.replace(secondPath.split('\\')[len(secondPath.split('\\')) - 1], '')
        os.makedirs(secondPathDir, exist_ok=True)
        shutil.copyfile(firstPath, secondPath)

    @staticmethod
    def compareFile(firstPath: str, secondPath: str) -> bool:
        return filecmp.cmp(firstPath, secondPath)

    @staticmethod
    def getFileHash(filename):
        """"This function returns the SHA-1 hash
        of the file passed into it"""

        # make a hash object
        h = hashlib.sha1()

        # open file for reading in binary mode
        with open(filename, 'rb') as file:
            # loop till the end of the file
            chunk = 0
            while chunk != b'':
                # read only 1024 bytes at a time
                chunk = file.read(1024)
                h.update(chunk)

        # return the hex representation of digest
        return h.hexdigest()

    @staticmethod
    def getFilesRecursive(path: str, isSubDir: int) -> List[str]:
        list = []

        for path, dirs, files in os.walk(path):
            if isSubDir != 1:
                for f in files:
                    list.append(path + '\\' + f)

            for d in dirs:
                for f in FileUtils.getFilesRecursive(path + '\\' + d, 1):
                    list.append(f)

        return list


class StorageFileUtils:

    @staticmethod
    def getDifferences() -> dict:
        return dict([("asd", "asdsss")])
