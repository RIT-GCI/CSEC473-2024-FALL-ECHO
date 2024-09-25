Noah Barnes
ndb1419@g.rit.edu
Daryl Johnson 
25 September 2024

This is a simple C2 server for a Windows machine that creates a socket on the client machine to connect back to the server on the Kali Box. 

This C2 also creates timestamped logs written to a file ("c2_client_log.txt" & "c2_server_log.txt") for report purposes. The goal is to hide the c2_client_log.txt on the machine once accessed.

The point of making it so that the client recieves request from the Kali Box and logs can be stored on both devices for most clarity. If the log file gets deleted on client device, there is still access through the one on the server.

This currently uses the metasploit port 4444

File on client is named __py__abc.py to obfuscate and hide it behind an actual lib (_py_abc)
