# Advanced_Keylogger
Overview

The Advanced Keylogger with System Monitoring and Encryption is a Python-based project designed to monitor and collect user activity, system data, clipboard content, and audio recordings for cybersecurity research and ethical hacking purposes. The project also integrates Fernet encryption to secure collected data and an email reporting system to send encrypted log files to authorized recipients.

Important Note: This project is intended for ethical hacking and cybersecurity research only. It should not be used for illegal activities. Make sure you have permission to use it on any systems.

Features

Keylogging: Captures every keystroke made by the user.
System Monitoring: Collects system information such as:
Hostname, IP addresses (both public and private)
System and processor details
Clipboard Monitoring: Captures the clipboard content.
Audio Recording: Records audio from the system's microphone for a set duration.
Screenshot Capture: Takes periodic screenshots of the system's screen.
Data Encryption: Uses Fernet encryption to secure sensitive log data.
Automated Reporting: Sends encrypted data files via email to a designated address.
File Cleanup: Automatically deletes logs and screenshots after the data has been sent.
Prerequisites

Before using the project, ensure you have the following dependencies installed:

Python 3.x
Libraries:
pynput (for keylogging)
pywin32 (for clipboard access)
scipy (for audio recording)
sounddevice (for audio recording)
cryptography (for encryption)
requests (for fetching public IP)
Pillow (for screenshot capture)
smtplib (for sending emails)
platform (for system information)
socket (for IP address information)
You can install the required libraries using pip:

![image](https://github.com/user-attachments/assets/8fb83ab4-5598-4bd0-8e1b-23cae18cded8)



Usage

Setting up the project:

Clone or download the repository to your local machine.
Navigate to the project directory.
Configuration:

Open the keylogger.py file and set up the following configurations:
email_address: Your email address (the sender).
password: The password of the email account (for authentication with the SMTP server).
toaddr: The recipient's email address (where logs will be sent).
key: The secret key used for encryption (you can generate it using GenerateKey.py).
Customize the directory paths as needed for storing log files and data.
Running the Program:

Execute keylogger.py in your terminal or command prompt:

![image](https://github.com/user-attachments/assets/4d45cf97-5dab-47da-b932-b626d93b7fee)



The script will start recording the user's activity, take periodic screenshots, record audio, and capture clipboard content. The data will be saved locally, encrypted, and sent via email automatically.
Stopping the Program:

To stop the program, press ESC on your keyboard or let the script run its course.
Data Encryption:

The collected data (e.g., system info, key logs, clipboard content) will be encrypted using the provided Fernet encryption key.
You can decrypt the files using the DecryptFile.py script.
Important Notes

Ethical Use Only: This tool is intended for educational, ethical hacking, and cybersecurity research purposes only. Do not use it on unauthorized systems.
Email Security: This script uses Gmail’s SMTP server for sending emails. Make sure to enable "Less Secure Apps" or use an App Password if 2FA is enabled.
Encryption: The data collected by this tool is encrypted using Fernet to ensure privacy and security. Only the correct decryption key can unlock the data.
How to Generate an Encryption Key
To generate your own Fernet encryption key, run the GenerateKey.py script:

![image](https://github.com/user-attachments/assets/cd24a70d-8176-4023-bd0f-cdbfde1a6159)



This will generate a key and save it in the file encryption_key.txt.

How to Decrypt Files

To decrypt the encrypted log files, use the DecryptFile.py script. The following example shows how to decrypt the encrypted files:

Open the DecryptFile.py file and set the correct decryption key.
Run the script:

![Screenshot 2025-02-28 061806](https://github.com/user-attachments/assets/293bf196-24a0-46fe-8375-6b80fd157fcc)



The encrypted files (e_key_log.txt, e_systeminfo.txt, e_clipboard.txt) will be decrypted and saved in the same directory.

Contributing

If you'd like to contribute to the project, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature-name).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-name).
Create a pull request.
License

This project is open-source and available under the MIT License.

Disclaimer

This tool is intended strictly for educational purposes. Misuse of this tool for unauthorized access or malicious activities is illegal. The author assumes no responsibility for the misuse of this project. Always ensure that you have explicit permission before testing or deploying this software.

