import pymongo
from pymongo import MongoClient


data = {
    "name": 'mikrotik',
    "payload": 'hello'
}

# Простое подключение
client = MongoClient('mongodb://admin:password123@192.168.89.115:27017/')
databases = client.list_database_names()
db = client['PYTHON']
collection = db['test1']
collection.insert_one(data)
print(list(collection.find({}))[0])


    

