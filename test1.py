import pymongo

client = pymongo.MongoClient("mongodb+srv://abhishek_mongo:Mongodbcloud@cluster0.ueuvsgs.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)