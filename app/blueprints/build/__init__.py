from flask import Blueprint

bp = Blueprint('build',__name__,url_prefix = '')

from . import routes