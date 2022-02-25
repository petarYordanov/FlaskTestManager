from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read("configuration_data/config.ini")
    return config.get(section, key)
