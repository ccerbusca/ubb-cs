"""
    This module contains the Client class definition
"""

class Client:
    __id = 0
    def __generateID(self):
        Client.__id += 1
        return Client.__id

    @property
    def clientID(self):
        return self.__clientID
    
    @property
    def name(self):
        return self.__name
    
    @clientID.setter
    def clientID(self, new):
        self.__clientID = new

    @name.setter
    def name(self, new):
        self.__name = new

    def __init__(self, name):
        self.__clientID = self.__generateID()
        self.__name = name
    
    def __str__(self):
        return "{}. {}".format(self.__clientID, self.__name)
    
    def __eq__(self, client2):
        return self.__name == client2.name