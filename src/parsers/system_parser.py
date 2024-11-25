import json

def parse_system_log(input_file, output_file):
    print("Starting the system log parsing...")  # Debugging print statement to confirm script execution

    with open(input_file, "r") as file:
        raw_logs = file.readlines()

    if not raw_logs:
        print("No logs found in the input file.")  # Check if the file is empty
        return

    parsed_logs = []
    
    # Example of simple parsing (this will depend on your log format)
    for line in raw_logs:
        # For now, just print the raw line to debug
        print("Raw log line:", line)
        if line.strip():  # Skip empty lines
            parsed_log = {
                "timestamp": "2024-11-25T12:00:00Z",  # Example timestamp, adjust as per your format
                "event_type": "system",
                "user": "user1",  # Example, extract from line if possible
                "ip_address": "192.168.1.1",  # Example, extract from line if possible
                "message": line.strip(),  # Use the whole line or parts of it
            }
            parsed_logs.append(parsed_log)
    
    if parsed_logs:
        with open(output_file, "w") as outfile:
            json.dump(parsed_logs, outfile, indent=4)
        print(f"Parsed {len(parsed_logs)} logs from {input_file} and saved to {output_file}.")
    else:
        print("No logs parsed.")

# Call the parsing function (adjust the paths as needed)
parse_system_log("./data/raw_logs/system.log", "./data/processed_logs/system_parsed.json")
