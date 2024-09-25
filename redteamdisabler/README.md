Hello! This is the readme to my red team tool for CSEC 473.

This tool is meant to slow down the blue team's initial start up and provide persistence.

My tool is a powershell script that when run will:
- Disables Task Manager
- Disables CMD
- Creates Persistence for our team's C2s
- Then Disables Registry Editor
- Finally the System Event Log, Security Event Log, and Application Event logs will all be cleared

To run this script:
Open powershell in administrator mode
Run the command: "set-executionpolicy remotesigned"
Type y and hit enter
cd to folder where file was downloaded
type ".\redteamtool.ps1"
and hit enter.

*Please note that the script may produce an error as example.exe clearly is not an actual program but a stand in for an actual program*
