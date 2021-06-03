from src.config import path, settings
from .models import Data


def read_txt_file():
    rows = open(path.SOME_PATH, 'r', encoding=settings.PROJECT_ENCODING).read().splitlines()
    return rows


def read():
    arr = read_txt_file()
    return Data(
        arr=arr
    )
