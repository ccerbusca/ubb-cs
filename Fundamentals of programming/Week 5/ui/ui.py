"""
    This module contains the UI functions
"""

from domain.movie import *
from domain.client import *
from domain.rental import *
from controller.undo_controller import *
from domain.repo_iterator import shellsort
import os
import datetime

class UI:
    def __init__(self, controller):
        self.__controller = controller
        self.__undoController = UndoController()
    
    @staticmethod
    def clear():
        print("\n" * 2)

    @staticmethod
    def printOptions():
        UI.clear()
        print("1. Add")
        print("2. Remove")
        print("3. Update")
        print("4. List")

    @staticmethod
    def printMenu():
        UI.clear()
        print("1. Movie")
        print("2. Clients")
        print("3. Rent a movie")
        print("4. Return a movie")
        print("5. Search")
        print("6. Statistics")
        print("7. Undo")
        print("8. Redo")
        print("9. Exit")
        print("10. Run Tests")

    def mainMenu(self):
        while True:
            try:
                UI.printMenu()
                menu = int(input())
                if menu in (1, 2):
                    UI.printOptions()
                    option = int(input())
                    if menu == 1:
                        if option == 1:
                            movie = UI.readMovie()
                            self.__undoController.add(Operation(FunctionCall(self.__controller.removeMovie, movie.movieID),
                                                                FunctionCall(self.__controller.addMovie, movie)))
                            self.__controller.addMovie(movie)
                        elif option == 2:
                            removeID = UI.readID("Introduce the ID of the movie you want to remove\n")
                            cascadeOp = CascadeOperation()
                            cascadeOp.add(Operation(FunctionCall(self.__controller.addMovie, self.__controller.getMovieByID(removeID)),
                                                    FunctionCall(self.__controller.removeMovie, removeID)))
                            for i in [k for k in self.__controller.rentals if k.movieID == removeID]:
                                cascadeOp.add(Operation(FunctionCall(self.__controller.rentMovie, i),
                                                        FunctionCall(self.__controller.removeRental, i.rentalID)))
                                self.__controller.removeRental(i.rentalID)
                            self.__undoController.add(cascadeOp)
                            self.__controller.removeMovie(removeID)

                        elif option == 3:
                            self.updateMovieUI()
                        elif option == 4:
                            #self.__controller.movies.sort(key=lambda x:x.movieID)
                            shellsort(self.__controller.movies, lambda x, y: x.movieID > y.movieID)
                            UI.printList(self.__controller.movies)
                    elif menu == 2:
                        if option == 1:
                            name = input("Introduce the client's name\n")
                            client = Client(name)
                            self.__undoController.add(Operation(FunctionCall(self.__controller.removeClient, client.clientID),
                                                                FunctionCall(self.__controller.addClient, client)))
                            self.__controller.addClient(client)
                        elif option == 2:
                            removeID = UI.readID("Introduce the ID of the client you want to remove\n")
                            cascadeOp = CascadeOperation()
                            cascadeOp.add(Operation(FunctionCall(self.__controller.addClient, self.__controller.getClientByID(removeID)),
                                                    FunctionCall(self.__controller.removeClient, removeID)))
                            for i in [k for k in self.__controller.rentals if k.clientID == removeID]:
                                cascadeOp.add(Operation(FunctionCall(self.__controller.rentMovie, i),
                                                        FunctionCall(self.__controller.removeRental, i.rentalID)))
                                self.__controller.removeRental(i.rentalID)
                            self.__undoController.add(cascadeOp)
                            self.__controller.removeClient(removeID)
                        elif option == 3:
                            self.updateClientUI()
                        elif option == 4:
                            #self.__controller.clients.sort(key=lambda x:x.clientID)
                            shellsort(self.__controller.clients, lambda x, y: x.clientID > y.clientID)
                            UI.printList(self.__controller.clients)
                elif menu == 3:
                    rental = self.readRental(self.__controller.movies)
                    if self.__controller.movieIsRented(rental.movieID):
                        raise ValueError("Movie not available")
                    now = datetime.datetime.now()
                    for i in self.__controller.rentals:
                        if i.clientID == rental.clientID and i.dueDate < now and i.returnedDate == None:
                            raise ValueError("The client cannot rent any movie, because he has not returned a movie with an expired due date")
                    self.__undoController.add(Operation(FunctionCall(self.__controller.removeRental, rental.rentalID),
                                                        FunctionCall(self.__controller.rentMovie, rental)))
                    self.__controller.rentMovie(rental)
                elif menu == 4:
                    movieID = int(input("Specify the movie's ID:\n"))
                    if not self.__controller.movieIsRented(movieID):
                        raise ValueError("This movie is not rented")
                    rental = [i for i in self.__controller.rentals if i.movieID == movieID].pop()
                    now = datetime.datetime.now()
                    cascadeOp = CascadeOperation()
                    cascadeOp.add(Operation(FunctionCall(rental.setReturnedDate, None),
                                            FunctionCall(rental.setReturnedDate, now)))
                    cascadeOp.add(Operation(FunctionCall(self.__controller.rentals.saveData),
                                            FunctionCall(self.__controller.rentals.saveData)))
                    self.__undoController.add(cascadeOp)
                    self.__controller.returnMovie(movieID, now)
                elif menu == 5:
                    self.searchUI()
                elif menu == 6:
                    self.statisticsUI()
                elif menu == 7:
                    self.__undoController.undo()
                elif menu == 8:
                    self.__undoController.redo()
                elif menu == 9:
                    return
                elif menu == 10:
                    import unittest
                    try:
                        unittest.main()
                    except SystemExit:
                        print("All tests passed")
                else:
                    raise ValueError("Wrong option")
            except ValueError as e:
                print(e)
    
    def statisticsUI(self):
        print("1. Most rented movies")
        print("2. Most active clients")
        print("3. All rentals")
        print("4. Late rentals")
        option = int(input())
        if option == 1:
            for i in self.__controller.mostRentedMovie():
                print("{} {}".format(i[0].title, i[1]))
        elif option == 2:
            for i in self.__controller.mostActiveClient():
                print("{} {}".format(i[0], i[1]))
        elif option == 3:
            for i in self.__controller.allRentals():
                print("{}. \"{}\":\n\tRented by {}\n\tFrom {} to {}. Return Date: {}".format(i.rentalID, self.__controller.getMovieByID(i.movieID).title,
                                    self.__controller.getClientByID(i.clientID).name, i.rentedDate.date(), i.dueDate.date(),
                                    i.returnedDate.date() if i.returnedDate != None else None))
        elif option == 4:
            for i in self.__controller.lateRentals():
                print("{}. \"{}\":\n\tRented by {}\n\tFrom {} to {}. Return Date: {}".format(i.rentalID, self.__controller.getMovieByID(i.movieID).title,
                                    self.__controller.getClientByID(i.clientID).name, i.rentedDate.date(), i.dueDate.date(),
                                    i.returnedDate.date() if i.returnedDate != None else None))
        else:
            raise ValueError("Invalid option")

    @staticmethod
    def printSearchClient():
        UI.clear()
        s = "Specify the field you want to search by:\n" + "1. ID\n" + "2. Name\n"
        print(s)

    @staticmethod
    def printSearchMovie():
        UI.clear()
        s = "Specify the field you want to search by:\n" + "1. ID\n" + "2. Title\n" + "3. Description\n" + "4. Genre\n"
        print(s)
    
    def searchUI(self):
        option = int(input("1. Clients\n" + "2.     Movies\n"))
        if option == 1:
            UI.printSearchClient()
            choice = int(input())
            if choice == 1:
                searchID = int(input("Input the ID you want to search:\n"))
                search = self.__controller.searchClientByID(searchID)
                if len(search) == 0:
                    raise ValueError("No client with such ID")
                print(search[0])
            elif choice == 2:
                searchName = input("Enter the client's name:\n").lower()
                search = self.__controller.searchClientByName(searchName)
                if len(search) == 0:
                    raise ValueError("No clients with such name")
                UI.printList(search)
            else:
                raise ValueError("Invalid option")
        elif option == 2:
            UI.printSearchMovie()
            choice = int(input())
            if choice == 1:
                searchID = int(input("Input the ID you want to search:\n"))
                search = self.__controller.searchMovieById(searchID)
                if len(search) == 0:
                    raise ValueError("No movie with such ID")
                print(search[0])
            elif choice == 2:
                searchTitle = input("Enter the movie's title:\n").lower()
                search = self.__controller.searchMovieByTitle(searchTitle)
                if len(search) == 0:
                    raise ValueError("No movies with such title")
                UI.printList(search)
            elif choice == 3:
                searhDesc = input("Enter the movie's description:\n").lower()
                search = self.__controller.searchMovieByDescription(searhDesc)
                if len(search) == 0:
                    raise ValueError("No movies with such title")
                UI.printList(search)
            elif choice == 4:
                searchGenre = input("Enter the movie's genre:\n").lower()
                search = self.__controller.searchMovieByGenre(searchGenre)
                if len(search) == 0:
                    raise ValueError("No movies with such title")
                UI.printList(search)
            else:
                raise ValueError("Invalid option")
        else:
            raise ValueError("Invalid option")

    @staticmethod
    def readMovie():
        try:
            UI.clear()
            title = input("Introduce the movie's name\n")
            description = input("Introduce the movie's description\n")
            genre = input("Introduce the movie's genre\n")
            return Movie(title, description, genre)
        except ValueError:
            print("Wrong parameters")
            return UI.readMovie()

    @staticmethod
    def readID(s):
        try:
            readID = int(input(s))
            return readID
        except ValueError:
            print("Wrong parameters")
            return UI.readID(s)
    
    @staticmethod
    def printList(L):
        for i in L:
            print(i)

    def updateMovieUI(self):
        try:
            updateID = int(input("Introduce the ID of the movie you want to update:\n"))
            if updateID not in [i.movieID for i in self.__controller.movies]:
                raise ValueError()
            print("1. Update Title")
            print("2. Update Genre")
            print("3. Update Description")
            choice = int(input())
            if choice == 1:
                newTitle = input("Introduce the new movie title:\n")
                self.__undoController.add(Operation(FunctionCall(self.__controller.updateMovieTitle, updateID, self.__controller.getMovieByID(updateID).title),
                                                    FunctionCall(self.__controller.updateMovieTitle, updateID, newTitle)))
                self.__controller.updateMovieTitle(updateID, newTitle)
            elif choice == 2:
                newGenre = input("Introduce the new movie genre:\n")
                self.__undoController.add(Operation(FunctionCall(self.__controller.updateMovieGenre, updateID, self.__controller.getMovieByID(updateID).genre),
                                                    FunctionCall(self.__controller.updateMovieGenre, updateID, newGenre)))
                self.__controller.updateMovieGenre(updateID, newGenre)
            elif choice == 3:
                newDesc = input("Introduce the new movie description:\n")
                self.__undoController.add(Operation(FunctionCall(self.__controller.updateMovieDescription, updateID, self.__controller.getMovieByID(updateID).description),
                                                    FunctionCall(self.__controller.updateMovieDescription, updateID, newDesc)))
                self.__controller.updateMovieDescription(updateID, newDesc)
            else:
                raise ValueError()
        except ValueError:
            print("Wrong parameters")
            self.updateMovieUI()

    def updateClientUI(self):
        try:
            updateID = int(input("Introduce the ID of the client you want to update:\n"))
            newName = input("Introduce the new name you'd like to set:\n")
            self.__undoController.add(Operation(FunctionCall(self.__controller.updateClient, updateID, self.__controller.getClientByID(updateID).name),
                                                FunctionCall(self.__controller.updateClient, updateID, newName)))
            self.__controller.updateClient(updateID, newName)
        except ValueError:
            print("Wrong parameters")
            self.updateClientUI()
    
    def readRental(self, movies):
        try:
            clientID = int(input("Specify the id of the client who is renting:\n"))
            print("Specify the id of the movie to be rented from the list below:\n")
            for i in movies:
                if not self.__controller.movieIsRented(i.movieID):
                    print("{}. {}".format(i.movieID, i.title))
            movieID = int(input())
            dueDateStr = input("Specify the due date in the following format: dd/mm/yyyy\n")
            now = datetime.datetime.now()
            dueDate = datetime.datetime.strptime(dueDateStr, "%d/%m/%Y")
            return Rental(movieID, clientID, now, dueDate, None)
        except ValueError as e:
            print(e)
            return self.readRental(movies)