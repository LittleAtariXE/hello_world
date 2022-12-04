import os
from random import choice

lib_path = os.path.dirname(os.path.abspath(__file__)) + '/library'

def load_txt(file_name):
    output = set()
    with open(f'{lib_path}/{file_name}', 'r') as f:
        for line in f.readlines():
            output.add(line.rstrip('\n'))

    return list(output)

def load_library(plec='men'):
    if plec == 'men':
        imiona = load_txt('imiona.txt')
        nazwiska = load_txt('nazwiska.txt')

    library = {
        'imiona': imiona,
        'nazwiska': nazwiska,
    }

    return library

library = load_library()

class Fake:
    def __init__(self, imie=None, nazwisko=None):
        if not imie:
            self.imie = choice(library['imiona'])
        else:
            self.imie = imie

        if not nazwisko:
            self.nazwisko = choice(library['nazwiska'])
        else:
            self.nazwisko = nazwisko



##### TEST

