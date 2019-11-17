
class Task:
    """
    A class representing a task
    """
    def __init__(self,
                 target_function,
                 args,
                 kwargs,
                 name,
                 time_delay,
                 time_interval,
                 num_to_run):
        """
        Constructor to initialize the task

        Parameters
        ----------
        target_function : function
            A function to be run
        args : tuple
            A tuple containing *args to be passed in to target_function
        kwargs: dict
            A dict containing **kwargs to be passed in to target_function
        name : string
            A string name for the task
        time_delay : float
            A float representing time_delay (in seconds) to run target_function
        time_interval : float
            A float representing time_interval (in seconds) to run target_function
        num_to_run : int
            An int representing how many times to run target_function
        """
        self.target_function = target_function
        self.args = args
        self.kwargs = kwargs
        self.name = name
        self.time_delay = time_delay
        self.time_interval = time_interval
        self.num_to_run = num_to_run
