from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["foss_db"]
collection = db["foss_tools"]

# Load JSON file
with open("data.json", "r") as file:
    data = json.load(file)

# Insert into DB
collection.delete_many({})  # clears old data (optional)
collection.insert_many(data)

print("✅ Data successfully inserted into MongoDB!")