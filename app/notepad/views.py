from . import notepad_blueprint
from flask import render_template, url_for, redirect
from .notepad import Notes
from .form import NotesForm



@notepad_blueprint.route('/', methods=['POST', 'GET'])
def home():
    Notepad = Notes()
    notes_form = NotesForm()
    if notes_form.validate_on_submit():
        new = notes_form.text.data
        if new:
            Notepad.notes = new
        return redirect(url_for('notepad.home'))
    return render_template('notepad/home.html', notepad=Notepad, form=notes_form)

