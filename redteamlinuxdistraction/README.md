# clone-tool.yml
This ansible script is designed to run on an Ubuntu Linux distribution and download a specified github repository, modify the script's file permission, update the sshd_config file, execute a script, and remove the github folder for cleanup.<br>

Update the inventory.ini file to include the target host IP.<br>
Update `repo` and `dest` with the desired github url and destination folder. <br>
Update the `command` under `Execute task` with the desired script to run from the github repo. 

## Running playbook
In order to run the playbook run the following command in terminal: `ansible-playbook -i inventory.ini clone-repo.yml`


# sneakytool.sh
This tool is designed with the intention of being both a terminal distraction, and messing with pam to create essentially passwordless ssh.<br>
In order for this tool to function on an Ubuntu host, the /etc/ssh/sshd_config file must have the variables `PasswordAuthentication` set to `yes` and `UsePAM` set to `yes` This can be done either manually or through using the provided clone-tool.yml ansible script.<br>
This tool also has included, commented out, commands that edit the mangle table in order to drop all traffic once per hour as a cronjob. 

## Running the tool
This bash script needs to be run with sudo privileges, or ran via the Ansible script `clone-tool.yml`

## Post running script
In order to ssh into the box from another box, you will no longer need to enter the correct password, however the entered password cannot be empty. 