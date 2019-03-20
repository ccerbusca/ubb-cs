import unittest
import os
import json
import pickle
from datetime import datetime
from domain.movie import Movie
from domain.client import Client
from domain.rental import Rental
from controller.controller import *
from repository.movie_repository import movieRepository
from repository.client_repository import clientRepository
from repository.rental_repository import rentalRepository
from domain.settings import Settings
from domain.repo_iterator import myFilter, shellsort

class TestSortAndFilter(unittest.TestCase):
    def setUp(self):
        self.list = [85, 98, 28, 8, 13, 72, 67, 3]
    
    def tearDown(self):
        del self.list
    
    def test_shellsort(self):
        self.assertEquals([3, 8, 13, 28, 67, 72, 85, 98], shellsort(self.list, lambda x, y: x > y), "The sorting function did not rearrange the list in ascending order")
    
    def test_myFilter(self):
        self.assertEquals(shellsort([28, 8, 13, 3], lambda x, y: x > y),
                          shellsort(myFilter(self.list, lambda x: x < 50), lambda x, y: x > y),
                          "The function did not filter all the elements lesser than 50")

class TestController(unittest.TestCase):    
    def setUp(self):
        self.settings = Settings("test.properties")
        self.controller = Controller(movieRepository(self.settings), clientRepository(self.settings), rentalRepository(self.settings))

    def tearDown(self):
        del self.controller
        Movie._Movie__id = 0
        Client._Client__id = 0
        Rental._Rental__id = 0
        if os.path.isfile("storage/{}".format(self.settings.moviesFile)):
            os.remove("storage/{}".format(self.settings.moviesFile))
        if os.path.isfile("storage/{}".format(self.settings.clientsFile)):
            os.remove("storage/{}".format(self.settings.clientsFile))
        if os.path.isfile("storage/{}".format(self.settings.rentalsFile)):
            os.remove("storage/{}".format(self.settings.rentalsFile))
    def test_addMovie(self):
        self.controller.addMovie(Movie("The Mentalist", "Serious Crimes getting solved", "Crime"))
        self.assertEquals(self.controller.movies.data[0], Movie("The Mentalist", "Serious Crimes getting solved", "Crime"), "Movies not equal")
        if self.settings.repositoryType.lower() == "file":
            with open("storage/{}".format(self.settings.moviesFile)) as file:
                data = json.load(file)
                self.assertEqual(Movie(data["movies"][0]["name"], data["movies"][0]["description"], data["movies"][0]["genre"]),
                                Movie("The Mentalist", "Serious Crimes getting solved", "Crime"), "Movies not equal")
        elif self.settings.repositoryType.lower() == "binaryfile":
            with open("storage/{}".format(self.settings.moviesFile), "rb") as file:
                data = pickle.load(file)
                self.assertEquals(data[0], Movie("The Mentalist", "Serious Crimes getting solved", "Crime"), "Movies not equal")
    
    def test_addClient(self):
        self.controller.addClient(Client("Cristian Cerbusca"))
        self.assertEquals(self.controller.clients.data[0], Client("Cristian Cerbusca"), "Clients not equal")
        if self.settings.repositoryType.lower() == "file":
            with open("storage/{}".format(self.settings.clientsFile)) as file:
                data = json.load(file)
                self.assertEqual(Client(data["clients"][0]["name"]),
                                Client("Cristian Cerbusca"), "Clients not equal")
        elif self.settings.repositoryType.lower() == "binaryfile":
            with open("storage/{}".format(self.settings.clientsFile), "rb") as file:
                data = pickle.load(file)
                self.assertEquals(data[0], Client("Cristian Cerbusca"), "Clients not equal")
    
    def test_removeMovie(self):
        self.controller.addMovie(Movie("1", "2", "3"))
        self.controller.removeMovie(self.controller.movies.data[0].movieID)
        self.assertEqual(self.controller.movies.data, [], "List not empty after movie removal")
    
    def test_removeClient(self):
        self.controller.addClient(Client("Cristian Cerbusca"))
        self.controller.removeClient(self.controller.clients.data[0].clientID)
        self.assertEqual(self.controller.clients.data, [], "List not empty after client removal")

    def test_updateMovie(self):
        self.controller.addMovie(Movie("1", "2", "3"))
        self.controller.updateMovieTitle(1, "The Mentalist")
        self.controller.updateMovieDescription(1, "Serious Crimes getting solved")
        self.controller.updateMovieGenre(1, "Crime")
        self.assertEqual(self.controller.movies.data[0].title, "The Mentalist", "Title not updated")
        self.assertEqual(self.controller.movies.data[0].description, "Serious Crimes getting solved", "Description not updated")
        self.assertEqual(self.controller.movies.data[0].genre, "Crime", "Genre not updated")
    
    def test_updateClient(self):
        self.controller.addClient(Client("Cristian Cerbusca"))
        self.controller.updateClient(1, "Andrei Pop")
        self.assertEqual(self.controller.clients.data[0].name, "Andrei Pop", "Client name not updated")
    
    def test_rentMovie(self):
        self.controller.addMovie(Movie("1", "2", "3"))
        self.controller.addClient(Client("Cristian Cerbusca"))
        self.controller.rentMovie(Rental(1, 1, datetime.datetime.strptime("11/11/2018", "%d/%m/%Y"), datetime.datetime.strptime("13/11/2018", "%d/%m/%Y"), None))
        self.assertEqual(self.controller.rentals.data[0], Rental(1, 1, datetime.datetime.strptime("11/11/2018", "%d/%m/%Y"),
                        datetime.datetime.strptime("13/11/2018", "%d/%m/%Y"), None), "Rentals not equal")

    def test_returnMovie(self):
        self.controller.addMovie(Movie("1", "2", "3"))
        self.controller.addClient(Client("Cristian Cerbusca"))
        self.controller.rentMovie(Rental(1, 1, datetime.datetime.strptime("11/11/2018", "%d/%m/%Y"), datetime.datetime.strptime("13/11/2018", "%d/%m/%Y"), None))
        self.controller.returnMovie(1, datetime.datetime.strptime("13/11/2018", "%d/%m/%Y"))
        self.assertEquals(self.controller.rentals.data[0].returnedDate, datetime.datetime.strptime("13/11/2018", "%d/%m/%Y"), "Returned date not correct")

if __name__ == "__main__":
    unittest.main()