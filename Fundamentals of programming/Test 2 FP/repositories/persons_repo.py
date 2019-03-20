from models.person import Person

class PersonRepo:
    def __init__(self, fname):
        self.data = []
        with open(fname, "r") as rfile:
            for i in rfile:
                fields = i.strip().split(",")
                self.data.append(Person(int(fields[0].strip()), fields[1].strip(), fields[2].strip()))
    
    def vaccinate(self, ID):
        for i in self.data:
            if i.id == ID:
                i.immunization = "vaccinated"
    
    def infect(self, ID):
        for i in self.data:
            if i.id == ID:
                i.status = "ill"
                i.days = 0