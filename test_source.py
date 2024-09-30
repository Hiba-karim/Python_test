# test_source.py
from test import mult_two, rectangle_perimeter, is_even, determine_sign, find_remainder, backward_string, checkio, first_word, number_length

def test_mult_two():
    assert mult_two(3, 2) == 6
    assert mult_two(0, 1) == 0

def test_rectangle_perimeter():
    assert rectangle_perimeter(2, 4) == 12
    assert rectangle_perimeter(3, 5) == 16
    assert rectangle_perimeter(10, 20) == 60

def test_is_even():
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True

def test_determine_sign():
    assert determine_sign(5) == "positive"
    assert determine_sign(0) == "zero"
    assert determine_sign(-10) == "negative"

def test_find_remainder():
    assert find_remainder(10, 3) == 1
    assert find_remainder(14, 4) == 2

def test_backward_string():
    assert backward_string("val") == "lav"
    assert backward_string("") == ""

def test_checkio():
    assert checkio(15) == "Fizz Buzz"
    assert checkio(6) == "Fizz"

def test_first_word():
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"

def test_number_length():
    assert number_length(10) == 2
    assert number_length(0) == 1
