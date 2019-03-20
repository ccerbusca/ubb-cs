from exception.GameException import GameException
from repo.game import Game


class GameController:
    def __init__(self):
        self.data = Game()

    def acresBuyOrSell(self, acres):
        if self.data.acres + acres < 0 or self.data.grain - self.data.land_price * acres < 0:
            if acres > 0:
                raise GameException("Not enough grain to buy that many acres")
            else:
                raise GameException("Can't sell more acres than you currently have")
        self.data.toBuyOrSell = acres

    def feedPopulation(self, units):
        if (self.data.grain - self.data.land_price * self.data.toBuyOrSell) - units < 0:
            raise GameException("You do not have this amount of grain")
        self.data.unitsToFeed = units

    def plant(self, acres):
        if (self.data.acres + self.data.toBuyOrSell) - acres < 0:
            raise GameException("You can't plant more acres than you have")
        if (self.data.grain - self.data.land_price * self.data.toBuyOrSell - self.data.unitsToFeed) - acres < 0:
            raise GameException("You can't plant grain you do not have")
        if acres > self.data.population * 10:
            raise GameException("Not enough people to plant that many acres")
        self.data.toPlant = acres

    def apply(self):
        self.data.apply()