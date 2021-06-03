from colorama import Fore, Style
from .readApp.read import read
from .writeApp.write import write
from . import config, console


def app():
    print(f'Application {Fore.BLUE}{config.Settings.PROJECT_NAME.upper()}{Style.RESET_ALL} has been started')
    print(read())
    write()
    console.log()
