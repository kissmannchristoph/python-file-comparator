import os


def copyTemplates(ROOT_PATH: str):
    templatePath = os.path.join(ROOT_PATH, 'templates')

    templates = []

    for entry in os.listdir(templatePath):
        templates.append(entry)

    return templates
