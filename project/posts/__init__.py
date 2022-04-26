"""
The recipes Blueprint handles the creation, modification, deletion,
and viewing of recipes for this application.
"""
from flask import Blueprint
posts_blueprint = Blueprint('posts', __name__, template_folder='templates')

from . import routes
