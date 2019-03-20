"""
This module contains the movie class definition
"""

class Movie:
    __id = 0
    def __generateID(self):
        Movie.__id += 1
        return Movie.__id

    @property
    def movieID(self):
        return self.__movieID
    
    @property
    def title(self):
        return self.__title
    
    @property
    def genre(self):
        return self.__genre
    
    @property
    def description(self):
        return self.__description
    
    @movieID.setter
    def movieID(self, new):
        self.__movieID = new

    @title.setter
    def title(self, new):
        self.__title = new
    
    @genre.setter
    def genre(self, new):
        self.__genre = new
    
    @description.setter
    def description(self, new):
        self.__description = new

    def __init__(self, title, description, genre):
        self.__movieID = self.__generateID()
        self.__title = title
        self.__description = description
        self.__genre = genre
    
    def __str__(self):
        return "{}. {}\n\tGenre: {}\n\tDescription: {}".format(self.__movieID, self.__title, self.__genre, self.__description)
    
    def __eq__(self, movie2):
        return self.__title == movie2.title and self.__genre == movie2.genre and self.__description == movie2.description