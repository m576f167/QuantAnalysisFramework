import logging
from .task_entry import TaskEntry
from app.services.common.logging.logger import Logger

class TaskManager:
    """
    A class for managing tasks
    """
    def __init__(self, logger: Logger):
        """
        Constructor to initialize the task manager

        Parameters
        ----------
        logger : Logger
            A Logger instance
        """
        self.__tasks__ = []
        self.logger = logger

    def add_task(self, task):
        """
        Add a new task to the task manager

        Parameters
        ----------
        task : Task
            A task
        """
        self.__tasks__.append(TaskEntry(task))
        self.logger.write(logging.INFO,
                          "A new task '{}' has been added".format(task.name))

    def remove_task(self, task_id):
        """
        Remove a task from the task manager

        Parameters
        ----------
        task_id : int
            Task id of the task to be removed
        """
        try:
            task_entry = self.__tasks__.pop(task_id)
            task_entry.stop_task()
        except IndexError as e:
            self.logger.write(logging.ERROR,
                              "A task with task_id: {} could not be found\n[{}]".format(task_id, str(e)))

    def run_task(self, task_id):
        """
        Run a task with task_id

        Parameters
        ----------
        task_id : int
            Task id of the task to be run
        """
        try:
            task_entry = self.__tasks__[task_id]
            task_entry.start_task()
        except IndexError as e:
            self.logger.write(logging.ERROR,
                              "A task with task_id: {} could not be found\n[{}]".format(task_id, str(e)))

    def stop_task(self, task_id):
        """
        Stop a task with task_id

        Parameters
        ----------
        task_id : int
            Task id of the task to be stopped
        """
        try:
            task_entry = self.__tasks__[task_id]
            task_entry.stop_task()
        except IndexError as e:
            self.logger.write(logging.ERROR,
                              "A task with task_id: {} could not be found\n[{}]".format(task_id, str(e)))

    def get_all_tasks(self):
        """
        Get a list of all tasks

        Returns
        -------
        list
            A list of all tasks
        """
        return self.__tasks__

    def get_running_tasks(self):
        """
        Get a list of all running tasks

        Returns
        -------
        list
            A list of all running tasks
        """
        return [task_entry  for task_entry in self.__tasks__ if task_entry.is_running()]

    def get_idle_tasks(self):
        """
        Get a list of all idle tasks

        Returns
        -------
        list
            A list of all idle tasks
        """
        return [task_entry for task_entry in self.__tasks__ if not task_entry.is_running()]
