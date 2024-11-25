import pandas as pd
from sklearn.ensemble import IsolationForest
import json

# Load the logs (assuming you already have the file in a dataframe 'df')
df = pd.read_json('data/query_results/authentication_logs.json')

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract relevant features for anomaly detection
# For example, analyze the message frequency or event_type occurrences
message_counts = df['message'].value_counts().reset_index()
message_counts.columns = ['message', 'count']

# Ensure there are enough different messages to detect anomalies
print(f"Number of unique messages: {message_counts.shape[0]}")

# Detect anomalies based on the message frequency
model = IsolationForest(contamination=0.1)  # Set contamination for testing purposes
message_counts['anomaly'] = model.fit_predict(message_counts[['count']])

# Print message frequencies with detected anomalies
print("Message Counts with Anomalies:", message_counts)

# Return anomalous messages (those with anomaly == -1)
anomalous_messages = message_counts[message_counts['anomaly'] == -1]
print("Detected Anomalies in Message Frequency:", anomalous_messages)

# Save the anomalies to a JSON file (if you want to keep them saved)
with open('anomalous_messages.json', 'w') as f:
    json.dump(anomalous_messages.to_dict(orient='records'), f, indent=4)

# If you want to check by event_type or other fields, you can group them similarly:
event_counts = df['event_type'].value_counts().reset_index()
event_counts.columns = ['event_type', 'count']

# Detect anomalies in event types
event_counts['anomaly'] = model.fit_predict(event_counts[['count']])
print("Event Type Counts with Anomalies:", event_counts)

# Return anomalous event types
anomalous_events = event_counts[event_counts['anomaly'] == -1]
print("Detected Anomalies in Event Types:", anomalous_events)

# Save the anomalous events to a JSON file
with open('anomalous_events.json', 'w') as f:
    json.dump(anomalous_events.to_dict(orient='records'), f, indent=4)
