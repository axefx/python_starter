'''
# examples fixtures "https://docs.pytest.org/en/stable/xunit_setup.html"
# use with -s flag
'''
import sys


def setup_module(module):
    print("\nIn setup_module()...")


def teardown_module(module):
    print("\nIn teardown_module()...")


def setup_function(function):
    print("\nIn setup_function()...")


def teardown_function(function):
    print("\nIn teardown_function()...")


def test_python_version():

    # tests if we are using python 3.9
    assert sys.version_info.major == 3 and sys.version_info.minor == 9
