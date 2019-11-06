""" Controller for Asset Universe REST API """

from . import bp
from app.services.alpaca.asset_universe_manager import AssetUniverseManager
import json

__ROOT_PATH = '/asset_universe/{}'

@bp.route(__ROOT_PATH.format(''),
          methods = ["GET"])
def get_all(asset_universe_manager: AssetUniverseManager):
    """
    Get all asset symbols in asset universe

    Parameters
    ----------
    asset_universe_manager : AssetUniverseManager
        An asset universe manager instance

    Returns
    -------
    string
        A JSON string containing the list of asset symbols in the asset universe
    """
    return json.dumps(asset_universe_manager.get_all())

@bp.route(__ROOT_PATH.format('<string:symbol>'),
          methods = ["GET"])
def contains(asset_universe_manager: AssetUniverseManager,
             symbol):
    """
    Check if the asset universe contains the asset symbol

    Parameters
    ----------
    asset_universe_manager : AssetUniverseManager
        An asset universe manager instance
    symbol: string
        An asset symbol String

    Returns
    -------
    string
        A JSON string of true (on existence) or false
    """
    return json.dumps(asset_universe_manager.contains(symbol))

@bp.route(__ROOT_PATH.format('<string:symbol>'),
          methods = ["POST", "PUT"])
def insert(asset_universe_manager: AssetUniverseManager,
           symbol):
    """
    Insert asset symbol to the asset universe

    Parameters
    ----------
    asset_universe_manager : AssetUniverseManager
        An asset universe manager instance
    symbol: string
        An asset symbol String

    Returns
    -------
    string
        A JSON string of true (on success) or false
    """
    return json.dumps(asset_universe_manager.insert(symbol))

@bp.route(__ROOT_PATH.format('<string:symbol>'),
          methods = ["DELETE"])
def delete(asset_universe_manager: AssetUniverseManager,
           symbol):
    """
    Delete asset symbol from the asset universe

    Parameters
    ----------
    asset_universe_manager : AssetUniverseManager
        An asset universe manager instance
    symbol: string
        An asset symbol String

    Returns
    -------
    string
        A JSON string of true (on success) or false
    """
    return json.dumps(asset_universe_manager.delete(symbol))
