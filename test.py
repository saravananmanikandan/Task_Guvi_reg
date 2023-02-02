
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://saravanan:saravanan123@cluster0.uasf7s8.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Reg_guvi"]
collection = db["users"]

post = {"_id":0, "name":"saravanan", "score":5}

collection.insert_one({post})