import json
import random
from domain.settings import Settings
from controller.controller import Controller
from repository.movie_repository import movieRepository
from repository.client_repository import clientRepository
from repository.rental_repository import rentalRepository
from domain.client import Client
from domain.movie import Movie
from domain.rental import Rental
from datetime import datetime
import datetime
from ui.ui import UI
import os


""" def initializeRentals(controller):
    now = datetime.datetime.now()
    for i in range(1, 101):
        movieId = random.choice(range(1, 101))
        while controller.movieIsRented(movieId):
            movieId = random.choice(range(1, 101))
        
        clientId = random.choice(range(1, 101))
        for i in controller.rentals.data:
            if i.clientID == clientId and i.dueDate < now and i.returnedDate == None:
                clientId = random.choice(range(1, 101))
            else:
                break
        year = random.choice(range(2015, 2019))
        month = random.choice(range(1, 13))
        day = random.choice(range(1, 29))
        rentDate = datetime.datetime(year=year, month=month, day=day)
        dueDate = rentDate + datetime.timedelta(days=random.choice(range(1, 15)))    
        returnedDate = random.choice([None, dueDate, dueDate + datetime.timedelta(days=random.choice(range(1, 15)))])
        rental = Rental(movieId, clientId, rentDate, dueDate, returnedDate)
        controller.rentMovie(rental) """

settings = Settings("settings.properties")
clientRepo = clientRepository(settings)
movieRepo = movieRepository(settings)
rentalRepo = rentalRepository(settings)
controller = Controller(movieRepo, clientRepo, rentalRepo)

ui = UI(controller)
ui.mainMenu()