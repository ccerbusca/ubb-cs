import random

from exception.GameException import GameOver


class Game:
    def __init__(self):
        self.starved = 0
        self.new_people = 0
        self.population = 100
        self.acres = 1000
        self.harvest_units = 3
        self.rats = 200
        self.land_price = 20
        self.grain = 2800
        self.toBuyOrSell = 0
        self.unitsToFeed = 0
        self.toPlant = 0
        self.game_over = False

    def updateLand(self):
        self.grain -= self.land_price * self.toBuyOrSell
        self.acres += self.toBuyOrSell
        self.land_price = random.randint(15, 25)

    def updatePopulation(self):
        self.grain -= self.unitsToFeed
        if self.unitsToFeed // 20 < self.population:
            self.starved = self.population - self.unitsToFeed // 20
            if self.starved >= self.population // 2:
                self.game_over = True
                raise GameOver("\nGAME OVER! Half your population starved!\n")
            self.population = self.unitsToFeed // 20
        if self.starved == 0:
            self.new_people = random.randint(0, 10)
            self.population += self.new_people

    def updateHarvest(self):
        self.grain -= self.toPlant
        self.harvest_units = random.randint(1, 6)
        self.grain += self.toPlant * self.harvest_units

    def ratInfestation(self):
        rand = random.choice([False, False, True, False, False])
        if rand:
            percent = random.randint(1, 10)
            toEat = percent / 100 * self.grain
            toEat = int(toEat // 10 * 10)
            self.rats = toEat
            self.grain -= toEat
        else:
            self.rats = 0

    def apply(self):
        self.updateLand()
        self.updatePopulation()
        self.updateHarvest()
        self.ratInfestation()







