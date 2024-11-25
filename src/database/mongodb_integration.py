from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Adjust if you have a different connection string
db = client["time_zero_db"]
collection = db["logs"]

# Load normalized data
with open("data/normalized_logs/normalized.json", "r") as file:
    normalized_data = json.load(file)

# Insert data into MongoDB
if normalized_data:
    collection.insert_many(normalized_data)
    print(f"Inserted {len(normalized_data)} records into MongoDB.")
else:
    print("No normalized data found to insert.")
