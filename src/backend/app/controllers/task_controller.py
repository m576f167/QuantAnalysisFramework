""" Controller for Task Manager REST API """

from . import bp
from app.services.common.task.task_manager import TaskManager
from flask import abort
from bson import json_util as json

__ROOT_PATH = '/task/{}'

@bp.route(__ROOT_PATH.format(''),
          methods = ["GET"])
def task_controller_get_all(
    task_manager: TaskManager):
    """
    Get all tasks in task manager

    Parameters
    ----------
    task_manager : TaskManager
        A TaskManager instance

    Returns
    -------
    string
        A JSON string containing all the tasks
    """
    tasks = {task_id: task_entry.task.name for (task_id, task_entry)
             in enumerate(task_manager.get_all_tasks())}
    return json.dumps(tasks)

@bp.route(__ROOT_PATH.format('running'),
          methods = ["GET"])
def task_controller_get_running(
    task_manager: TaskManager):
    """
    Get all running tasks in task manager

    Parameters
    ----------
    task_manager : TaskManager
        A TaskManager instance

    Returns
    -------
    string
        A JSON string containing all the running tasks
    """
    tasks = {task_id: task_entry.task.name for (task_id, task_entry)
             in enumerate(task_manager.get_running_tasks())}
    return json.dumps(tasks)

@bp.route(__ROOT_PATH.format('idle'),
          methods = ["GET"])
def task_controller_get_idle(
    task_manager: TaskManager):
    """
    Get all idle tasks in task manager

    Parameters
    ----------
    task_manager : TaskManager
        A TaskManager instance

    Returns
    -------
    string
        A JSON string containing all the idle tasks
    """
    tasks = {task_id: task_entry.task.name for (task_id, task_entry)
             in enumerate(task_manager.get_idle_tasks())}
    return json.dumps(tasks)

@bp.route(__ROOT_PATH.format('<int:task_id>'),
          methods = ["DELETE"])
def task_controller_remove_task(
    task_manager: TaskManager,
    task_id):
    """
    Stop and remove task with task_id from the TaskManager

    Parameters
    ----------
    task_manager : TaskManager
        A TaskManager instance
    task_id : int
        A task_id to be removed

    Returns
    -------
    string
        204 if task is removed

    Raises
    ------
    HTTPException
        404 if task with task_id does not exist
    """
    try:
        task_manager.remove_task(task_id)
    except IndexError as error:
        abort(404, str(error))
    return '', 204

@bp.route(__ROOT_PATH.format('run/<int:task_id>'),
          methods = ["GET"])
def task_controller_run_task(
    task_manager: TaskManager,
    task_id):
    """
    Run task with task_id in the TaskManager

    Parameters
    ----------
    task_manager : TaskManager
        A TaskManager instance
    task_id : int
        A task_id of the task to be to be run

    Returns
    -------
    string
        204 if task is run

    Raises
    ------
    HTTPException
        404 if task with task_id does not exist
    """
    try:
        task_manager.run_task(task_id)
    except IndexError as error:
        abort(404, str(error))
    return '', 204

@bp.route(__ROOT_PATH.format('stop/<int:task_id>'),
          methods = ["GET"])
def task_controller_stop_task(
    task_manager: TaskManager,
    task_id):
    """
    Stop task with task_id in the TaskManager

    Parameters
    ----------
    task_manager : TaskManager
        A TaskManager instance
    task_id : int
        A task_id of the task to be to be stopped

    Returns
    -------
    string
        204 if task is stopped

    Raises
    ------
    HTTPException
        404 if task with task_id does not exist
    """
    try:
        task_manager.stop_task(task_id)
    except IndexError as error:
        abort(404, str(error))
    return '', 204
