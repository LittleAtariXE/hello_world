from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class FakeForm(FlaskForm):
    name = StringField('Podaj imię lub pozostaw puste')
    surname = StringField('Podaj nazwisko lub pozostaw puste')
    submit = SubmitField('GENERUJ')
