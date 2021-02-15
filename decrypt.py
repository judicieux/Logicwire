from cryptography.fernet import Fernet
import glob
import os

def load_key():
    """
    Charge la clé
    """
    a = input("Key: ")
    return a.encode()

def decrypt(dir, key):
    global decrypted_data
    f = Fernet(key)
    for filename in glob.glob(os.path.join(dir, '*.txt')):
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(filename, "wb") as file:
            file.write(decrypted_data)

key = load_key()
dir = "fichiers"
decrypt(dir, key)