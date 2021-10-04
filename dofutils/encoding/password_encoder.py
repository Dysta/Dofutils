from .base64 import Base64


class PasswordEncoder:
    def __init__(self, key: str) -> None:
        """
        Construct a password_encoder object

        :param key: The key to use. Must be enough to encode the password
        """
        self._key = key

    def key(self) -> str:
        """
        Get the encoding key

        :return: the key
        :rtype: str
        """
        return self._key

    def decode(self, encoded: str) -> str:
        """
        decode the given encoded string using the key

        :param encoded: the encoded string
        :return: the decoded string in base64 format
        :raise ValueError: when the encoded string is invalid or the key is too small
        :rtype: str
        """
        if len(encoded) % 2 != 0:
            raise ValueError("Invalid encoded string")

        if len(self._key) * 2 < len(encoded):
            raise ValueError("Encoded string is too long for the key")

        decoded: list = [None for _ in range(len(encoded) // 2)]

        for i in range(0, len(encoded), 2):
            p: int = i // 2
            k: int = ord(self._key[p]) % 64

            # get two chars int value (divider and modulo)
            d: int = Base64.ord(encoded[i])
            r: int = Base64.ord(encoded[i + 1])

            # remove key value
            d -= k
            r -= k

            # if values are negative due to modulo, reverse the modulo
            while d < 0:
                d += 64
            while r < 0:
                r += 64

            # retrieve the original value
            v: int = d * 16 + r

            decoded[p] = chr(v)

        return "".join(decoded)

    def encode(self, password: str) -> str:
        """
        Encode the given password using the key

        :param password: the raw password
        :return: the encoded password
        :raise ValueError: when the password is too long
        :rtype: str
        """
        if len(self._key) < len(password):
            raise ValueError("The password is too long for the key")

        encoded: list = [None for _ in range(len(password) * 2)]

        for i in range(len(password)):
            # password char and key
            c: int = ord(password[i])
            k: int = ord(self._key[i])

            # get the divider and modulo values
            d: int = c // 16
            r: int = c % 16

            # encode into base64
            encoded[i * 2] = Base64.chr_mod(d + k)
            encoded[i * 2 + 1] = Base64.chr_mod(r + k)

        return "".join(encoded)
