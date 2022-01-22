from pymongo import MongoClient
import json
client = MongoClient('mongodb+srv://tathagataraha:dfs-hello-world@cluster0.7ffec.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.new_database
collection = db.new_collection
with open('data.json', 'r') as f:
    data = json.load(f)
collection.insert_many(data)