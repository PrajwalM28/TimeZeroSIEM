from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI if hosted elsewhere
db = client["time_zero_db"]

# Insert anomalous messages
with open("data/anomalies/anomalous_messages.json", "r") as f:
    anomalous_messages = json.load(f)
    db.anomalous_messages.insert_many(anomalous_messages)

# Insert anomalous events
with open("data/anomalies/anomalous_events.json", "r") as f:
    anomalous_events = json.load(f)
    db.anomalous_events.insert_many(anomalous_events)

print("Anomalies successfully inserted into MongoDB.")
