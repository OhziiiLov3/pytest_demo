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
    assert 1 + 1 == 0 

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

# Parameterized Test Cases 
# Mutliplication test idea 
# Two postive intgers 
# Identity: multiplying any number by 1 
# Zero: multiplying any number by 0 
# Positive by a negative 
# Negative by a negative 
# Multiply by floats 

# def test_multiply_two_positive_ints():
#     assert 2 * 3 == 6

# def test_multiply_identity():
#     assert 1 * 99 == 99 

# def test_multiply_zero():
#     assert 0 * 100 == 0 

# DRY: Remember DOnt repeat yourself 

products = [
    (2, 3, 6),         # Positive Intgers 
    (1, 99, 99),       # Identity
    (0, 99, 0),        # Zero
    (3, -4, -12),      # Positive by Negative 
    (-5, -5, 25),      # Negative by Negative 
    (2.5, 6.7, 16.75)  # Floats 
]
# Decorators are a special function that wraps around another function. The inner function is the test case 
@pytest.mark.parametrize('a , b , product', products)
def test_multiplication(a, b, product):
    assert a * b == product

# Testing Classes 


