""" Flask application configuration  """

import logging
from flask import Flask
from flask_injector import FlaskInjector
from flask_mongoengine import MongoEngine
from config import Config
from injector import Injector
from app.services.common.logging.logger import Logger

def create_db_client():
    """
    Create an instance of database client

    Returns
    -------
    MongoEngine
        A database client
    """
    return MongoEngine()

def create_app(config_class = Config, modules = [], injector = None, load_from_envvar = True):
    """
    Create an instance of Flask application and configure it according to the
    config_class and environment variable

    Parameters
    ----------
    config_class : object, optional
        The object containing configuration for the application (default is Config
        object stored in config.py)
    modules: list, optional
        A list of modules for FlaskInjector
    load_from_envvar : bool, optional
        Whether we want to load configuration from a file referred by the value
        of 'CONFIG_FILE' environment variable (default is True)

    Returns
    -------
    Flask
        A Flask application instance generated
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    if load_from_envvar:
        app.config.from_envvar('CONFIG_FILE')

    db_client = create_db_client()
    db_client.init_app(app)

    from app.controllers import bp as bp_controllers
    app.register_blueprint(bp_controllers)

    if injector is None:
        injector = Injector()
    FlaskInjector(app = app, modules = modules, injector = injector)

    if not app.debug and not app.testing:
        logger = injector.get(Logger)
        logger.set_flask_app(app)
        logger.write(logging.INFO, 'Application Started')

    return app
