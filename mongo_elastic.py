from elasticsearch import Elasticsearch
from pymongo import MongoClient


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

client = MongoClient()
col = client.local.tweets


