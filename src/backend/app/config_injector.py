""" Configuration module for FlaskInjector   """

from alpaca_trade_api import REST as ApiREST
from app.services.alpaca.asset_universe_manager import AssetUniverseManager
from app.services.common.logging.logger import Logger
from app.services.common.task.task_manager import TaskManager
from injector import Module, provider, singleton

class ConfigInjector(Module):
    @provider
    def provider_api_rest(self) -> ApiREST:
        return ApiREST()

    @provider
    @singleton
    def provider_logger(self) -> Logger:
        return Logger('logs', 'application.log', 10)

    @provider
    @singleton
    def provider_asset_universe_manager(self, api_rest: ApiREST, logger: Logger) -> AssetUniverseManager:
        return AssetUniverseManager(api_rest, logger)

    @provider
    @singleton
    def provider_task_manager(self, logger: Logger) -> TaskManager:
        return TaskManager(logger)
