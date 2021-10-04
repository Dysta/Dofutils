from .xor_cipher import XorCipher
from urllib.parse import urlencode, unquote_plus
from secrets import token_urlsafe
from typing import Optional


class Key:
    def __init__(self, key: str) -> None:
        self._key: str = key
        self._cipher: Optional[XorCipher] = None

    @property
    def key(self) -> str:
        """
        Return the current key used

        :return: The current key used
        :rtype: str
        """
        return self._key

    def cipher(self) -> XorCipher:
        """
        Get the cipher relative to this key.
        The cipher instance is saved into the key

        :return: The cipher instance
        :rtype: XorCipher
        """
        if self._cipher is None:
            self._cipher = XorCipher(self._key)

        return self._cipher

    def encode(self) -> str:
        """
        Encode the key to hexadecimal string

        :return: The encoded key
        :rtype: str
        """
        raw: str = urlencode({"": self._key})[1:]
        encrypted: str = ""

        for c in raw:
            if ord(c) < 16:
                encrypted += "0"

            encrypted += hex(ord(c))[2:]

        return encrypted

    def __len__(self) -> int:
        """
        Return the len of the current key used
        :return: the len of the key
        :rtype: int
        """
        return len(self._key)

    @staticmethod
    def parse(input: str) -> "Key":
        """
        Parse a hexadecimal key string

        :param input: The key to parse
        :raise ValueError: When invalid key is not even
        :return: The key instance
        :rtype: Key
        """
        if len(input) % 2 != 0:
            raise ValueError("Invalid key. Length of key must be even")

        key: list = [None for _ in range(len(input) // 2)]

        for i in range(0, len(input), 2):
            key[i // 2] = chr(int(input[i : i + 2], 16))

        return Key(unquote_plus("".join(key)))

    @staticmethod
    def generate(size: int = 128) -> "Key":
        """
        Generate a new random key

        :param size: The key size
        :return: The generated key
        :rtype: Key
        """
        return Key(token_urlsafe(size)[:size])
