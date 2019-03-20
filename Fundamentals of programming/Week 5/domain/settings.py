import configparser

class Settings:
    def __init__(self, file):
        self.__config = configparser.RawConfigParser()
        self.__config.read(file)
        self.repositoryType = self.__config["Type"]["repository"]
        if self.repositoryType.lower() == "file":
            self.moviesFile = self.__config["File"]["movies"]
            self.rentalsFile = self.__config["File"]["rentals"]
            self.clientsFile = self.__config["File"]["clients"]
        elif self.repositoryType.lower() == "binaryfile":
            self.moviesFile = self.__config["BinaryFile"]["movies"]
            self.rentalsFile = self.__config["BinaryFile"]["rentals"]
            self.clientsFile = self.__config["BinaryFile"]["clients"]
    