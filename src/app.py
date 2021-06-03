from .readApp.read import read
from .writeApp.write import write
from . import config, console
from colorama import Fore, Style


def app():
    print(f'APPLICATION {Fore.BLUE}{config.Settings.PROJECT_NAME}{Style.RESET_ALL} has been started')
    print(read())
    write()
    console.log()
