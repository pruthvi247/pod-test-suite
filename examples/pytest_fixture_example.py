import pytest
import logging

logger = logging.getLogger(__name__)

def get_data():
    # Retrieve values from CSV
    # return [['a','b','c'], {"key":'bb'}, 'cc']
    # return [['a', 'b', 'c'], {"key": 'bb'}, 'cc']
    dict = {}
    dict['Capital'] = "London"
    dict['Food'] = "Fish&Chips"
    dict['2012'] = "Olympics"
    return dict.values()

@pytest.mark.parametrize("value", get_data())
def test_sample(value):
    logger.debug("Reading input test case csv >>>>>>>>>: {}".format("dummy")) # doesnot work, pytest has different logging frame work
    print(f'input params given from function : {value}')
    print(f'input params given from function : {type(value)}')


