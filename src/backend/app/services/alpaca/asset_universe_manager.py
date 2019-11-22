import logging
from alpaca_trade_api import REST as ApiREST
from alpaca_trade_api.rest import APIError
from app.models.adapter.alpaca.asset_universe_adapter import AssetUniverseAdapter
from app.models.asset_universe_model import AssetUniverseModel
from app.services.common.logging.logger import Logger
from mongoengine import OperationError

class AssetUniverseManager:
    """
    A class for managing asset universe
    """
    def __init__(self, api_rest: ApiREST, logger: Logger):
        """
        Constructor to initialize AssetUniverseManager

        Parameters
        ----------
        api_rest : ApiREST
            An ApiREST instance
        logger : Logger
            A Logger instance
        """
        self.__api_rest__ = api_rest
        self.logger = logger

    def get_all(self):
        """
        Get all asset symbols in asset universe

        Returns
        -------
        list
            A list of asset symbols in the asset universe
        """
        return [document.to_mongo().to_dict()
                for document in AssetUniverseModel.objects]

    def insert(self, symbol):
        """
        Insert asset symbol to the asset universe

        Parameters
        ----------
        symbol : String
            An asset symbol String

        Raises
        ------
        LookupError
            If the symbol could not be found in Alpaca
        OperationError
            If could not save the symbol in Database
        """
        try:
            asset = self.__api_rest__.get_asset(symbol)
            document = AssetUniverseAdapter.convert(asset)
            document.save()
        except APIError as error:
            self.logger.write(logging.ERROR,
                              "Asset symbol {} could not be found in Alpaca\n[{}]".format(symbol, str(error)))
            raise LookupError("[AssetUniverseManager]: {}".format(str(error)))
        except OperationError as error:
            self.logger.write(logging.ERROR,
                              "Error in saving symbol {} in Database\n[{}]".format(symbol, str(error)))
            raise error

    def delete(self, symbol):
        """
        Delete asset symbol from the asset universe

        Parameters
        ----------
        symbol : String
            An asset symbol String

        Raises
        ------
        LookupError
            If the symbol to be deleted does not exist
        """
        document = AssetUniverseModel.objects(symbol = symbol)
        if document:
            document.delete()
        else:
            raise LookupError('[AssetUniverseManager]: symbol does not exist')

    def get(self, symbol):
        """
        Get an asset with the requested symbol in the Asset Universe

        Parameters
        ----------
        symbols : String
            An asset symbol String

        Returns
        -------
        dict
            dict representation of the asset

        Raises
        ------
        LookupError
            If the symbol to be retrieved does not exist
        """
        document = AssetUniverseModel.objects(symbol = symbol)[0]
        if document:
            return document.to_mongo().to_dict()
        else:
            raise LookupError('[AssetUniverseManager]: symbol does not exist')
