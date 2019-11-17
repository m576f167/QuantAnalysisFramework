""" Configuration module for FlaskInjector   """

from app.services.alpaca.asset_universe_manager import AssetUniverseManager
from app.services.common.logging.logger import Logger
from app.services.common.task.task_manager import TaskManager
from injector import Module, provider, singleton

class ConfigInjector(Module):
    @provider
    @singleton
    def provider_asset_manager_universe(self) -> AssetUniverseManager:
        return AssetUniverseManager()

    @provider
    @singleton
    def provider_logger(self) -> Logger:
        return Logger('logs', 'application.log', 10)

    @provider
    @singleton
    def provider_task_manager(self, logger: Logger) -> TaskManager:
        return TaskManager(logger)
