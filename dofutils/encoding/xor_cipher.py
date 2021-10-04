from urllib.parse import quote, unquote


class XorCipher:
    def __init__(self, key: str) -> None:
        self._key = key

    @property
    def key(self) -> str:
        """
        Return the key

        :return: the key used by the xor cipher
        :rtype: str
        """
        return self._key

    def encrypt(self, value: str, key_offset: int) -> str:
        """
        Encrypt the given value with the current xor cipher key
        The encrypted value is an upper case hexadecimal string

        :param value: Value to encrypt
        :param key_offset: Offset to use for the key
        :return: Encrypted value
        :rtype: str
        """
        evalue: str = XorCipher._escape(value)
        encrypted: str = ""

        for i in range(len(evalue)):
            c: int = ord(evalue[i])
            k: int = ord(self._key[(i + key_offset) % len(self._key)])

            e: str = chr(c ^ k)
            if ord(e) < 16:
                encrypted += "0"

            encrypted += hex(ord(e))[2:]

        return encrypted.upper()

    def decrypt(self, value: str, key_offset: int) -> str:
        """
        Decrypt the given value by using the key

        :param value: The value to decrypt. Must be an hexadecimal string
        :param key_offset: Offset to use on the key. Must be the same used for encryption
        :raise ValueError: When encrypted value is not odd
        :return: The decrypted value
        :rtype: str
        """
        if len(value) % 2 != 0:
            raise ValueError("Invalid encrypted value. Value must be odd")

        decrypted: list = [None for _ in range(len(value) // 2)]

        for i in range(0, len(value), 2):
            p: int = (i // 2 + key_offset) % len(self._key)
            k: int = ord(self._key[p])
            c: int = int(value[i : i + 2], 16)

            decrypted[i // 2] = chr(c ^ k)

        return unquote("".join(decrypted))

    @staticmethod
    def _escape(value: str) -> str:
        """
        Escape the given value using URLEncode

        :param value: the value to escape
        :return: the escaped value
        :rtype: str
        """
        escaped: str = ""

        for i in value:
            c: int = ord(i)
            if c < 32 or c > 127 or i == "%" or i == "+":
                escaped += quote(i)
            else:
                escaped += i

        return escaped
