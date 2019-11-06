""" Configuration module for FlaskInjector   """

from app.services.alpaca.asset_universe_manager import AssetUniverseManager
from injector import Module, provider, singleton

class ConfigInjector(Module):
    @provider
    @singleton
    def provider_asset_manager_universe(self) -> AssetUniverseManager:
        return AssetUniverseManager()
