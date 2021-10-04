from unittest import TestCase
from dofutils.encoding import Key


class TestKey(TestCase):
    def test_cipher(self):
        key: Key = Key("my key")

        self.assertEqual("my key", key.cipher().key())
        self.assertEqual(key.cipher(), key.cipher())

    def test_key(self):
        self.assertEqual("my key", Key("my key").key())

    def test_encore(self):
        self.assertEqual("6d792b6b6579", Key("my key").encode())
        self.assertEqual("253235254333254239253430254333254130", Key("%ù@à").encode())

    def test_parse(self):
        self.assertEqual("my key", Key.parse("6d792b6b6579").key())
        self.assertEqual(
            "%ù@à", Key.parse("253235254333254239253430254333254130").key()
        )

        self.assertRaises(ValueError, Key.parse, input="invalid")
        self.assertRaises(ValueError, Key.parse, input="not hexa")

    def test_generate(self):
        self.assertEqual(128, len(Key.generate(128)))
        self.assertEqual(32, len(Key.generate(32)))

        self.assertNotEqual(Key.generate(), Key.generate())
