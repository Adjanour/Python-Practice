import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

client = MongoClient(os.getenv("MONGO"))

db = client["inventory_management"]
if "products" in db.list_collection_names():
    print("Connected to MongoDB successfully!")
else:
    print("Failed to connect to MongoDB. Please check your connection settings.")