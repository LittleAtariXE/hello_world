from flask import render_template
from . import make_fake_blueprint
from .form import FakeForm

@make_fake_blueprint.route('/', methods=['POST', 'GET'])
def home():
    form = FakeForm()
    return render_template('make_fake/home.html', form=form)
