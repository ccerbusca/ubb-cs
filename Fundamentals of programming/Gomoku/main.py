from UI.ui import UI
from model.settings import Settings

settings = Settings()
if settings.uiType == "console":
    UI.start()