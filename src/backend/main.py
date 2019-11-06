""" Entry point for the application  """

import sys
from app import create_app
from app.config_injector import ConfigInjector

app = create_app(modules = [ ConfigInjector ])
