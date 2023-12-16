from shiny_server import server
from shiny_ui import app_ui
from shiny import App

app = App(app_ui, server)
