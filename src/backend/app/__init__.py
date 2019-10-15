""" Flask application configuration  """

import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from flask_migrate import Migrate
from config import Config

db = MongoAlchemy()
migrate = Migrate()

def create_app(config_class = Config, load_from_envvar = True):
    """
    Create an instance of Flask application and configure it according to the
    config_class and environment variable

    Parameters
    ----------
    config_class : object, optional
        The object containing configuration for the application (default is Config
        object stored in config.py)
    load_from_envvar : bool, optional
        Whether we want to load configuration from a file referred by the value
        of 'CONFIG_FILE' environment variable (default is True)

    Returns
    -------
    object
        A Flask application instance generated
    """

    app = Flask(__name__)
    app.config.from_object(config_class)
    if load_from_envvar:
        app.config.from_envvar('CONFIG_FILE')

    db.init_app(app)
    migrate.init_app(app)

    from app.controllers import bp as bp_controllers
    app.register_blueprint(bp_controllers)

    from app.error_handlers import bp as bp_error_handlers
    app.register_blueprint(bp_error_handlers)

    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/application.log',
                                           backupCount = 10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Application Started')

    return app
