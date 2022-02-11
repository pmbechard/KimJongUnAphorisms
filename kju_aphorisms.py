from random import choice


def get_kju_aphorism():
    with open('KimJongUn-Aphorisms-2016.txt') as f:
        contents = f.read()

    contents = contents.replace('“', '"').replace('”', '"').split('"')
    contents = contents[1:-1:2]

    return choice(contents)
