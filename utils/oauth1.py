from requests_oauthlib import OAuth1Session


def create_oauth_session(oauth_keys):
    (client_key, client_secret,
     access_key, access_secret) = oauth_keys
    return OAuth1Session(client_key,
                         client_secret=client_secret,
                         resource_owner_key=access_key,
                         resource_owner_secret=access_secret)
