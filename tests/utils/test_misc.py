import unittest
import contextlib
from unittest.mock import patch

import click

from utils import misc


class TestMiscModuleFunctions(unittest.TestCase):

    def test_open_twitter_rules_call(self):
        with patch('utils.misc.webbrowser.open_new_tab') as web_mock:
            misc.open_twitter_rules()
            web_mock.assert_called_once_with(misc.TWITTER_RULES_URL)

    def test_print_and_exit_print_call(self):
        with patch('utils.misc.print') as print_mock:
            with contextlib.suppress(SystemExit):
                exit_message = 'exiting program'
                misc.print_and_exit(exit_message)
                print_mock.assert_called_once_with(exit_message)

    def test_print_and_exit_raise_system_exit(self):
        with self.assertRaises(SystemExit):
            misc.print_and_exit('exit message')

    def test_prompt_wrapper_click_prompt_call(self):
        with patch('utils.misc.click.prompt') as mock_prompt:
            prompt_msg = 'its a prompt message'
            default_value = 'y'

            misc.prompt_wrapper(prompt_msg, default_value)
            mock_prompt.assert_called()


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
