from flask_socketio import SocketIO, emit

# Initialize SocketIO
socketio = SocketIO()

def start_socketio(app):
    """Attach the SocketIO instance to a Flask app."""
    socketio.init_app(app)

def handle_new_log_data(data):
    """Process incoming log data and emit to clients."""
    print(f"Received log data: {data}")
    socketio.emit('new_log', data)  # Broadcast log data to clients
