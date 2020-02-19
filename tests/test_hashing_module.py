from unittest import TestCase, main as main_function
from utils.hashing import _convert_from_string_to_byte, sha1_hex_digest


class TestHashingModuleFunctions(TestCase):

    def setUp(self):
        self.string = "bytes!"

    def test_string_convertion_to_byte_object(self):
        expected_byte_obj = b"bytes!"
        byte_object = _convert_from_string_to_byte(self.string)

        self.assertEqual(expected_byte_obj,
                         byte_object,
                         "Byte objects dont match!")

    def test_different_byte_objects_dont_match(self):
        byte_object = _convert_from_string_to_byte(self.string)
        different_byte_obj = b"is not bytes!"

        self.assertNotEqual(different_byte_obj,
                            byte_object,
                            "Byte objects are equal!")

    def test_sha1_hex_digest_generation(self):
        digest = sha1_hex_digest(self.string)
        expected_digest = "9d1cf02da81f072e2b08b9c78ba4e07af997b205"

        self.assertEqual(digest,
                         expected_digest,
                         "Digests dont match!")

    def test_different_digests_dont_match(self):
        digest = sha1_hex_digest(self.string)
        different_string = "is not bytes!"
        different_digest = sha1_hex_digest(different_string)

        self.assertNotEqual(digest,
                            different_digest,
                            "Digests are equal!")

    if __name__ == '__main__':
        main_function()
