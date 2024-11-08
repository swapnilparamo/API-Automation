import configparser


def getMethodEndpoint():
    config = configparser.ConfigParser()

    # konti file with extention ini ticha path dyaicha
    config.read("C:\\Users\\swapnil.bedse\\PycharmProjects\\pythonProject\\apiAutomation\\utilities\\global.ini")
    return config


