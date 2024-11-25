from pymongo import MongoClient
import json
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['time_zero_db']  # Replace with your database name
collection = db['every_logs']           # Replace with your collection name

# Define start and end time for filtering logs (optional)
start_time = datetime(2024, 11, 25, 0, 0, 0)  # Replace with your desired start time
end_time = datetime(2024, 11, 25, 23, 59, 59)  # Replace with your desired end time

# Convert datetime to ISO format for MongoDB query
start_time_iso = start_time.isoformat() + "Z"  # Add 'Z' for UTC time
end_time_iso = end_time.isoformat() + "Z"      # Add 'Z' for UTC time

# Query logs between the start and end times
logs = collection.find({
    "timestamp": {
        "$gte": start_time_iso,  # Greater than or equal to start_time
        "$lte": end_time_iso     # Less than or equal to end_time
    }
})

# Check if any logs are being retrieved
log_list = list(logs)

# Print logs to check if data is being retrieved
print(f"Retrieved {len(log_list)} logs.")
if log_list:
    print(f"Sample logs: {log_list[:5]}")  # Print the first 5 logs to check their structure

# Custom function to convert MongoDB documents to JSON serializable format
def json_serialize(document):
    document['_id'] = str(document['_id'])  # Convert ObjectId to string
    document['timestamp'] = str(document['timestamp'])  # Convert datetime to string
    return document

# If logs are found, save them to a file
if log_list:
    with open('authentication_logs.json', 'w') as file:
        # Apply the serialization function to each log entry
        json.dump([json_serialize(log) for log in log_list], file, indent=4)

    print("Logs saved to authentication_logs.json")
else:
    print("No logs found during the specified period.")
