import pytest


@pytest.fixture()
def name(pytestconfig):
    return pytestconfig.getoption("name")


def test_print_name(name):
    print(f"\ncommand line param (name): {name}")


# print(pytest.config.getoption('name'))

def setup_module(mod):
    print("Host is %s" % pytest.config.getoption('host'))
