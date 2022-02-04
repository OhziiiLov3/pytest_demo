""" 
This module contains baisc unit tests for math operations.
Thier purpose is to show how to use the pytest framework by example.

"""

# A Basic Test Function, our test cas checks the basic operation of addition 
# Pass test 

def test_one_plus():
    # assert is bulit-in and evaluates as a boolean and raises an excpetion of type error
    assert 1 + 1 == 2 
# Fail Test Case 

# A Test Function to show Assertion Introspection

def test_one_plus_two():
    a = 1 
    b = 2
    c = 0
    assert a + b == c 