import unittest
from utils.hashing import _convert_from_string_to_byte, sha1_hex_digest


class HashingTest(unittest.TestCase):

    def setUp(self):
        self.string = "bytes!"

    def test_convert_from_unicode_to_byte(self):
        byte_obj = b"bytes!"
        converted_string = _convert_from_string_to_byte(self.string)
        self.assertEqual(byte_obj,
                         converted_string,
                         "Byte objects dont match")

    def test_sha1_hex_digest(self):
        hex_digest = sha1_hex_digest(self.string)
        self.assertEqual(hex_digest,
                         "9d1cf02da81f072e2b08b9c78ba4e07af997b205",
                         "Digests dont match")

    if __name__ == '__main__':
        unittest.main()




