import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read("E:\\PycharmProjects\\pythonProject\\apiAutomation\\utilities1\\aaa.ini")
    return config
