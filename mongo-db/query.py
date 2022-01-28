# importing librarires
from pymongo import MongoClient
import pprint
# Initiating client
client = MongoClient('mongodb+srv://tathagataraha:dfs-hello-world@cluster0.7ffec.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
# opening db

db = client.new_database
collection = db.new_collection
# sending queries to find a user with first name Giavani
res = collection.find_one({'first_name': 'Giavani'})
print("A person named Giavani:")
# printing the result of the query
pprint.pprint(res)
# sending queries to finding users with gender female
res = collection.find({'gender': 'Female'})
# printing the result of the query

print("All girls in database:")
for girl in res:
    pprint.pprint(girl)
