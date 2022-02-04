""" 
This module contains baisc unit tests for math operations.
Thier purpose is to show how to use the pytest framework by example.

"""
import pytest 

# Python Uses Functions to evaluate Test vs Junit which uses classes 
# A Basic Test Function, our test cas checks the basic operation of addition 
# Pass test 

def test_one_plus():
    # assert is bulit-in and evaluates as a boolean and raises an excpetion of type error
    assert 1 + 1 == 2 

# Fail Test Case 
# A Test Function to show Assertion Introspection
# def test_one_plus_two():
#     a = 1 
#     b = 2
#     c = 0
#     assert a + b == c 
def test_one_plus_two():
    a = 1 
    b = 2
    c = 3
    assert a + b == c 

# Test case with an Exception 

# Test Function that verifies an exception

# def test_divide_by_zero():
#     num = 1 / 0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)


