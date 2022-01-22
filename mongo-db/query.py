from pymongo import MongoClient
import pprint
client = MongoClient('mongodb+srv://tathagataraha:dfs-hello-world@cluster0.7ffec.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.new_database
collection = db.new_collection
res = collection.find_one({'first_name': 'Giavani'})
print("A person named Giavani:")
pprint.pprint(res)
res = collection.find({'gender': 'Female'})
print("All girls in database:")
for girl in res:
    pprint.pprint(girl)
