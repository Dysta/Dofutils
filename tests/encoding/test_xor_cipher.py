from unittest import TestCase

from dofutils.encoding import XorCipher


class TestXorCipher(TestCase):
    def test_key(self):
        self.assertEqual("my key", XorCipher("my key").key)

    def test_encrypt(self):
        cipher: XorCipher = XorCipher("my key")

        self.assertEqual(
            "251C4C070A593A16520701594C", cipher.encrypt("Hello World !", 0)
        )
        self.assertEqual("251C4C070A59271648054558", cipher.encrypt("Hello John !", 0))
        self.assertEqual("483A134E2440483A134E2449", cipher.encrypt("éà", 0))
        self.assertEqual("230015011600210A11035901", cipher.encrypt("Hello John !", 3))
        self.assertEqual(
            "271104091D003C0A0B03104844",
            XorCipher("other key").encrypt("Hello World !", 0),
        )

    def test_decrypt(self):
        cipher: XorCipher = XorCipher("my key")

        self.assertRaises(ValueError, cipher.decrypt, value="invalid", key_offset=0)
        self.assertRaises(ValueError, cipher.decrypt, value="####", key_offset=0)

        self.assertEqual(
            "Hello World !", cipher.decrypt("251C4C070A593A16520701594C", 0)
        )
        self.assertEqual("Hello John !", cipher.decrypt("251C4C070A59271648054558", 0))

        self.assertNotEqual(
            "Hello World !",
            XorCipher("other key").decrypt("251C4C070A593A16520701594C", 0),
        )

    def test_key_offset(self):
        c1: XorCipher = XorCipher("abcd")
        c2: XorCipher = XorCipher("cdab")

        self.assertEqual(c1.encrypt("Hello World !", 2), c2.encrypt("Hello World !", 0))
        self.assertEqual("Hello World !", c2.decrypt(c1.encrypt("Hello World !", 2), 0))

    def test_encrypt_decrypt(self):
        cipher: XorCipher = XorCipher("my key")

        strings: list = ["Hello World !", "%%%%", "", "éà@_9èè£$ø*µ+"]

        for s in strings:
            self.assertEqual(s, cipher.decrypt(cipher.encrypt(s, 0), 0))
