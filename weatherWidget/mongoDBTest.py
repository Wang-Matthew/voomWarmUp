import pymongo
from pymongo import MongoClient
import certifi
import pprint

cluster = MongoClient("mongodb+srv://mattWang:zoomVoomZOOM!1@cluster0.8blkad4.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = cluster["widgets"]
collection = db["weather"]

results = collection.find_one()
pprint.pprint(results)