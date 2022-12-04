from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import data_required

class NotesForm(FlaskForm):
    text = TextAreaField('Dodaj Notatke', validators=[data_required()])
    submit = SubmitField('Wyślij')