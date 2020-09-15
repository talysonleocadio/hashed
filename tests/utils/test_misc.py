import unittest
import contextlib
from unittest.mock import patch

from utils import misc


class TestMiscModuleFunctions(unittest.TestCase):

    def test_print_and_exit_print_call(self):
        with patch('utils.misc.print') as print_mock:
            with contextlib.suppress(SystemExit):
                exit_message = 'exiting program'
                misc.print_and_exit(exit_message)
                print_mock.assert_called_once_with(exit_message)

    def test_print_and_exit_raise_system_exit(self):
        with self.assertRaises(SystemExit):
            misc.print_and_exit('exit message')


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
