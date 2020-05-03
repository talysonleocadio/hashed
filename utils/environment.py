import os
import dotenv

ENV_PATH = os.path.join(os.environ['HOME'], '.app-env')
OAUTH_ENVIRON_KEYS = ['CLIENT_KEY', 'CLIENT_SECRET',
                      'ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET']


def get_oauth_keys():
    dotenv.load_dotenv(dotenv_path=ENV_PATH)
    return tuple(os.environ[key] for key in OAUTH_ENVIRON_KEYS)
