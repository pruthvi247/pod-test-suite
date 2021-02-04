import pytest

####### pytest setup example
# @pytest.fixture()
# def setUp() : ### this method name need not be as setup only we can give any name like m1(), setup and tear down is defined by fixtrues
#         print('Setup method')
#
# def test_method1():
#         print('Test method 1')
#
# def test_method2(setUp): ### here we are associating setup fixture with test_method2
#         print('Test method 2')
# @pytest.yield_fixture(scope='module')
# def setupandteardownClass():
#         print('class level setup')
#         yield
#         print('class level teardown')
#
# @pytest.yield_fixture()
# def setupandteardownmethod():
#         print('method level setup')
#         yield
#         print('method level teardown')
#
# def test_method1(setupandteardownClass,setupandteardownmethod):
#         print('test_method1')
#
# def test_method2(setupandteardownmethod):
#         print('test_method2')


@pytest.fixture
def error_fixture():
    print(">>>>>>><<<<<< error_fixture")
    # assert 0
    pass

def test_ok():
    print("ok")

# def test_fail():
#     assert 0

def test_error(error_fixture):
    print(">>>>>>><<<<<< test error")
    pass

def test_skip():
    pytest.skip("skipping this test")

# def test_xfail():
#     pytest.xfail("xfailing this test")

# @pytest.mark.xfail(reason="always xfail")
# def test_xpass():
#     pass