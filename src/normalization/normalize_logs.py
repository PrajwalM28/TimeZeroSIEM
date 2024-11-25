import json
import os

# Directory paths
input_dir = "data/processed_logs/"
output_file = "data/normalized_logs/normalized.json"

# Ensure output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Define a consistent schema
def normalize_log_entry(log_entry, log_type):
    normalized_entry = {
        "timestamp": log_entry.get("timestamp", "unknown"),
        "event_type": log_entry.get("event_type", log_type),
        "user": log_entry.get("user", "N/A"),
        "ip_address": log_entry.get("ip_address", "N/A"),
        "message": log_entry.get("message", ""),
    }
    return normalized_entry

# Process all JSON files
normalized_data = []
for filename in os.listdir(input_dir):
    if filename.endswith(".json"):
        log_type = filename.split("_")[0]  # e.g., 'authentication', 'kernel'
        with open(os.path.join(input_dir, filename), "r") as file:
            log_entries = json.load(file)
            print(f"Loaded {len(log_entries)} entries from {filename}")  # Debug print
            if log_entries:
                for entry in log_entries:
                    normalized_data.append(normalize_log_entry(entry, log_type))

# Check if data was added before writing to file
if normalized_data:
    with open(output_file, "w") as file:
        json.dump(normalized_data, file, indent=4)
    print(f"Normalized logs saved to {output_file}")
else:
    print("No data found to normalize.")
