"""
    This module contains the Movie Repository definition
"""
import json
import pickle
from domain.movie import Movie
from domain.repo_iterator import repoIterator

class movieRepository(repoIterator):
    def __init__(self, settings):
        repoIterator.__init__(self)
        self.settings = settings
        try:
            if self.settings.repositoryType == "file":
                with open('storage/{}'.format(self.settings.moviesFile)) as file:
                    data = json.load(file)
                    for p in data['movies']:
                        self.data.append(Movie(p["name"], p["description"], p["genre"]))
            elif self.settings.repositoryType == "binaryfile":
                with open('storage/{}'.format(self.settings.moviesFile), 'rb') as file:
                    self.data = pickle.load(file)
        except FileNotFoundError:
            pass

    def saveData(self):
        if self.settings.repositoryType == "file":
            data = {}
            data["movies"] = []
            for p in self:
                data["movies"].append({
                    "id": p.movieID,
                    "name": p.title,
                    "genre": p.genre,
                    "description": p.description
                })
            try:
                with open('storage/{}'.format(self.settings.moviesFile), 'x') as outfile:
                    json.dump(data, outfile)
            except FileExistsError:
                with open('storage/{}'.format(self.settings.moviesFile), 'w') as outfile:
                    json.dump(data, outfile)
        elif self.settings.repositoryType == "binaryfile":
            try:
                with open('storage/{}'.format(self.settings.moviesFile), 'xb') as outfile:
                    pickle.dump(self.data, outfile)
            except FileExistsError:
                with open('storage/{}'.format(self.settings.moviesFile), 'wb') as outfile:
                    pickle.dump(self.data, outfile)
                

    def add(self, movie):
        self.data.append(movie)
        self.saveData()
    
    def remove(self, removeID):
        for i in range(len(self)):
            if self[i].movieID == removeID:
                del self[i]
                break
        self.saveData()
    
    def updateTitle(self, updateID, title):
        for i in range(len(self)):
            if self[i].movieID == updateID:
                self[i].title = title
        self.saveData()
    
    def updateDescription(self, updateID, description):
        for i in range(len(self)):
            if self[i].movieID == updateID:
                self[i].description = description
        self.saveData()
    
    def updateGenre(self, updateID, genre):
        for i in range(len(self)):
            if self[i].movieID == updateID:
                self[i].genre = genre
        self.saveData()