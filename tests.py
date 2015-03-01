from string import digits, ascii_uppercase, ascii_lowercase

from baco import Baco, base2, base8, base10, base16, base36, base62


def test_Baco_alphabets():
    assert base2 == '01'
    assert base8 == '01234567'
    assert base10 == digits
    assert base16 == digits + 'abcdef'
    assert base36 == digits + ascii_lowercase
    assert base62 == digits + ascii_uppercase + ascii_lowercase


def test_Baco_class():
    b = Baco(number=18, alphabet=digits)
    assert b.number == [1, 8]
    assert b.base == 10
    assert b.alphabet == digits


def test_Baco_convert():
    b = Baco(number=18, alphabet=digits)
    assert b.convert(base16) == '12'


def test_Baco_to_hex():
    b = Baco.to_hex(15)
    assert b == 'f'


def test_Baco_to_bin():
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


def test_Baco_from_16_to_62():
    b = Baco.to_62('abc', base16)
    assert b == 'iK'


def test_Baco_from_62_to_10():
    b = Baco.to_dec('1LY7VK', base62)
    assert b == '1234567890'
