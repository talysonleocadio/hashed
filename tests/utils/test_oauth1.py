import unittest
from unittest.mock import patch

from requests_oauthlib import OAuth1Session

from utils import oauth1


class TestOauthModuleFunctions(unittest.TestCase):

    def setUp(self):
        self.oauth_values = ('client_key', 'client_secret',
                             'access_token', 'access_token_secret')

    def test_create_oauth_session_call(self):
        with patch('utils.oauth1.OAuth1Session') as mock_OAuthSession:
            oauth1.create_oauth_session(self.oauth_values)
            (mock_OAuthSession
             .assert_called_with(self.oauth_values[0],
                                 client_secret=self.oauth_values[1],
                                 resource_owner_key=self.oauth_values[2],
                                 resource_owner_secret=self.oauth_values[3]))

    def test_create_oauth_session_object(self):
        oauth1_session = oauth1.create_oauth_session(self.oauth_values)
        self.assertIsInstance(oauth1_session, OAuth1Session)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
