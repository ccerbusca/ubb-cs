import unittest
from repositories.persons_repo import PersonRepo
from ui.ui import UI
from controllers.app_controller import AppController

class myTest(unittest.TestCase):
    def setUp(self):
        repo = PersonRepo("persons.txt")
        self.controller = AppController(repo)
    
    def tearDown(self):
        del self.controller
    
    def test_simulateDay_personGetsInfected(self):
        self.controller.simulateDay()
        count = len([i for i in self.controller.repo.data if i.status == "ill"])
        self.assertEqual(count, 6, "The method did not infect random persons")

    def test_simulateDay_personGetsCuredAfter3Days(self):
        try:
            self.controller.simulateDay()
            self.controller.simulateDay()
            self.controller.simulateDay()
            person = [i for i in self.controller.repo.data if i.id == 1][0]
            self.assertEqual(person.status, "healthy", "The repeated call of the method did not heal the initial ill person")
        except ValueError as e:
            pass

    def test_vaccinate(self):
        self.controller.vaccinate(2)
        person = [i for i in self.controller.repo.data if i.id == 2][0]
        self.assertEqual(person.immunization, "vaccinated", "The method did not change the immunization of the person")
    
unittest.main()