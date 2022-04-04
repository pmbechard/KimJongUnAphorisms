from random import choice


def get_kju_aphorism():
    with open('KimJongUn-Aphorisms-2016.txt') as f:
        contents = f.read()

    contents = contents.replace('“', '"').replace('”', '"').split('"')
    contents = contents[1:-1:2]

    daily_aphorism = choice(contents)

    with open('schedule.txt', 'a') as f:
        f.write(f'\n{daily_aphorism}')

    return daily_aphorism
