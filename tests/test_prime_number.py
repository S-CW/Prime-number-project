import pytest
from prime_number import *

def test_prime_number():
    assert is_prime(1) == False
    assert is_prime(29) == True

def test_composite_number():
    assert is_prime(9) == False

def test_prime_number_sum():
    assert sum_of_prime([]) == 0
    assert sum_of_prime([2, 3, 5, 7, 11]) == 28