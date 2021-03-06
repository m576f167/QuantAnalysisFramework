""" Controller for Asset Universe REST API """

from . import bp
from app.services.alpaca.asset_universe_manager import AssetUniverseManager
from flask import abort
from mongoengine import OperationError
from bson import json_util as json

__ROOT_PATH = '/asset_universe/{}'

@bp.route(__ROOT_PATH.format(''),
          methods = ["GET"])
def asset_universe_controller_get_all(
    asset_universe_manager: AssetUniverseManager):
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
def asset_universe_controller_get(
    asset_universe_manager: AssetUniverseManager,
    symbol):
    """
    Get an asset with the requested symbol in the Asset Universe

    Parameters
    ----------
    asset_universe_manager : AssetUniverseManager
        An asset universe manager instance
    symbol: string
        An asset symbol String

    Returns
    -------
    string
        200 The json representation of the asset with the requested symbol

    Raises
    ------
    HTTPException
        404 if symbol does not exist
    """
    try:
        asset = asset_universe_manager.get(symbol)
        return json.dumps(asset), 200
    except LookupError as error:
        abort(404, str(error))

@bp.route(__ROOT_PATH.format('<string:symbol>'),
          methods = ["POST", "PUT"])
def asset_universe_controller_insert(
    asset_universe_manager: AssetUniverseManager,
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
        201 if symbol is created

    Raises
    ------
    HTTPException
        404 if symbol is not created
    """
    try:
        asset_universe_manager.insert(symbol)
    except LookupError as error:
        abort(404, str(error))
    except OperationError as error:
        abort(404, str(error))
    return '', 201

@bp.route(__ROOT_PATH.format('<string:symbol>'),
          methods = ["DELETE"])
def asset_universe_controller_delete(
    asset_universe_manager: AssetUniverseManager,
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
        204 No content if symbol is deleted

    Raises
    ------
    HTTPException
        404 if symbol does not exist
    """
    try:
        asset_universe_manager.delete(symbol)
    except LookupError as error:
        abort(404, str(error))
    return '', 204
