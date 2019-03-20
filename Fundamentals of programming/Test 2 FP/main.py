from repositories.persons_repo import PersonRepo
from ui.ui import UI
from controllers.app_controller import AppController


repo = PersonRepo("persons.txt")
controller = AppController(repo)
ui = UI(controller)

ui.start()