from flask import Blueprint

make_fake_blueprint = Blueprint('make_fake', __name__, template_folder='templates')
from . import views