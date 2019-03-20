from unittest import TestCase

from controller.GameController import GameController
from exception.GameException import GameException


class TestGameController(TestCase):
    def setUp(self):
        self.controller = GameController()

    def tearDown(self):
        del self.controller

    def test_inputValidation_acresBuyOrSell(self):
        try:
            self.controller.acresBuyOrSell(200)
            self.fail("You shouldn't be able to buy more land than you have grain for")
        except GameException:
            self.assertEqual(True, True)

        try:
            self.controller.data.acres = 1
            self.controller.acresBuyOrSell(-100)
            self.fail("You shouldn't be able to sell more land than you have")
        except GameException:
            self.assertEqual(True, True)

    def test_inputValidation_feedPopulation(self):
        try:
            self.controller.feedPopulation(2801)
            self.fail("You can't feed people with grain you do not have")
        except GameException:
            self.assertEqual(True, True)

    def test_inputValidation_plant(self):
        try:
            self.controller.plant(1001)
            self.fail("You can't plant more acres than you have")
        except GameException:
            self.assertEqual(True, True)
        try:
            self.controller.data.grain = 2
            self.controller.plant(3)
            self.fail("You can't plant grain you do not have")
        except GameException:
            self.assertEqual(True, True)
        try:
            self.controller.data.grain = 2800
            self.controller.data.acres = 2000
            self.controller.data.population = 1
            self.controller.plant(100)
            self.fail("Not enough people to plant that many acres")
        except GameException:
            self.assertEqual(True, True)

    def test_updateLand(self):
        self.controller.acresBuyOrSell(100)
        self.controller.data.updateLand()
        self.assertEqual(self.controller.data.grain, 800, "Grain stock should not change")
        self.assertEqual(self.controller.data.acres, 1100, "Acres amount should not change")
        self.controller.acresBuyOrSell(0)
        self.controller.data.updateLand()
        self.assertEqual(self.controller.data.grain, 800, "Grain stock should not change")
        self.assertEqual(self.controller.data.acres, 1100, "Acres amount should not change")

    def test_updatePopulation(self):
        self.controller.feedPopulation(1999)
        self.controller.data.updatePopulation()
        self.assertEqual(self.controller.data.grain, 801, "Grain used to feed the population should be subtracted from the stock")
        self.assertEqual(self.controller.data.starved, 1, "A person should have starved")
        self.assertEqual(self.controller.data.population, 99, "The population should have been decreased")
        self.assertEqual(self.controller.data.new_people, 0, "No new people should have come to the city")

    def test_updateHarvest(self):
        self.controller.plant(800)
        self.controller.data.updateHarvest()
        self.assertEqual(self.controller.data.grain, 2000 + 800 * self.controller.data.harvest_units, "The grain stock should have been updated")

    def test_ratInfestation(self):
        self.controller.data.rats = 0
        self.controller.data.ratInfestation()
        self.assertEqual(self.controller.data.grain, 2800 - self.controller.data.rats, "Rats should have eaten a part of the grain stock (if the infestation took place)")
