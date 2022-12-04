from flask import Blueprint

notepad_blueprint = Blueprint('notepad', __name__, template_folder='templates')
from . import views
