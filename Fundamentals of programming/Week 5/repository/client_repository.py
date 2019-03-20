"""
    This module contains the repository for the clients
"""
import json
import pickle
from domain.client import Client
from domain.repo_iterator import repoIterator

class clientRepository(repoIterator):
    def __init__(self, settings):
        repoIterator.__init__(self)
        self.settings = settings
        try:
            if self.settings.repositoryType == "file":
                with open('storage/{}'.format(self.settings.clientsFile)) as file:
                    data = json.load(file)
                    for p in data['clients']:
                        self.data.append(Client(p['name']))
            elif self.settings.repositoryType == "binaryfile":
                with open('storage/{}'.format(self.settings.clientsFile), 'rb') as file:
                    self.data = pickle.load(file)
        except FileNotFoundError:
            pass

    def saveData(self):
        if self.settings.repositoryType == "file":
            data = {}
            data["clients"] = []
            for p in self:
                data["clients"].append({
                    "id": p.clientID,
                    "name": p.name
                })
            try:
                with open('storage/{}'.format(self.settings.clientsFile), 'x') as outfile:
                    json.dump(data, outfile)
            except FileExistsError:
                with open('storage/{}'.format(self.settings.clientsFile), 'w') as outfile:
                    json.dump(data, outfile)
        elif self.settings.repositoryType == "binaryfile":
            try:
                with open('storage/{}'.format(self.settings.clientsFile), 'xb') as outfile:
                    pickle.dump(self.data, outfile)
            except FileExistsError:
                with open('storage/{}'.format(self.settings.clientsFile), 'wb') as outfile:
                    pickle.dump(self.data, outfile)

    def add(self, client):
        self.data.append(client)
        self.saveData()
    
    def remove(self, removeID):
        for i in range(len(self)):
            if self[i].clientID == removeID:
                del self[i]
                break
        self.saveData()
    
    def update(self, updateID, name):
        for i in self:
            if i.clientID == updateID:
                i.name = name
        self.saveData()