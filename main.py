from settings import ROUTES, FRONT_CONTROLLER
from simple_uwsgi import App

application = App(ROUTES, FRONT_CONTROLLER)
