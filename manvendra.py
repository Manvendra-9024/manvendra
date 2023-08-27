import os
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as file:
        file.write(encrypted_data)
    return encrypted_file_path

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    decrypted_file_path = os.path.splitext(encrypted_file_path)[0]
    with open(decrypted_file_path, 'wb') as file:
        file.write(decrypted_data)
    return decrypted_file_path

def login(username, password):
    # Example implementation - Replace with your own authentication logic
    valid_username = 'admin'
    valid_password = 'password'
    
    if username == valid_username and password == valid_password:
        return True
    else:
        return False

def secure_transmission(file_path):
    # TODO: Implement secure transmission logic
    # Encrypt the file and securely send it to the recipient
    pass

def main():
    # Generate a key for encryption/decryption
    key = generate_key()

    # Prompt for user login
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    # Authenticate the user
    if login(username, password):
        print('Login successful!')
    else:
        print('Login failed. Exiting program.')
        return

    # Path to the file you want to share
    file_path = './file.txt'

    # Encrypt the file
    encrypted_file_path = encrypt_file(file_path, key)
    print('File encrypted successfully:', encrypted_file_path)

    # Securely transmit the file
    secure_transmission(encrypted_file_path)
    print('File securely transmitted.')
    
    # Prompt for the received file path
    received_file_path = input('Enter the path to the received file: ')

    # Decrypt the received file
    decrypted_file_path = decrypt_file(encrypted_file_path, key)
    print('File decrypted successfully:', decrypted_file_path)

    # TODO: Implement further processing or actions with the decrypted file

if __name__ == '__main__':
    main()
