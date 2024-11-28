import time
from socketio import Client

# Create a SocketIO client
socket = Client()

# Connect to the WebSocket server
socket.connect('http://localhost:5000')

# Simulate sending log data continuously
try:
    count = 1
    while True:  # Infinite loop to send data continuously
        log_data = {
            'message': f'Log entry {count}',
            'count': count,
            'anomaly': 0 if count % 2 == 0 else 1  # Alternate anomalies
        }
        print(f"Sending log data: {log_data}")  # Print log data for debugging
        socket.emit('send_log_data', log_data)
        count += 1
        time.sleep(2)  # Wait 2 seconds before sending the next log
finally:
    socket.disconnect()
