import os
from pymongo import MongoClient

class BasePymongoModel:
    """
    A base class for database model using pymongo
    """
    def __init__(self, config = None):
        """
        Constructor to initialize the host, port, and mongo client

        Parameters
        ----------
        config : dict, optional
            A dictionary containing host and port for mongo client

        Raises
        ------
        KeyError
            If the config does not contain required keys
        """
        self.__host = os.environ.get('MONGODB_HOST')
        self.__port = os.environ.get('MONGODB_PORT')

        if config is not None:
            self.__load_config(config)

        self.__client = MongoClient(self.__host, self.__port)

    def __validate_config(self, config):
        """
        Validate config

        Parameters
        ----------
        config : dict, optional
            A dictionary containing host and port for mongo client

        Raises
        ------
        KeyError
            If the config does not contain required keys
        """
        if 'host' not in config: raise KeyError('Key "host" is not in config')
        if 'port' not in config: raise KeyError('Key "port" is not in config')

    def __load_config(self, config):
        """
        Load the config and set host and port according to it

        Parameters
        ----------
        config : dict, optional
            A dictionary containing host and port for mongo client

        Raises
        ------
        KeyError
            If the config does not contain required keys
        """
        self.__validate_config(config)
        self.__host = config['host']
        self.__port = config['port']
