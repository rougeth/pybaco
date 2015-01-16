from string import digits, ascii_uppercase, ascii_lowercase


class Baco(object):

    def __init__(self, number, alphabet):
        self.number = number
        self.base = len(alphabet)
        self.alphabet = alphabet

    def convert(self, alphabet):
        number = self.number
        base = len(alphabet)
        digits = []
        while number > 0:
            digits.insert(0, number % base)
            number = number // base

        return ''.join([alphabet[d] for d in digits])

    @classmethod
    def to_bin(cls, number, alphabet=digits):
        b = cls(number=number, alphabet=alphabet)
        return b.convert('01')

    @classmethod
    def to_oct(cls, number, alphabet=digits):
        b = cls(number=number, alphabet=alphabet)
        return b.convert('01234567')

    @classmethod
    def to_hex(cls, number, alphabet=digits):
        b = cls(number=number, alphabet=alphabet)
        return b.convert(digits + 'abcdef')

    @classmethod
    def to_36(cls, number, alphabet=digits):
        b = cls(number=number, alphabet=alphabet)
        return b.convert(digits + ascii_lowercase)

    @classmethod
    def to_62(cls, number, alphabet=digits):
        b = cls(number=number, alphabet=alphabet)
        return b.convert(digits + ascii_uppercase + ascii_lowercase)
