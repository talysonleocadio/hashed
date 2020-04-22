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

    def test_append_content_to_file_call(self):
        expected_digest = "be316e4"
        open_mock = mock_open()

        with patch('utils.files.open', open_mock):
            file_utils.append_content_to_file(self.temp_file.name,
                                              expected_digest)

        open_mock.assert_called_with(self.temp_file.name, 'a+')
        open_mock.return_value.write.assert_called_with(expected_digest)

    def test_read_content_from_file_call(self):
        open_mock = mock_open()
        file_utils.HASH_FILE_PATH = self.temp_file.name
        with patch('utils.files.open', open_mock):
            file_utils.get_file_content()

        open_mock.assert_called_with(self.temp_file.name, 'r')

    def test_read_content_from_inexistent_file(self):
        file_utils.HASH_FILE_PATH = 'inexistent_file.txt'
        self.assertRaises(FileNotFoundError,
                          file_utils.get_file_content)

    def test_get_fortunes_from_file_list(self):
        file_list = ['debian', 'debian.dat', 'kids', 'kids.dat']
        expected_fortunes = ['debian', 'kids']

        fortunes = file_utils.get_fortunes_from_file_list(file_list)
        self.assertCountEqual(fortunes, expected_fortunes)

    def test_hash_file_exists_with_mocked_path(self):
        with patch('utils.files.HASH_FILE_PATH', self.temp_file.name):
            hash_file_exists = file_utils.hash_file_exists()
            self.assertTrue(hash_file_exists)

    def test_hash_file_exists_os_module_call(self):
        with patch('utils.files.os.path.isfile') as mock_os:
            file_utils.hash_file_exists()
            mock_os.assert_called_with(file_utils.HASH_FILE_PATH)

    def test_get_file_list(self):
        files = file_utils.get_file_list(self.temp_path)
        self.assertTrue(self.tempfile_name in files)

    if __name__ == '__main__':
        unittest.main()  # pragma: no cover
