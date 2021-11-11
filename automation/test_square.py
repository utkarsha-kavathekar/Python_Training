#run code using command pytest
#this command will execute all testing files in current directory
import math
import pytest

@pytest.mark.square
def test_sqrt():
    num=25
    assert math.sqrt(num)==5

@pytest.mark.square
def testsquare():
    num=7
    assert num*num == 40

@pytest.mark.others
def test_equality():
    assert 11==10

#this fun is not executed as test fun as it is not in format test* or *test
def tesequality():
    assert 11==10
