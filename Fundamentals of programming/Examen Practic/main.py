from controller.GameController import GameController
from ui.ui import UI

controller = GameController()
ui = UI(controller)
ui.start()