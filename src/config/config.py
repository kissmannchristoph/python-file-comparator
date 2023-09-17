import json
import root

CONFIG_FILE = root.getMainPath('config.json')


class ConfigData:
    teamsOfflineDir = str

    def __init__(self, input):
        self.teamsOfflineDir = input.get('teamsOfflineDir')


class Config:

    @staticmethod
    def getConfig() -> ConfigData:
        # open text file in read mode
        text_file = open(CONFIG_FILE, "r")

        # read whole file to a string
        data = text_file.read()

        # close file
        text_file.close()

        return json.loads(data, object_hook=ConfigData)
