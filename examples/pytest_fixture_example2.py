import pytest
import pandas as pd
# import datatest as dt


@pytest.fixture(scope='module')
def mydata():
    return pd.DataFrame(
        data=[
            ['x', 'foo', 20],
            ['x', 'foo', 30],
            ['y', 'foo', 10],
            ['y', 'bar', 20],
            ['z', 'bar', 10],
            ['z', 'bar', 10],
        ],
        columns=['A', 'B', 'C'],
    )

# @pytest.mark.parametrize("value", get_data())
def test_total(mydata):
    total = mydata['C'].sum()
    requirement = 100

def test_total1(mydata):
    total = mydata['B'].sum()
    requirement = 100
