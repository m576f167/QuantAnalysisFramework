""" Module for controllers in the application """

import os
import glob
from flask import Blueprint

bp = Blueprint('controllers', __name__)

__all__ = [os.path.basename(f)[:-3]
    for f in glob.glob(os.path.dirname(__file__) + "/*.py")]

from . import *
from . import error_handlers
