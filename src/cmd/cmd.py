import sys


class KeyValuePar(object):
    key: str
    value: None | str

    def __init__(self, key: str, value: str | None):
        self.key = key
        self.value = value


def getArg(key: str) -> KeyValuePar | None:
    rt: KeyValuePar | None = None

    for arg in sys.argv:
        if arg.startswith('--' + key):
            cleanedArg = arg.replace('--', '')
            if "=" in arg:
                if cleanedArg.split("=")[1] is '':
                    rt = KeyValuePar(cleanedArg.split("=")[0], None)
                else:
                    rt = KeyValuePar(cleanedArg.split("=")[0], cleanedArg.split("=")[1])
                break
            else:
                rt = KeyValuePar(cleanedArg, None)
                break

    return rt

def proceedInput(input: str):
    print(input)

def watchInput():
    _input = str(input())
    proceedInput(_input)
    watchInput()