from unittest import TestCase, main as main_function
from utils.file import (content_exists_in_file,
                        get_file_path,
                        append_content_on_file)


class TestFileModuleFunctions(TestCase):

    def setUp(self):
        pass

    def test_file_content_comparation_case_content_exists(self):
        file_content = ["hash_one", "hash_two", "hash_three"]
        content_exists = content_exists_in_file(file_content,
                                                "hash_one")

        self.assertTrue(content_exists)

    def test_file_content_comparation_case_content_doesnt_exist(self):
        file_content = ["hash_one", "hash_two", "hash_three"]
        content_doesnt_exist = content_exists_in_file(file_content,
                                                      "hash_four")

        self.assertFalse(content_doesnt_exist)

    if __name__ == '__main__':
        main_function()
