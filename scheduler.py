def get_schedule():
    try:
        with open('schedule.txt') as f:
            contents = f.read()
        if not contents:
            contents = set_schedule("8:00")
    except FileNotFoundError:
        with open('schedule.txt', 'w') as f:
            contents = set_schedule("8:00")
            f.write(contents)
    return contents


def set_schedule(time):
    with open('schedule.txt', 'w') as f:
        f.write(time)
    return time
