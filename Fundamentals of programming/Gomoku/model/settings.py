import configparser


class Settings:
    def __init__(self):
        self.__config = configparser.RawConfigParser()
        self.__config.read("ui.settings")
        self.uiType = self.__config["Type"]["ui"]
