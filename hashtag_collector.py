import tweepy
import csv
from tokens import csecret, ckey, asecret, atoken


auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth, wait_on_rate_limit=True)


for tweet in tweepy.Cursor(api.search, q="#JusticeForNirmala", count=100,
                           lang="en",
                           since="2018-10-13").items():
    print (tweet)