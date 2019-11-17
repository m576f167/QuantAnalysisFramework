import os
import logging
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, log_path, log_name, backup_count):
        """
        Constructor to initialize Logger and initialize the log handler

        Parameters
        ----------
        log_path : string
            A string representing the path to store the log
        log_name : string
            A string representing the name of the log
        backup_count : int
            The number of back up log
        """
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        self.__log_handler__ = RotatingFileHandler(os.path.join(log_path, log_name),
                                           backupCount = backup_count)
        self.__log_handler__.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s'
            '[in %(pathname)s:%(lineno)d]'
        ))
        self.__app__ = None

    def write(self, log_level, message):
        """
        Log a message according to the level

        Parameters
        ----------
        log_level : integer
            Integer value for logging level (example: logging.INFO, logging.WARNING, etc)
        message : string
            A string representing the message

        Raises
        ------
        TypeError
            If the flask app instance has not been set
        """
        if self.__app__ is None:
            raise TypeError('Flask App instance has not been set')
        self.__app__.logger.setLevel(log_level)
        self.__app__.logger.log(log_level, message)

    def set_flask_app(self, app):
        """
        Set Flask app instance

        Parameters
        ----------
        app : Flask
            A Flask app instance
        """
        self.__app__ = app
        self.__app__.logger.addHandler(self.__log_handler__)
