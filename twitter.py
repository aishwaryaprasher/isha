from key import Consumer_Key,Consumer_Secret,Access_Token,AccessToken_Secret

import tweepy

oauth=tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
oauth.set_access_token(Access_Token,AccessToken_Secret)
api=tweepy.API(oauth)
print(api.search("#modi"))

user=api.get_user("aishwaryaprasher")
print(user.screen_name)
print(user.followers_count)