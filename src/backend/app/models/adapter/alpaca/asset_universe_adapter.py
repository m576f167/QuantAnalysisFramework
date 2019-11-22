from app.models.asset_universe_model import AssetUniverseModel

class AssetUniverseAdapter():
    """
    Class adapter for Alpaca asset to AssetUniverseModel
    """
    @staticmethod
    def convert(data):
        """
        Convert Alpaca asset to AssetUniverseModel

        Parameters
        ----------
        data : Asset
            Alpaca asset instance

        Returns
        -------
        AssetUniverseModel
            AssetUniverseModel from the converted Alpaca asset instance
        """
        raw_data = data._raw
        return AssetUniverseModel(
            symbol = raw_data['symbol'],
            asset_class = raw_data['class'],
            easy_to_borrow = raw_data['easy_to_borrow'],
            exchange = raw_data['exchange'],
            asset_id = raw_data['id'],
            marginable = raw_data['marginable'],
            name = raw_data['name'],
            shortable = raw_data['shortable'],
            status = raw_data['status'],
            tradable = raw_data['tradable']
        )
