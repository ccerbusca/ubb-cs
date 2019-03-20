"""
    This module contains the class definition of Rental
"""

class Rental:
    __id = 0
    def __generateID(self):
        Rental.__id += 1
        return Rental.__id
    
    @property
    def rentalID(self):
        return self.__rentalID
    
    @property
    def movieID(self):
        return self.__movieID
    
    @property
    def clientID(self):
        return self.__clientID
    
    @property
    def rentedDate(self):
        return self.__rentedDate
    
    @property
    def dueDate(self):
        return self.__dueDate
    
    @property
    def returnedDate(self):
        return self.__returnedDate
    
    def setReturnedDate(self, new):
        self.returnedDate = new

    @rentalID.setter
    def rentalID(self, new):
        self.__rentalID = new
    
    @movieID.setter
    def movieID(self, new):
        self.__movieID = new
    
    @clientID.setter
    def clientID(self, new):
        self.__clientID = new
    
    @rentedDate.setter
    def rentedDate(self, new):
        self.__rentedDate = new
    
    @dueDate.setter
    def dueDate(self, new):
        self.__dueDate = new

    @returnedDate.setter
    def returnedDate(self, new):
        self.__returnedDate = new

    def __init__(self, movieID, clientID, rentedDate, dueDate, returnedDate):
        self.__rentalID = self.__generateID()
        self.__movieID = movieID
        self.__clientID = clientID
        self.__rentedDate = rentedDate
        self.__dueDate = dueDate
        self.__returnedDate = returnedDate
    
    def __eq__(self, that):
        return self.movieID == that.movieID and self.clientID == that.clientID and self.rentedDate == that.rentedDate and self.dueDate == that.dueDate and \
                self.returnedDate == that.returnedDate