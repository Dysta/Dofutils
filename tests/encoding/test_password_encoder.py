from unittest import TestCase

from dofutils.encoding import PasswordEncoder


class TestPasswordEncoder(TestCase):
    def test_key(self):
        self.assertEqual(
            "my super secure key", PasswordEncoder("my super secure key").key
        )

    def test_encode_simple(self):
        pe: PasswordEncoder = PasswordEncoder("my super secure key")

        self.assertEqual("0W_-MJ648321Q05YMH62SOQQ7e50RP", pe.encode("secure_password"))
        self.assertEqual("Z8a9MO5483", pe.encode("other"))

    def test_encode_too_long_password(self):
        pe: PasswordEncoder = PasswordEncoder("key")

        self.assertRaises(ValueError, pe.encode, password="too long")

    def test_decode_simple(self):
        pe: PasswordEncoder = PasswordEncoder("my super secure key")

        self.assertEqual("secure_password", pe.decode("0W_-MJ648321Q05YMH62SOQQ7e50RP"))
        self.assertEqual("other", pe.decode("Z8a9MO5483"))

    def test_decode_special_char(self):
        data: str = "é#ç@à²"
        pe: PasswordEncoder = PasswordEncoder("azertyuiop")

        encoded: str = pe.encode(data)
        self.assertEqual(data, pe.decode(encoded))

    def test_decode_complex_key(self):
        data: str = "my_secret_data"
        pe: PasswordEncoder = PasswordEncoder("é#ç@à²{ùø*µ°~§a/_.")

        encoded: str = pe.encode(data)
        self.assertEqual(data, pe.decode(encoded))

    def test_decode_invalide_data(self):
        pe: PasswordEncoder = PasswordEncoder("my super secure key")

        self.assertRaises(ValueError, pe.decode, encoded="aaa")
        self.assertRaises(ValueError, pe.decode, encoded="not base64")
        self.assertRaises(
            ValueError,
            pe.decode,
            encoded="a_string_too_long_for_the_given_key_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        )

    def test_encode_decode(self):
        pe: PasswordEncoder = PasswordEncoder("my super secure key")

        self.assertEqual("", pe.decode(pe.encode("")))
        self.assertEqual("aaa", pe.decode(pe.encode("aaa")))
        self.assertEqual("Duis blandit id", pe.decode(pe.encode("Duis blandit id")))

        encoder: PasswordEncoder = PasswordEncoder("a")
        self.assertEqual("a", encoder.decode(encoder.encode("a")))
