import unittest
from unittest.mock import patch
from subprocess import CalledProcessError

from utils import fortunes


class TestFortuneModuleFunctions(unittest.TestCase):

    def test_get_random_fortune_calls(self):
        file_list = ['kids.dat', 'kids', 'cookies.dat', 'cookies']
        available_fortunes = ['kids', 'cookies']
        with patch('utils.fortunes.files') as mock_files:
            with patch('utils.fortunes.random') as random_mock:
                mock_files.get_file_list.return_value = file_list
                (mock_files.
                 get_fortunes_from_file_list.return_value) = available_fortunes

                fortunes._get_random_fortune()
                random_mock.choice.assert_called_with(available_fortunes)
                (mock_files
                 .get_file_list
                 .assert_called_with(fortunes.FORTUNES_FILE_PATH))
                (mock_files
                 .get_fortunes_from_file_list
                 .assert_called_with(file_list))

    def test_get_random_fortune_from_arbitray_fortunes(self):
        arbitrary_file_list = ['debian.dat', 'debian', 'love.dat', 'love']
        arbitrary_fortunes = ['debian', 'love']

        with patch('utils.fortunes.files') as files_mock:
            files_mock.get_file_list.return_value = arbitrary_file_list
            (files_mock
             .get_fortunes_from_file_list.return_value) = arbitrary_fortunes

            random_fortune = fortunes._get_random_fortune()
            self.assertTrue(random_fortune in arbitrary_fortunes)

    def test_gen_fortune_args_with_arbitrary_entry(self):
        expected_args = ['fortune', '-s', 'kids']
        arbitrary_fortune = 'kids'

        fortune_args = fortunes._gen_fortune_args(arbitrary_fortune)
        self.assertCountEqual(fortune_args, expected_args)

    def test_get_fortune_calls(self):
        with patch('utils.fortunes._get_random_fortune') as mock_get:
            with patch('utils.fortunes._gen_fortune_args') as mock_gen:
                with patch('utils.fortunes.subprocess.run') as mock_run:
                    arbitrary_fortune = 'computers'
                    mock_get.return_value = arbitrary_fortune

                    arbitrary_args = ['fortune', '-s', 'magic']
                    mock_gen.return_value = arbitrary_args

                    fortunes.get_fortune_message()
                    mock_get.assert_called_once()
                    mock_gen.assert_called_once_with(arbitrary_fortune)
                    mock_run.assert_called_once_with(arbitrary_args,
                                                     capture_output=True,
                                                     encoding='utf-8',
                                                     check=True)

    def test_get_fortune_message_raises_called_process_error(self):
        with patch('utils.fortunes._get_random_fortune'):
            with patch('utils.fortunes._gen_fortune_args') as mock_gen:
                args_with_invalid_option = ['fortune', '-z']
                mock_gen.return_value = args_with_invalid_option

                self.assertRaises(CalledProcessError,
                                  fortunes.get_fortune_message)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
