import unittest
import tempfile
import contextlib
from unittest.mock import patch

import utils.environment as environ


class TestEnvironmentModuleFunctions(unittest.TestCase):

    def setUp(self):
        self.env_tempfile = tempfile.NamedTemporaryFile('w', encoding='utf-8')
        self.env_tempfile.writelines(['KEY=some_key\n',
                                      'SECRET=some_secret\n'])
        self.env_tempfile.seek(0)

    def tearDown(self):
        self.env_tempfile.close()

    def test_get_oauth_keys_call(self):
        with patch('utils.environment.dotenv.load_dotenv') as mock_load:
            with contextlib.suppress(KeyError):
                environ.get_oauth_keys()
                mock_load.assert_called_with(dotenv_path=environ.ENV_PATH)

    def test_get_oauth_keys_with_mocked_env_path(self):
        environ.ENV_PATH = self.env_tempfile.name
        environ.OAUTH_ENVIRON_KEYS = ['KEY', 'SECRET']
        expected_tuple = ('some_key', 'some_secret')

        generated_tuple = environ.get_oauth_keys()
        self.assertCountEqual(expected_tuple, generated_tuple)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
