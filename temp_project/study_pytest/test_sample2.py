# Run a subset of Entire Test with PyTest :
# Sometimes we don't want to run the entire test suite. Pytest allows us to run specific tests. We can do it in 2 ways
#
# Grouping of test names by substring matching
# Grouping of tests by markers

### >> py.test -k method1 -v
import pytest


@pytest.mark.set1
def test_file2_method1():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
    assert x == y, "test failed because x=" + str(x) + " y=" + str(y)


@pytest.mark.set1
def test_file2_method2():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
