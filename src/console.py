def summary():
    pass


def success():
    print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')


def log():
    summary()
    success()
