from cryptography.fernet import Fernet

class EncryptionModule:
    def __init__(self):
        # Generate a key for encryption
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        # Encrypt data using the key
        encrypted_data = self.cipher_suite.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        # Decrypt data using the key
        decrypted_data = self.cipher_suite.decrypt(encrypted_data).decode()
        return decrypted_data

    def save_key_to_file(self, file_path):
        # Save the key to a file
        with open(file_path, 'wb') as key_file:
            key_file.write(self.key)

    def load_key_from_file(self, file_path):
        # Load the key from a file
        with open(file_path, 'rb') as key_file:
            self.key = key_file.read()
            self.cipher_suite = Fernet(self.key)
