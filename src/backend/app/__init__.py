""" Flask application configuration  """

from flask import Flask

app = Flask(__name__)
app.config.from_envvar('CONFIG_FILE')

from app.controllers import *
from app.error_handlers import *
from app.models import *
