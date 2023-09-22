Using SFTP:

Open your terminal on your local machine.

Use the sftp command to establish an SFTP session with your cloud Ubuntu sandbox. Replace your.username with your username on the Ubuntu instance, and replace your.server.ip with the IP address or hostname of your Ubuntu sandbox:

sftp your.username@your.server.ip

For example:

sftp ubuntu@192.168.1.100
Once connected, you'll be in an SFTP prompt. Use the put command to upload your file to the remote server:

put /path/to/your/local/file /path/on/ubuntu/sandbox/

For example:

put ~/Desktop/myfile.txt /home/ubuntu/

After the upload is complete, use the exit command to exit the SFTP session:

exit

Your file should now be transferred to your cloud Ubuntu sandbox.
