import sys
import os

# Add the root directory of the project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from flask import Flask, render_template
from src.web_socket.websocket_handler import socketio, start_socketio, handle_new_log_data

app = Flask(__name__)

# Initialize SocketIO
start_socketio(app)

@app.route('/')
def index():
    return render_template('index.html')  # Web interface for visualization

@socketio.on('connect')
def on_connect():
    print("Client connected")

@socketio.on('disconnect')
def on_disconnect():
    print("Client disconnected")

@socketio.on('send_log_data')
def on_send_log_data(data):
    """Receive data from simulate_log_data.py and broadcast to clients."""
    print(f"Broadcasting log data: {data}")
    handle_new_log_data(data)  # Broadcast via the 'new_log' event

if __name__ == '__main__':
    print('Starting Websocket Server...')
    socketio.run(app, host='127.0.0.1', port=5000, debug=True, use_reloader=False)
