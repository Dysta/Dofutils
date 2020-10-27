from unittest import TestCase
from encoding.base64 import *


class TestBase64(TestCase):
    def test_ord_success(self):
        charset: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
        for i in range(len(charset)):
            self.assertEqual(i, Base64.ord(charset[i]), f"Fail with numb {i} and char {charset[i]}")

    def test_ord_invalid_param(self):
        self.assertRaises(ValueError, Base64.ord, char="#")
        self.assertRaises(ValueError, Base64.ord, char="#a")

    def test_chr(self):
        self.assertEqual('a', Base64.chr(0))
        self.assertEqual('_', Base64.chr(63))
        self.assertEqual('c', Base64.chr(2))

    def test_chr_invalid_param(self):
        self.assertRaises(ValueError, Base64.chr, value=-1)
        self.assertRaises(ValueError, Base64.chr, value=68)

    def test_chr_mod(self):
        self.assertEqual('a', Base64.chr_mod(64))
        self.assertEqual('r', Base64.chr_mod(145))
        self.assertEqual('c', Base64.chr_mod(66))

    def test_encode_single_char(self):
        self.assertEqual("cr", Base64.encode(145, 2))
        self.assertEqual("a", Base64.encode(64, 1))

    def test_encode_too_small_number_will_keep_length(self):
        self.assertEqual("aac", Base64.encode(2, 3))

    def test_encode_invalid_param(self):
        self.assertRaises(ValueError, Base64.encode, value=123, length=0)
        self.assertRaises(ValueError, Base64.encode, value=123, length=15)

    def test_decode(self):
        self.assertEqual(458, Base64.decode("hk"))

    def test_decode_empty_str(self):
        self.assertEqual(0, Base64.decode(""))

    def test_decode_tool_long_str(self):
        self.assertRaises(ValueError, Base64.decode, encoded="aaaaaaaaaaaaaaaaa")

    def test_decode_encode_two_char(self):
        self.assertEqual(741, Base64.decode(Base64.encode(741, 2)))
        self.assertEqual(951, Base64.decode(Base64.encode(951, 2)))
        self.assertEqual(325, Base64.decode(Base64.encode(325, 2)))
        self.assertEqual(769, Base64.decode(Base64.encode(769, 2)))

    def test_decode_encode_big_number(self):
        self.assertEqual("_____w", Base64.encode(-42, 6))
        self.assertEqual(-42, Base64.decode("_____w"))

        self.assertEqual("ai4qHh", Base64.encode(148965447, 6))
        self.assertEqual(148965447, Base64.decode("ai4qHh"))
