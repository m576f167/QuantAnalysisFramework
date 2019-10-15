""" Default controller for hello world """

from . import bp

@bp.route('/')
@bp.route('/index')
def index():
    return "Hello, World!"
