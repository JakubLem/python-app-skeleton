from typing import Set


class Settings:
    PROJECT_NAME = 'some name'
    PROJECT_ENCODING = 'utf-8'


class Files:
    SOME_FILE = 'test.txt'


class Path:
    SOME_PATH = f'data/{Files.SOME_FILE}'


settings = Settings()
path = Path()
