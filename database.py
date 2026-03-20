from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["foss_db"]
collection = db["foss_tools"]