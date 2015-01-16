from string import digits
from pybaco import Baco


def test_Baco_class():
    b = Baco(number=18, alphabet=digits)
    assert b.number == 18
    assert b.base == 10
    assert b.alphabet == digits


def test_Baco_convert():
    b = Baco(number=18, alphabet=digits)
    assert b.convert(digits + 'abcdef') == '12'


def test_Baco_to_hex():
    b = Baco.to_hex(15)
    assert b == 'f'


def test_baco_to_bin():
    b = Baco.to_bin(18)
    assert b == '10010'


def test_Baco_to_oct():
    b = Baco.to_oct(18)
    assert b == '22'


def test_Baco_to_36():
    b = Baco.to_36(123456789)
    assert b == '21i3v9'


def test_Baco_to_62():
    b = Baco.to_62(123456789)
    assert b == '8M0kX'
