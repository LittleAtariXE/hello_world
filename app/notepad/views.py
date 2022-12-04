from . import notepad_blueprint
from flask import render_template, request, url_for, redirect
from .notepad import Notes



@notepad_blueprint.route('/', methods=['POST', 'GET'])
def home():
    Notepad = Notes()
    if request.method == 'POST':
        new = request.form['new']
        if new:
            Notepad.notes = new
        return redirect(url_for('notepad.home'))
    return render_template('notepad/home.html', notepad=Notepad)

