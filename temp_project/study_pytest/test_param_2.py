import pytest

# @pytest.mark.parametrize("x, y", [("a", "b")], indirect=["x"])
# @pytest.mark.parametrize("x, y", [("a", "b")],indirect=["x"])
# def test_indirect(x, y):
#     assert x == "a"
#     assert y == "b"

# @pytest.fixture(scope="function")
# def y(request):
#     return request.param * 2
#
#
# @pytest.mark.parametrize("x, y", [("a", "b")], indirect=["y"])
# def test_indirect(x, y):
#     assert x == "aaa"
#     assert y == "b"

# @pytest.fixture(scope="module", params=["mod1", "mod2"])
# def modarg(request):
#     param = request.param
#     print("  SETUP modarg", param)
#     yield param
#     print("  TEARDOWN modarg", param)
#
# @pytest.fixture(scope="function", params=[1, 2])
# def otherarg(request):
#     param = request.param
#     print("  SETUP otherarg", param)
#     yield param
#     print("  TEARDOWN otherarg", param)
#
# def test_0(otherarg):
#     print("  RUN test0 with otherarg", otherarg)
#
# def test_1(modarg):
#     print("  RUN test1 with modarg", modarg)
#
# def test_2(otherarg, modarg):
#     print("  RUN test2 with otherarg {} and modarg {}".format(otherarg, modarg))

# test_parameterized_fixture2.py
import pytest

class MyTester:
    def __init__(self, x):
        self.x = x

    def dothis(self):
        assert self.x
        # assert True

@pytest.fixture
def tester(tester_arg):
    """Create tester object"""
    return MyTester(tester_arg)


class TestIt:
    @pytest.mark.parametrize('tester_arg', [True, False])
    def test_tc1(self, tester):
       tester.dothis()
       assert True