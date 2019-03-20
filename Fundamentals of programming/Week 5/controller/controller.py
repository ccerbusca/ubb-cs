"""
    This module contains the controller of the application that deals with the operations on the repositories
"""

from domain.repo_iterator import shellsort, myFilter
import datetime
class Controller:
    def __init__(self, movies, clients, rentals):
        self.__movies = movies
        self.__clients = clients
        self.__rentals = rentals
    
    @property
    def movies(self):
        return self.__movies
    
    @property
    def clients(self):
        return self.__clients
    
    @property
    def rentals(self):
        return self.__rentals

    def addMovie(self, movie):
        '''Add a movie to the repository'''
        if 0 not in (len(movie.title), len(movie.description), len(movie.genre)):
            self.__movies.add(movie)
        else:
            raise ValueError("You can't input empty parameters")

    def removeMovie(self, removeID):
        '''Remove movie specified by its ID'''
        self.__movies.remove(removeID)
    
    def updateMovieTitle(self, updateID, title):
        '''Update the title of the movie specified by it's ID'''
        self.__movies.updateTitle(updateID, title)
    
    def updateMovieDescription(self, updateID, description):
        '''Update the description of the movie specified by it's ID'''
        self.__movies.updateDescription(updateID, description)
    
    def updateMovieGenre(self, updateID, genre):
        '''Update the genre of the movie specified by it's ID'''
        self.__movies.updateGenre(updateID, genre)

    def addClient(self, client):
        '''Adds a client object to the list'''
        self.__clients.add(client)
    
    def removeClient(self, removeID):
        '''Remove a client specified by his ID'''
        self.__clients.remove(removeID)
    
    def updateClient(self, updateID, name):
        '''Update a client's name, specified by his ID'''
        self.__clients.update(updateID, name)
    
    def rentMovie(self, rental):
        '''This function checks if a rental is valid and adds it to the list'''
        self.__rentals.rentMovie(rental)
    
    def returnMovie(self, movieID, time):
        '''Returns a movie from a rental'''
        self.__rentals.returnMovie(movieID, time)
    
    def searchClientByID(self, searchID):
        '''Search a client by his ID'''
        #return [i for i in self.clients if i.clientID == searchID]
        return myFilter(self.clients, lambda x: x.clientID == searchID)
    
    def searchClientByName(self, name):
        '''Search a client by name'''
        #return [i for i in self.clients if name in i.name.lower()]
        return myFilter(self.clients, lambda x: name in x.name.lower())
    
    def searchMovieById(self, searchID):
        '''Search a movie by ID'''
        #return [i for i in self.movies if i.movieID == searchID]
        return myFilter(self.movies, lambda x: x.movieID == searchID)
    
    def searchMovieByTitle(self, title):
        '''Search movie by title'''
        #return [i for i in self.movies if title in i.title.lower()]
        return myFilter(self.movies, lambda x: title in x.title.lower())
    
    def searchMovieByDescription(self, description):
        '''Search movie by description'''
        #return [i for i in self.movies if description in i.description.lower()]
        return myFilter(self.movies, lambda x: description in x.description.lower())
    
    def searchMovieByGenre(self, genre):
        '''Search a movie by genre'''
        #return [i for i in self.movies if genre in i.genre.lower()]
        return myFilter(self.movies, lambda x: genre in x.genre.lower())
    
    def getMovieByID(self, ID):
        '''Return the movie object identified by the specified ID'''
        for i in self.movies:
            if i.movieID == ID:
                return i    

    def getClientByID(self, ID):
        '''Return the client object, identified by the specified ID'''
        for i in self.clients:
            if i.clientID == ID:
                return i

    def mostRentedMovie(self):
        '''Returns a list of movies sorted by how many times it was rented'''
        mostRented = {}
        for i in shellsort(self.rentals, lambda x, y:x.rentalID > y.rentalID):
            if i.movieID in mostRented.keys():
                mostRented[i.movieID] += 1
            else:
                mostRented[i.movieID] = 1
        mostRented = [(i, mostRented[i]) for i in mostRented.keys()]
        shellsort(mostRented, lambda x, y: x[1] > y[1])
        mostRented = [(self.getMovieByID(i[0]), i[1]) for i in mostRented]
        return mostRented

    def mostActiveClient(self):
        '''Returns the list of clients sorted by the number of rented days'''
        mostActive = {}
        for i in shellsort(self.rentals, lambda x, y:x.rentalID > y.rentalID):
            if i.clientID in mostActive.keys():
                mostActive[i.clientID] += (i.returnedDate - i.rentedDate).days if i.returnedDate != None else (datetime.datetime.now() - i.rentedDate).days
            else:
                mostActive[i.clientID] = (i.returnedDate - i.rentedDate).days if i.returnedDate != None else (datetime.datetime.now() - i.rentedDate).days
        mostActive = [(self.getClientByID(i), mostActive[i]) for i in mostActive.keys()]
        shellsort(mostActive, lambda x, y: x[1] > y[1])
        return mostActive
    
    def allRentals(self):
        '''Return the list of all the movies currently rented'''
        return [i for i in shellsort(self.rentals, lambda x, y:x.rentalID > y.rentalID)]
    
    def lateRentals(self):
        '''Returns the list of all movies, whose due date has passed'''
        return [i for i in shellsort(self.rentals, lambda x, y:x.rentalID > y.rentalID) if datetime.datetime.now() > i.dueDate and i.returnedDate == None]
    
    def removeRental(self, removeID):
        '''Remove the rental specified by the removeID'''
        self.rentals.remove(removeID)
    
    def movieIsRented(self, movieID):
        '''Check whether a movie is rented or not'''
        for i in self.rentals:
            if i.movieID == movieID and i.returnedDate == None:
                return True
        return False