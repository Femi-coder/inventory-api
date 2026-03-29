from pymongo import MongoClient

MONGO_URI = "mongodb+srv://Femi:femi_123@ecowheelsdublin.zpsyu.mongodb.net/"

client = MongoClient(MONGO_URI)

db = client["inventory_db"]
collection = db["products"]