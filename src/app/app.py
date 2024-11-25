from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
socketio = SocketIO(app)

# Serve the index page
@app.route('/')
def index():
    return render_template('index.html')

# WebSocket connect event
@socketio.on('connect')
def handle_connect():
    print("Client connected")
    emit('message', {'data': 'Connected to WebSocket server!'})

# WebSocket disconnection event
@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

# WebSocket event to send log data
@socketio.on('send_log_data')
def handle_send_log_data(data):
    print(f"Received log data: {data}")
    emit('new_log', data)  # Emit log data to all connected clients

# Simulate log data and send to clients every 5 seconds
def simulate_log_data():
    while True:
        log_data = {
            'message': 'Log data at ' + time.strftime('%H:%M:%S'),
            'count': time.time() % 100,
            'anomaly': 'Yes' if time.time() % 2 < 1 else 'No'
        }
        socketio.emit('new_log', log_data)  # Send log data to clients
        time.sleep(5)  # Send data every 5 seconds

# Run the Flask app with WebSocket support
if __name__ == '__main__':
    from threading import Thread
    thread = Thread(target=simulate_log_data)  # Start log data simulation in a separate thread
    thread.start()
    socketio.run(app, host='0.0.0.0', port=5000)
