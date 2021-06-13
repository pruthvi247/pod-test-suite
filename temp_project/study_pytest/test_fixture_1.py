import pytest

# @pytest.fixture(autouse=True, scope='module')
@pytest.fixture(autouse=True, scope='function')
def module_setup_teardown():
    print("MODULE SETUP!!!")
    yield
    print("MODULE TEARDOWN!!!")


def test1():
    print("TEST1!!!")


def test2():
    print("TEST2!!!")