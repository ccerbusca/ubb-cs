from exception.GameException import GameException, GameOver


class UI:
    def __init__(self, controller):
        self.controller = controller

    def start(self):
        i = 1
        while i < 6:
            print()
            print("In year {}, {} people starved.".format(i, self.controller.data.starved))
            print("{} people came to the city.".format(self.controller.data.new_people))
            print("City population is {}.".format(self.controller.data.population))
            print("City owns {} acres of land.".format(self.controller.data.acres))
            print("Harvest was {} units per acre.".format(self.controller.data.harvest_units))
            print("Rats ate {} units.".format(self.controller.data.rats))
            print("Land price is {} units per acre.".format(self.controller.data.land_price))
            print("\nGrain stocks are {} units.\n".format(self.controller.data.grain))
            try:
                self.getFirstInput()
                self.getSecondInput()
                self.getThirdInput()
                self.controller.apply()
            except GameOver as e:
                print(e)
                return
            i += 1
        if not self.controller.data.game_over:
            if self.controller.data.population > 100 and self.controller.data.acres > 1000:
                print("\nCongratulations! You WON the game!")
            else:
                print("\nGAME OVER. You did not do well.")

    def getFirstInput(self):
        try:
            acres = int(input("Acres to buy/sell(+/-) -> "))
            self.controller.acresBuyOrSell(int(acres))
        except ValueError:
            print("You must input a number")
            self.getFirstInput()
        except GameException as e:
            print(e)
            self.getFirstInput()

    def getSecondInput(self):
        try:
            feed_pop = int(input("Units to feed the population -> "))
            self.controller.feedPopulation(int(feed_pop))
        except ValueError:
            print("You must input a number")
            self.getSecondInput()
        except GameException as e:
            print(e)
            self.getSecondInput()

    def getThirdInput(self):
        try:
            plant = int(input("Acres to plant -> "))
            self.controller.plant(int(plant))
        except ValueError:
            print("You must input a number")
            self.getThirdInput()
        except GameException as e:
            print(e)
            self.getThirdInput()
