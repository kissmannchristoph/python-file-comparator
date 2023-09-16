import os

def copyTemplates(ROOT_PATH: str):
    templatePath = os.path.join(ROOT_PATH, 'templates')

    templates = []

    for path, dirs, files in os.walk(templatePath):
        for dir in dirs:
            templates.append(dir)
        for file in files:
            templates.append(file)


    return templates