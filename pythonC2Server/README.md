Welcome to the C2 Red Team Tool README file!
This file will cover important info regarding the tool, and how to use it.
This tool can be used to execute commands on a remote host.

To begin using this tool, be sure to run files in the following order:

NOTE: These files should all be located in the /etc/ansible directory. Also, all of these scripts will be run on the client machine.

#1 run the the c2_server_transfer_tool.yaml file.
#2 run the c2_server_execute_tool.yaml file.(run both of these two scripts on the same terminal).

#3 run the c2_client.py file, from another terminal on the cient machine.
#4 you should now be connected, and be able to give commands to be executed on the remote host.

Several commands you can use include the follwing: "ls", "ls -l", "ss -tan state established", etc.

NOTE: Make sure to run the scripts in the order given. If you do not, then the connection between the host and client will not get established.
