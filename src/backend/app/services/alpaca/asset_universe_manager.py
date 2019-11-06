from app.models.asset_universe_model import AssetUniverseModel

class AssetUniverseManager:
    """
    A class for managing asset universe
    """
    def get_all(self):
        """
        Get all asset symbols in asset universe

        Returns
        -------
        list
            A list of asset symbols in the asset universe
        """
        return [document.symbol for document in AssetUniverseModel.objects]

    def insert(self, symbol):
        """
        Insert asset symbol to the asset universe

        Parameters
        ----------
        symbol : String
            An asset symbol String

        Returns
        -------
        boolean
            True if successful, False otherwise
        """
        document = AssetUniverseModel(symbol = symbol)
        document.save()
        return True

    def delete(self, symbol):
        """
        Delete asset symbol from the asset universe

        Parameters
        ----------
        symbol : String
            An asset symbol String

        Returns
        -------
        boolean
            True if successful, False otherwise
        """
        document = AssetUniverseModel.objects(symbol = symbol)
        if document:
            document.delete()
            return True
        else:
            return False

    def contains(self, symbol):
        """
        Check if the asset universe contains the asset symbol

        Parameters
        ----------
        symbols : String
            An asset symbol String

        Returns
        -------
        boolean
            True if successful, False otherwise
        """
        return True if AssetUniverseModel.objects(symbol = symbol) else False
