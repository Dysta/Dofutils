class Base64:
    # fmt: off
    _CHARSET: list = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "_",
    ]
    # fmt: on

    @staticmethod
    def ord(char: str) -> int:
        """
        Convert the given single char value in base64

        :param char: The char to convert
        :raises ValueError: When parameter char isn't a single character
        :raises ValueError: When parameter char is outside the charset
        :return: The int value, between 0 and 63 included
        :rtype: int
        """
        if len(char) > 1:
            raise ValueError("Expected a single character")
        if char[0] not in Base64._CHARSET:
            raise ValueError("Invalid char value")

        if "a" <= char <= "z":
            return ord(char) - ord("a")

        if "A" <= char <= "Z":
            return ord(char) - ord("A") + 26

        if "0" <= char <= "9":
            return ord(char) - ord("0") + 52

        if char == "-":
            return 62

        return 63  # char is equal to '_'

    @staticmethod
    def chr(value: int) -> str:
        """
        Get the base64 character from the given value

        :param value: The value to convert
        :raise ValueError: when value is not in the charset
        :return: Encoded value
        :rtype: str
        """
        if not value < len(Base64._CHARSET) or value < 0:
            raise ValueError("Invalid value, must be in the following range [0-63]")
        return Base64._CHARSET[value]

    @staticmethod
    def chr_mod(value: int) -> str:
        """
        Get the base64 character from the given value after applying a modulo on it
        to ensure the call will not fail

        :parameter value: The value to convert
        :return: Encoded value
        :rtype: str
        """
        return Base64._CHARSET[value % len(Base64._CHARSET)]

    @staticmethod
    def encode(value: int, length: int) -> str:
        """
        Encode a int value to pseudo base64

        :param value: value to encode
        :param length: then expected result length. Must be in range [1-6]
        :raise ValueError: when the encoded string is not in range [1-6]
        :return: the decoded value
        :rtype: str
        """
        if length < 1 or length > 6:
            raise ValueError("Parameter length must be in range [1-6]")

        v: int = value
        result: str = ""

        for i in range(length, 0, -1):
            result = str(Base64._CHARSET[v & 63]) + result
            v >>= 6

        return result

    @staticmethod
    def decode(encoded: str) -> int:
        """
        Decode pseudo base64 value to int

        :param encoded: the encoded value
        :return: the decoded value
        :raise ValueError: when the encoded string is not in range [1-6]
        :rtype: int
        """
        if len(encoded) > 6:
            raise ValueError("Parameter too long")

        def overflow(val: int) -> int:
            """
            from https://stackoverflow.com/questions/7770949/simulating-integer-overflow-in-python
            Simulate a int overflow

            :param val: the int to overflow
            :return: the overflowed int
            """

            MAX_INT: int = 2**31 - 1
            if not -MAX_INT - 1 <= val <= MAX_INT:
                val = (val + (MAX_INT + 1)) % (2 * (MAX_INT + 1)) - MAX_INT - 1
            return val

        value: int = 0

        for c in encoded:
            value <<= 6
            value += Base64.ord(c)
            value = overflow(value)

        return value

    @staticmethod
    def to_bytes(encoded: str) -> bytearray:
        """
        Decode a Base 64 string to a byte array
        Each byte will represents the {@link Base64#ord(char)} value of each characters

        :param encoded: the encoded value
        :return: the decoded byte array. The array size will be the same as the string size
        :rtype: bytearray
        """
        b: bytearray = bytearray()
        for c in encoded:
            b.append(Base64.ord(c))

        return b
