from string import digits, ascii_uppercase, ascii_lowercase


base2 = digits[:2]
base8 = digits[:8]
base10 = digits
base16 = digits + 'abcdef'
base36 = digits + ascii_lowercase
base62 = digits + ascii_uppercase + ascii_lowercase


class Baco(object):

    def __init__(self, number, alphabet):

        self.number = [alphabet.index(i) for i in str(number)]
        self.base = len(alphabet)
        self.alphabet = alphabet

    def convert(self, alphabet):

        digits = self.number
        base = len(alphabet)

        number = 0
        for digit in digits:
            number = self.base * number + digit

        digits = []
        while number > 0:
            digits.insert(0, number % base)
            number = number // base

        return ''.join([alphabet[d] for d in digits])

    @classmethod
    def to_bin(cls, number, alphabet=digits):
        b = cls(number=number, alphabet=alphabet)
        return b.convert(base2)

    @classmethod
    def to_oct(cls, number, alphabet=digits):
        b = cls(number=number, alphabet=alphabet)
        return b.convert(base8)

    @classmethod
    def to_dec(cls, number, alphabet):
        b = cls(number=number, alphabet=alphabet)
        return b.convert(base10)

    @classmethod
    def to_hex(cls, number, alphabet=digits):
        b = cls(number=number, alphabet=alphabet)
        return b.convert(base16)

    @classmethod
    def to_36(cls, number, alphabet=digits):
        b = cls(number=number, alphabet=alphabet)
        return b.convert(base36)

    @classmethod
    def to_62(cls, number, alphabet=digits):
        b = cls(number=number, alphabet=alphabet)
        return b.convert(base62)
