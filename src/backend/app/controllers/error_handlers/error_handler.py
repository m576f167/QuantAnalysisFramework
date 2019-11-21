""" Error handler for the Flask Application """

from . import bp
from werkzeug.exceptions import HTTPException
import json

def create_error_response(error):
    """
    Create error response from an error exception

    Parameters
    ----------
    error : Exception
        An error exception

    Returns
    -------
    string
        A JSON string of the error response
    """
    error_response = json.dumps({
        'status_code': 500,
        'status': error.__class__.__name__,
        'description': str(error),
    })
    return error_response

def create_error_response_from_httpexception(http_exception):
    """
    Create error response from an HTTPException error

    Parameters
    ----------
    http_exception : HTTPException
        An HTTPException error

    Returns
    -------
    string
        A JSON string of the HTTPException error response
    """
    http_exception_response = http_exception.get_response()
    error_response = json.dumps({
        'status_code': http_exception_response.status_code,
        'status': http_exception_response.status,
        'description': http_exception.description,
    })
    return error_response

@bp.errorhandler(HTTPException)
def handle_exception(error):
    """
    Flask error handler for HTTPException

    Parameters
    ----------
    error : HTTPException
        An HTTPException error

    Returns
    -------
    string
        A JSON string of the HTTPException error response
    """
    response = create_error_response_from_httpexception(error)
    status_code = error.get_response().status_code
    return response, status_code

@bp.errorhandler(Exception)
def handle_exception(error):
    """
    Flask error handler for Exception

    Parameters
    ----------
    error : Exception
        An Exception error

    Returns
    -------
    string
        A JSON string of the Exception error response
    """
    response = create_error_response(error)
    return response, 500
