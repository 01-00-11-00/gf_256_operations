# ---------------------------- GF 256 Operations ------------------------------- #

class GF256Operations:

    # Constructor
    def __init__(self, minimal_polynomial: int):
        self.minimal_polynomial = minimal_polynomial

    # Methods
    @staticmethod
    def get_degree(a) -> int:
        """
        Get the degree of a given polynomial.
        :param a: The polynomial to get the degree of.
        :return: The degree of the polynomial.
        """

        return a.bit_length() - 1

    @staticmethod
    def add(a: int, b: int) -> int:
        """
        Add two numbers in GF(2^8).
        :param a: The first number.
        :param b: The second number.
        :return: The result of the addition.
        """

        return a ^ b

    def multiply(self, a: int, b: int) -> int:
        """
        Multiply two numbers in GF(2^8).
        :param a: The first number.
        :param b: The second number.
        :return: The result of the multiplication.
        """

        result = 0

        while b:
            if b & 1:
                result ^= a

            a <<= 1

            if a & 0x100:
                a ^= self.minimal_polynomial

            b >>= 1

        return result & 0xff

    def modular_reduction(self, a: int) -> int:
        """
        Perform a modular reduction of a number in GF(2^8).
        :param a: The number to be reduced.
        :return: The result of the reduction.
        """

        while a >= 256:
            a ^= self.minimal_polynomial << (a.bit_length() - 9)

        return a

    def invert(self, a) -> int:
        """
        Invert a number in GF(2^8).
        :param a: The number to be inverted.
        :return: The inverse of the number.
        """

        min_pol = self.minimal_polynomial
        coefficient_1 = 1
        coefficient_2 = 0
        difference = self.get_degree(a) - 8

        while a != 1:
            if difference < 0:
                a, min_pol = min_pol, a
                coefficient_1, coefficient_2 = coefficient_2, coefficient_1
                difference = -difference

            a ^= min_pol << difference
            coefficient_1 ^= coefficient_2 << difference

            a %= 256
            coefficient_1 %= 256

            difference = self.get_degree(a) - self.get_degree(min_pol)

        return coefficient_1
