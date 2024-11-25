import json
from flask_socketio import SocketIO, emit

# Initialize SocketIO instance
socketio = SocketIO()

def start_socketio(app):
    """Function to initialize SocketIO with the Flask app"""
    socketio.init_app(app)

def handle_new_log_data(data):
    """Function to handle new log data and send to WebSocket clients"""
    print(f"Received new log data: {data}")
    emit('new_log', data)  # Emit new log data to clients
