import time
import socketio

# Create a Socket.IO client
sio = socketio.Client()

# Connect to the WebSocket server
try:
    sio.connect('http://localhost:5000')
    print("Connected to WebSocket server.")
except Exception as e:
    print(f"Error connecting to WebSocket server: {e}")

# Send simulated log data to the server every 5 seconds
def send_log_data():
    while True:
        log_data = {
            'message': 'Simulated log data from client at ' + time.strftime('%H:%M:%S'),
            'count': time.time() % 100,  # Use time-based values
            'anomaly': 'Yes' if time.time() % 2 < 1 else 'No'  # Random anomaly flag
        }
        sio.emit('send_log_data', log_data)  # Send log data to server
        time.sleep(5)

# Run the simulated log data function
send_log_data()
