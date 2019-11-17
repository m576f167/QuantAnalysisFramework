from .task import Task

class TaskBuilder:
    """
    A class representing a builder for a task
    """
    def __init__(self, target_function, *args, **kwargs):
        """
        Constructor to initialize the target_function, args, and kwargs. It also
        initializes the following to their default values:
            name = 'task'
            time_delay = 0
            time_interval = 0
            num_to_run = 1

        Parameters
        ---------
        target_function: function
            A function to be run
        args : tuple
            A tuple containing *args to be passed in to target_function
        kwargs: dict
            A dict containing **kwargs to be passed in to target_function

        Returns
        -------
        TaskBuilder
            Return self
        """
        self.target_function = target_function
        self.args = args
        self.kwargs = kwargs
        self.name = 'task'
        self.time_delay = 0
        self.time_interval = 0
        self.num_to_run = 1
        return self

    def build(self):
        """
        Build and return a Task

        Returns
        -------
        Task
            A Task
        """
        return Task(self.target_function,
                    self.args,
                    self.kwargs,
                    self.name,
                    self.time_delay,
                    self.time_interval,
                    self.num_to_run)

    def set_name(self, name):
        """
        Set the name of the task

        Parameters
        ----------
        name : string
            A string name for the task

        Returns
        -------
        TaskBuilder
            Return self
        """
        self.name = name
        return self

    def set_time_delay(self, time_delay):
        """
        Set the time delay before running the target_function

        Parameters
        ----------
        time_delay : float
            A float representing time_delay (in seconds) to run target_function

        Returns
        -------
        TaskBuilder
            Return self
        """
        self.time_delay = time_delay
        return self

    def set_time_interval(self, time_interval):
        """
        Set the time interval for running the target_function

        Parameters
        ----------
        time_interval : float
            A float representing time_interval (in seconds) to run target_function

        Returns
        -------
        TaskBuilder
            Return self
        """
        self.time_interval = time_interval
        return self

    def set_num_to_run(self, num_to_run):
        """
        Set the number of times to run the target_function

        Parameters
        ----------
        num_to_run : int
            An int representing how many times to run target_function

        Returns
        -------
        TaskBuilder
            Return self
        """
        self.num_to_run = num_to_run
        return self
