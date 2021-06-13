# Option 2) Run tests by markers
#
# Pytest allows us to set various attributes for the test methods using pytest markers, @pytest.mark . To use markers in the test file, we need to import pytest on the test files.
#
# Here we will apply different marker names to test methods and run specific tests based on marker names. We can define the markers on each test names by using
#
# @pytest.mark.<name>.
# We are defining markers set1 and set2 on the test methods, and we will run the test using the marker names. Update the test files with the following code
#
# test_sample1.py


import pytest
@pytest.mark.set1
def test_file1_method1():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
    assert x == y, "test failed because x=" + str(x) + " y=" + str(y)


@pytest.mark.set2
@pytest.mark.set3
def test_file1_method2():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
