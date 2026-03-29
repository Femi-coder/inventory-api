import pandas as pd
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://Femi:femi_123@ecowheelsdublin.zpsyu.mongodb.net/"

client = MongoClient(MONGO_URI)

db = client["inventory_db"]
collection = db["products"]

# Read CSV
df = pd.read_csv("products.csv")

# Convert to JSON
data = df.to_dict(orient="records")

# Insert data
collection.insert_many(data)

print("Data successfully inserted into MongoDB Atlas!")