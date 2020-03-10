from unittest import TestCase, main as main
from utils.files import (digest_exists_in_file,
                         get_absolute_file_path,
                         file_exists,
                         append_content_to_file)
from tempfile import NamedTemporaryFile, gettempdir


class TestFileModuleFunctions(TestCase):

    def setUp(self):
        self.temp_path = gettempdir()
        self.temp_file = NamedTemporaryFile(mode='w+', suffix='.txt')
        self.tempfile_name = self.temp_file.name.split('/')[-1]

    def test_file_content_comparation_where_content_exists(self):
        file_content = ["digest_one", "digest_two", "digest_three"]
        content_exists = digest_exists_in_file(file_content,
                                               "digest_one")

        self.assertTrue(content_exists)

    def test_file_content_comparation_where_content_doesnt_exist(self):
        file_content = ["digest_one", "digest_two", "digest_three"]
        content_exists = digest_exists_in_file(file_content,
                                               "digest_four")

        self.assertFalse(content_exists)

    def test_generated_file_paths_with_same_file_name(self):
        expected_file_path = os.join(self.temp_path, self.tempfile_name)
        gen_file_path = get_absolute_file_path(self.temp_path,
                                               self.tempfile_name)
        is_the_same_file_path = (expected_file_path == gen_file_path)

        self.assertTrue(is_the_same_file_path)

    def test_generated_file_paths_with_different_file_names(self):
        diff_file_path = os.path.join(self.temp_path, "text_list.txt")
        gen_file_path = get_absolute_file_path(self.temp_path,
                                               self.tempfile_name)
        is_the_same_file_path = (diff_file_path == gen_file_path)

        self.assertFalse(is_the_same_file_path)

    if __name__ == '__main__':
        main()