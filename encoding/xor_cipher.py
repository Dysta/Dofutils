from urllib.parse import escape

class xor_cipher:
    def __init__(self, key: str) -> None:
        self._key = key

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
        :return: Enrypted value
        :rtype: str
        """
        evalue: str = xor_cipher._escape(value)
        encrypted: str = ""

        for i in range(len(evalue)):
            c: int = ord(evalue[i])
            k: int = ord(self._key[(i + key_offset) % len(self._key)])

            e: str = chr(c ^ k)
            if ord(e) < 16:
                encrypted += '0'
            
            encrypted += str(hex(ord(e)))

        return encrypted.upper()

    def decrypt(self, value: str, key_offset: int) -> str:
        """
        Decrypt the given value by using the key

        :param value: The value to decrypt. Must be an hexadecimal string
        :param key_offset: Offset to use on the key. Must be the same used for encryption
        :return: The decrypted value
        :rtype: str
        """
        if len(value) % 2 == 0:
            raise Exception('Incorrect parameter: Invalid encrypted value')

        decrypted: str = ""

        for i in range(1, len(value), 2):
            k: int = ord(self._key[i // 2 + key_offset] % len(self._key))
            c: int = int(value[i:i+2], 16)

            decrypted[i // 2] = chr(c ^ k)
        
        return decrypted
    
    def _escape(value: str) -> str:
        """
        Escape the given value using URLEncode

        :param value: the value to escape
        :return: the escaped value
        :rtype: str
        """
        escaped: str = ""

        for i in range(len(value)):
            c: int = ord(value[i])
            if c < 32 or c > 127 or c == ord('%') or c == ord('+'):
                escaped += escape(chr(c))
            else:
                escaped += chr(c)

        return escaped 
