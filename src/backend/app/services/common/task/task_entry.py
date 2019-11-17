from datetime import datetime
from threading import Thread
from time import sleep, time

class TaskEntry:
    """
    A class representing task entry in TaskManager
    """
    def __init__(self, task):
        """
        Constructor to initialize the task entry

        Parameters
        ----------
        task: Task
            A task
        """
        self.task = task
        self.__thread__ = Thread(
            target = self.__target_function_wrapper__
        )
        self.__run_counter__ = 0
        self.created_at = datetime.now()
        self.last_run = datetime.now()
        self.is_terminate = True

    def __target_function_wrapper__(self):
        """
        Function wrapper for target function to run it in loop
        """
        sleep(self.task.time_delay)
        while self.__run_counter__ < self.task.num_to_run and not self.is_terminate:
            start_time = time()
            self.task.target_function(*self.task.args, **self.task.kwargs)
            end_time = time()
            elapsed_time = end_time - start_time
            if elapsed_time < self.task.time_interval:
                sleep(self.task.time_interval - elapsed_time)
        self.last_run = datetime.now()

    def is_running(self):
        """
        Check if the task is running

        Returns
        -------
        boolean
            True if task is running, False otherwise
        """
        return self.__thread__.is_alive()

    def start_task(self):
        """
        Start running task
        """
        if self.is_running():
            return
        self.__run_counter__ = 0
        self.is_terminate = False
        self.__thread__.start()

    def stop_task(self):
        """
        Stop running task
        """
        self.is_terminate = True
