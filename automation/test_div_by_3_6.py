"""
Fixtures are functions, which will run before each test function to which it is applied. 
Fixtures are used to feed some data to the tests such as database connections,
 URLs to test and some sort of input data.
""" 
import pytest

#annotation used to indicate fun as fixture which provides input to test fun
#its scope is limite dto this file
# to use it in other files also define it in conftest.py file
@pytest.fixture
def input_value():
   input = 45
   return input

#pass fun name as arg from which you are taking input for testing
def test_div_by_3(input_value):
   assert input_value % 3 == 0

def test_div_by_6(input_value):
   assert input_value % 6 == 0