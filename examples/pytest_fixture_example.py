import pytest


def get_data():
    # Retrieve values from CSV
    return [['a','b','c'], 'bb', 'cc']

@pytest.mark.parametrize("value", get_data())
def test_sample(value):
    print(f'input params given from function : {value}')