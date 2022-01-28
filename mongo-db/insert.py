# importing librarires
from pymongo import MongoClient
import json
# Initiating client
client = MongoClient('mongodb+srv://tathagataraha:dfs-hello-world@cluster0.7ffec.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
# opening db
db = client.new_database
collection = db.new_collection
# Loading data from json file
with open('data.json', 'r') as f:
    data = json.load(f)
# Inserting data into MongoDB database
collection.insert_many(data)