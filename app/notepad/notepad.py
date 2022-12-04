import json
import os


notes_path = os.path.dirname(__file__) + '/notes.json'

def load_json():
    try:
        with open(notes_path, 'r') as f:
            notes = json.loads(f.read())
    except:
        notes = {1: 'Hello World'}
    return notes

class Notes:
    def __init__(self, notes=load_json()):
        self._notes = notes

    def save(self):
        notes_json = json.dumps(self.notes, indent=3)
        with open(notes_path, 'w') as f:
            f.write(notes_json)

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, note):
        index = len(self.notes) + 1
        self.notes[index] = note
        self.save()

    def remove(self, index):
        del self.notes[index]
        self.save()


##### TEST





