import unittest
from string import ascii_lowercase, ascii_uppercase, digits

from baco import Baco, base2, base8, base10, base16, base36, base62


class TestPybaco(unittest.TestCase):
    def test_Baco_alphabets(self):
        self.assertEqual(base2, '01')
        self.assertEqual(base8, '01234567')
        self.assertEqual(base10, digits)
        self.assertEqual(base16, digits + 'abcdef')
        self.assertEqual(base36, digits + ascii_lowercase)
        self.assertEqual(base62, digits + ascii_uppercase + ascii_lowercase)

    def test_Baco_class(self):
        b = Baco(number=18, alphabet=digits)
        self.assertEqual(b.number, [1, 8])
        self.assertEqual(b.base, 10)
        self.assertEqual(b.alphabet, digits)

    def test_converting_dec_to_hex_passing_alphabet(self):
        b = Baco(number=18, alphabet=digits)
        self.assertEqual(b.convert(base16), '12')

    def test_converting_dec_to_hex(self):
        b = Baco.to_hex(15)
        self.assertEqual(b, 'f')

    def test_converting_dec_to_bin(self):
        b = Baco.to_bin(18)
        self.assertEqual(b, '10010')

    def test_converting_dec_to_oct(self):
        b = Baco.to_oct(18)
        self.assertEqual(b, '22')

    def test_converting_dec_to_36(self):
        b = Baco.to_36(123456789)
        self.assertEqual(b, '21i3v9')

    def test_converting_dec_to_62(self):
        b = Baco.to_62(123456789)
        self.assertEqual(b, '8M0kX')

    def test_converting_hex_to_62(self):
        b = Baco.to_62('abc', base16)
        self.assertEqual(b, 'iK')

    def test_converting_62_to_10(self):
        b = Baco.to_dec('1LY7VK', base62)
        self.assertEqual(b, '1234567890')


if __name__ == '__main__':
    unittest.main()
