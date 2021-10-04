class CheckSum:
    @staticmethod
    def integer(value: str) -> int:
        """
        Compute the checksum as in integer

        :param value: The value to compute
        :return: the checksum of the given value
        :rtype: str
        """
        csum: int = 0
        for s in value:
            csum += ord(s) % 16

        return csum % 16

    @staticmethod
    def hexadecimal(value: str) -> str:
        """
        Compute the checksum as an hexadecimal string
        The return value is a single hexadecimal char string

        :param value: The value to compute
        :return: The hexadecimal checksum of the given value
        :rtype: str
        """
        return hex(CheckSum.integer(value)).upper()

    @staticmethod
    def verify_int(input: str, expected: int) -> bool:
        """
        Verify the checksum of the input

        :param input: The value to check
        :param expected: The expected checksum as int
        :return: true if checksum match, false otherwise
        :rtype: bool
        """
        return CheckSum.integer(input) == expected

    @staticmethod
    def verify_str(input: str, expected: str) -> bool:
        """
        Verify the checksum of the input value

        :param input: The input value to check
        :param expected: The expected checksum value as an hexadecimal string
        :return: true if checksum match, false otherwise
        :rtype: bool
        """
        return CheckSum.integer(input) == int(expected, 16)
