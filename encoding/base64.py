class Base64:
    _CHARSET: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                      'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                      'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                      'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_']
    _a: int = 97
    _A: int = 65
    _0: int = 48

    def ord(char: str) -> int:
        """
        Convert the given single char value in base64
        :parameter
        char : str
            The char to convert
        :return
            The int value, between 0 and 63 included
        :raises
            Exception when character is outside the charset
            Exception when parameter is not a single char
        """
        if len(char) > 1:
            raise Exception('Incorrect parameter: expected a single character')
        if char[0] not in Base64._CHARSET and not char == '-' and not char == '_':
            raise Exception('Incorrect parameter: invalid char value')

        if 'a' <= char <= 'z':
            return int(char) - Base64._a

        if 'A' <= char <= 'Z':
            return int(char) - Base64._A + 26

        if '0' <= char <= '9':
            return int(char) - Base64._0 + 52

        if char == '-':
            return 62
        elif char == '_':
            return 63
        else:
            raise Exception('Incorrect parameter: invalid char value')


    def chr(value: int) -> str:
        """
        Get the base64 character from the given value
        :parameter
        value : int
            The value to convert
        :return:
            Encoded value
        :raise
            Exception when value is not in the charset
        """
        if not value < len(Base64._CHARSET):
            raise Exception('Incorrect parameter: invalid value')

        return Base64._CHARSET[value]

    def chrMod(value: int):
        """
        Get the base64 character from the given value after applying a modulo on it
        to ensure the call will not fail
        :parameter
        value : int
            The value to convert
        :return:
            Encoded value
        """
        return Base64._CHARSET[value % len(Base64._CHARSET)]

    def encode(value: int, length: int) -> str:
        """
        Encode a int value to pseudo base64
        :parameter
        value: int
            value to encode
        length: int
            then expected result length. Must be in range [1-6]
        :return:
            the decoded value
        :raise
            Exception when the encoded string is not in range [1-6]
        """
        if length < 1 or length > 6:
            raise Exception('Incorrect parameter: l must be in range [1-6]')

        v: int = value
        result: str = ""

        for i in range(length - 1, 0, -1):
            result = str(Base64._CHARSET[v & 63]) + result
            v >>= 6

        return result

    def decode(encoded: str) -> int:
        """
        Decode pseudo base64 value to int
        :parameter
        encoded : str
            the encoded value
        :return:
            the decoded value
        :raise
            Exception when the encoded string is not in range [1-6]
        """
        if len(encoded) > 6:
            raise Exception('Incorret parameter: parameter too long')

        value: int = 0

        for c in encoded:
            value <<= 6
            value += Base64.ord(c)

        return value