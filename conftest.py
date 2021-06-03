import pytest


@pytest.fixture
def some_obj():
    def result():
        return 11

    return result
