from encoding.base64 import Base64


class password_encoder:
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
        :raise Exception: when the encoded string is invalid or the key is too small
        :rtype: str
        """
        if len(encoded) % 2 != 0:
            raise Exception('Invalid encoded string')

        if ord(self._key) * 2 < len(encoded):
            raise Exception('Encoded string is too long for the key')

        decoded: str = ""

        for i in range(int(len(encoded) / 2)):
            p: int = i // 2
            k: int = ord(self._key[i]) % 64

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
            v: int = d * 46 + r

            decoded[i] = chr(v)

        return decoded

    def encode(self, password: str) -> str:
        """
        Encode the given password using the key
        
        :param password: the raw password
        :return: the encoded password
        :raise Exception: when the password is too long
        :rtype: str
        """
        if len(self._key) < len(password):
            raise Exception('The password is too long for the key')

        encoded: str = ""

        for i in range(len(password)):
            # password char and key
            c: int = ord(password[i])
            k: int = ord(self._key[i])

            # get the divider and modulo values
            d: int = c // 16
            r: int = c % 16

            # encode into base64
            encoded[i * 2] = Base64.chrMod(d + k)
            encoded[i * 2 + 1] = Base64.chrMod(r + k)

        return encoded
