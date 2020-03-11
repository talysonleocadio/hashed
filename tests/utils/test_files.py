import unittest
from unittest.mock import mock_open, patch
import tempfile

import utils.files as file_utils


class TestFileModuleFunctions(unittest.TestCase):

    def setUp(self):
        self.temp_path = tempfile.gettempdir()
        self.temp_file = tempfile.NamedTemporaryFile(mode='w+', suffix='.txt')
        self.tempfile_name = self.temp_file.name.split('/')[-1]

    def tearDown(self):
        self.temp_file.close()

    def test_file_content_comparation_where_content_exists(self):
        file_content = ["digest_one", "digest_two", "digest_three"]
        content_exists = file_utils.digest_exists_in_file(file_content,
                                                          "digest_one")

        self.assertTrue(content_exists)

    def test_file_content_comparation_where_content_doesnt_exist(self):
        file_content = ["digest_one", "digest_two", "digest_three"]
        content_exists = file_utils.digest_exists_in_file(file_content,
                                                          "digest_four")

        self.assertFalse(content_exists)

    def test_generated_file_paths_with_same_file_name(self):
        expected_file_path = self.temp_file.name
        gen_file_path = file_utils.get_absolute_file_path(self.temp_path,
                                                          self.tempfile_name)
        is_the_same_file_path = (expected_file_path == gen_file_path)

        self.assertTrue(is_the_same_file_path)

    def test_generated_file_paths_with_different_file_names(self):
        diff_file_path = f"{self.temp_path}/diff_file.txt"
        gen_file_path = file_utils.get_absolute_file_path(self.temp_path,
                                                          self.tempfile_name)
        is_the_same_file_path = (diff_file_path == gen_file_path)

        self.assertFalse(is_the_same_file_path)

    def test_append_content_to_generated_tempfile(self):
        expected_digest = "be316e4"
        file_utils.append_content_to_file(self.temp_file.name, "be316e4")

        try:
            with open(self.temp_file.name, 'r') as file:
                file.seek(0)
                end_of_file = file.readlines()[-1]
        except FileNotFoundError as error:
            print(f"Temp file does not exist: {error}")

        self.assertEqual(end_of_file, expected_digest)

    def test_wheter_file_exists_with_real_file(self):
        self.assertTrue(file_utils.file_exists(self.temp_file.name))

    def test_whter_file_exists_with_inexistent_file(self):
        self.assertFalse(file_utils.file_exists("inexistent_file.txt"))

    if __name__ == '__main__':
        unittest.main()
