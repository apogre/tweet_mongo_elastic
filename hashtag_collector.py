import tweepy
import csv
from tokens import csecret, ckey, asecret, atoken
from mongo_elastic import col, es
import json


auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth, wait_on_rate_limit=True)


def update_mongo(data):
    col.insert_one(data)


def update_es(data):
    es.index(index='jtn-index', doc_type='tweets', body=data)



for tweet in tweepy.Cursor(api.search, q="#JusticeForNirmala", count=100,
                           since="2018-10-14").items():
    data = tweet._json
    # print type(data)
    try:
        update_mongo(data)
        update_es(data)
    except Exception as e:
        print e