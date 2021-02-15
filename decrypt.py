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
    try:
        f = Fernet(key)
        subdirs = [x[0] for x in os.walk(dir)]
        for dirdir in subdirs:
            for filename in glob.glob(os.path.join(dirdir, '*.*'), recursive=True):
                with open(filename, "rb") as file:
                    encrypted_data = file.read()
                decrypted_data = f.decrypt(encrypted_data)
                with open(filename, "wb") as file:
                    file.write(decrypted_data)
    except:
        pass

key = load_key()
dir = "fichiers"
decrypt(dir, key)
