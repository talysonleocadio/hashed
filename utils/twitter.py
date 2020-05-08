
BASE_URL = 'https://api.twitter.com/1.1'


def verify_oauth_credentials(session):
    credentials_url = f'{BASE_URL}/account/verify_credentials.json'
    return session.get(credentials_url).ok


def post_fortune(session, fortune_msg):
    post_url = f'{BASE_URL}/statuses/update.json?status={fortune_msg}'
    return session.post(post_url)

