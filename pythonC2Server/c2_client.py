##########################################################################
#Name: Nicholas Milonni
#Date: 9/20/2024
#Course: CSEC 473
#Semester: Fall 2024

#This file contains a C2 Server Client. It is mean to be used
#in a red team role. It goes hand and hand with the server file.
##########################################################################

import socket

'''This function starts the C2 server client.
'''
def client(host, port):
    print("The C2 Server Client Has Started.")
    new_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Trying to connect to the host:
    connect_tuple = (host, int(port))
    new_client.connect(connect_tuple) #establishing a connection with the host.

    print("Connection Established on Port: " + str(port) + " and on host: " + host)
    continue_response = True
    while continue_response:
        usr_input = input("Use Command: ")
        if usr_input == "end":
            print("Shutting down the C2 client.")
            new_client.close()
            exit()

        #Sending the commands entered by the user to the server,
        #as well as obtaining and printing the outputs/results:
        new_client.send(usr_input.encode())
        result = new_client.recv(1024).decode()
        print(result)

'''This function allows for the client
   function to be called.
'''
def main():
    host = "100.65.3.0"
    port = 47
    client(host, port) #calling the client to start.

main()
