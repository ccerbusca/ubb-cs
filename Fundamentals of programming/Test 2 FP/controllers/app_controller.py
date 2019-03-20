import random

class AppController:
    def __init__(self, repo):
        self.repo = repo
    
    def simulateDay(self):
        """
            The method simulates the passing of a day. It increments the number of days passed since getting ill for the infected persons,
            and infects a random healthy, nonvaccinated person
        """
        for i in self.repo.data:
            if i.status == "ill":
                i.days += 1
                if i.days >= 3:
                    i.status = "healthy"
        count = len([i for i in self.repo.data if i.status == "ill"])
        for i in range(count):
            l = [i for i in self.repo.data if i.status == "healthy" and i.immunization == "nonvaccinated" and i.days < 3]
            if len(l) == 0:
                raise ValueError("Cannot infect anyone else")
            p = random.choice(l)
            self.repo.infect(p.id)
    

    def vaccinate(self, ID):
        """
        The method simulates the vaccination of a healthy person
        """
        person = [i for i in self.repo.data if i.id == ID][0]
        if person.status == "healthy":
            self.repo.vaccinate(ID)
        else:
            raise ValueError("Cannot vaccinate a ill person")
    
