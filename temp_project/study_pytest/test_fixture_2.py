import pytest


@pytest.yield_fixture(autouse=True,scope='module')
# @pytest.yield_fixture(scope='module')
def setupandteardownClass():
        print('class level setup')
        yield
        print('class level teardown')


# @pytest.yield_fixture(autouse=True,scope='function')
@pytest.yield_fixture(scope='function')
def setupandteardownmethod():
        print('method level setup')
        yield
        print('method level teardown')


# def test_method1(setupandteardownClass,setupandteardownmethod):
#         print('test_method1')
#
#
# def test_method2(setupandteardownmethod):
#         print('test_method2')


def test_method3():
        print('test_method2')