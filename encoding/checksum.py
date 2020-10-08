class checksum:
    def integer(value: str) -> int:
        """
        Compute the checksum as in integer

        :param value: The value to compute
        :return: the checksum of the given value
        """
        csum: int = 0
        for s in value:
            csum += ord(s) % 16

        return csum % 16

    def hexadecimal(value: str) -> str:
        """
        Compute the checksum as an hexadecimal string
        The return value is a single heacedimal char string
        :param value: The value to compute
        :return:
            The hexadecimal checksum of the given value
        :rtype str
        """
        return hex(checksum.integer(value)).upper()

    def verify_int(input: str, expected: int) -> bool:
        """
        Verify the checksum of the input

        :param input: The value to check
        :param expected: The expected checksum as int
        :return: true if checksum match, false otherwise
        """
        return checksum.integer(input) == expected

    def verify_str(input: str, expected: str) -> bool:
        """
        Verify the checksum of the input value

        :param input: The input value to check
        :param expected: The expected checksum value as an hexadecimal string
        :return: true if checksum match, false otherwise
        """
        return checksum.integer(input) == int(expected, 16)
