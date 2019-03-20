"""
    This module contains the Rental Repository definition
"""
import json
import pickle
import datetime
from domain.rental import Rental
from domain.repo_iterator import repoIterator

class rentalRepository(repoIterator):
    def __init__(self, settings):
        repoIterator.__init__(self)
        self.settings = settings
        try:
            if self.settings.repositoryType == "file":
                with open('storage/{}'.format(self.settings.rentalsFile)) as file:
                    data = json.load(file)
                    for p in data['rentals']:
                        self.data.append(Rental(
                            int(p["movieID"]),
                            int(p["clientID"]),
                            datetime.datetime.strptime(p["rentedDate"], "%d/%m/%Y"),
                            datetime.datetime.strptime(p["dueDate"], "%d/%m/%Y"),
                            datetime.datetime.strptime(p["returnedDate"], "%d/%m/%Y") if p["returnedDate"] != "None" else None)
                        )
            elif self.settings.repositoryType == "binaryfile":
                with open('storage/{}'.format(self.settings.rentalsFile), 'rb') as file:
                    self.data = pickle.load(file)
        except FileNotFoundError:
            pass
    
    def saveData(self):
        if self.settings.repositoryType == "file":
            data = {}
            data["rentals"] = []
            for p in self:
                data["rentals"].append({
                    "id": p.rentalID,
                    "movieID": p.movieID,
                    "clientID": p.clientID,
                    "rentedDate": p.rentedDate.strftime("%d/%m/%Y"),
                    "dueDate": p.dueDate.strftime("%d/%m/%Y"),
                    "returnedDate": p.returnedDate.strftime("%d/%m/%Y") if p.returnedDate != None else "None"
                })
            try:
                with open('storage/{}'.format(self.settings.rentalsFile), 'x') as outfile:
                    json.dump(data, outfile)
            except FileExistsError:
                with open('storage/{}'.format(self.settings.rentalsFile), 'w') as outfile:
                    json.dump(data, outfile)
        elif self.settings.repositoryType == "binaryfile":
            try:
                with open('storage/{}'.format(self.settings.rentalsFile), 'xb') as outfile:
                    pickle.dump(self.data, outfile)
            except FileExistsError:
                with open('storage/{}'.format(self.settings.rentalsFile), 'wb') as outfile:
                    pickle.dump(self.data, outfile)

    def rentMovie(self, rental):
        self.data.append(rental)
        self.saveData()
    
    def remove(self, removeID):
        for i in range(len(self)):
            if self[i].rentalID == removeID:
                del self[i]
                break
        self.saveData()

    def returnMovie(self, movieID, time):
        ok = False
        for i in self:
            if i.movieID == movieID and i.returnedDate == None:
                i.returnedDate = time
                ok = True
        if not ok:
            raise ValueError("Movie not rented")
        self.saveData()
