import pytest
#test fun for comparison
#command to execute specific test file
#pytest filenm -v

#To execute test fun with marker name
#pytest -m markernm -v
@pytest.mark.great  #great is marker name
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.others
def test_less():
   num = 100
   assert num < 200

#to execute test fun having specific sub string in it use
#pytest -k substring -v
#pytest -k greater -v