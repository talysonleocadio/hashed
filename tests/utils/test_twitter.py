import unittest
from unittest.mock import Mock

from utils import twitter


class TestTwitterModuleFunctions(unittest.TestCase):

    def test_verify_oauth_credentials_call(self):
        mock_session = Mock()
        expect_url = f'{twitter.BASE_URL}/account/verify_credentials.json'

        twitter.verify_oauth_credentials(mock_session)
        mock_session.get.assert_called_with(expect_url)

    def test_post_fortune(self):
        mock_session = Mock()
        status = 'some fortune'
        expect_url = (f'{twitter.BASE_URL}/statuses/update.json'
                      f'?status={status}')

        twitter.post_fortune(mock_session, status)
        mock_session.post.assert_called_with(expect_url)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
