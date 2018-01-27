import time 
import os 
import urllib.request 
print("Welcome to the PyTunes installer!")
print("Press 1 to install PyTunes now, or 2 to exit.")
install = input("")
if install == ("1"):
    print("Downloading...")
    update = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/PyTunes.py/master/PyTunes.py') 
    response = urllib.request.urlopen(update) 
    newcode = response.read() 
    master = newcode.decode() 
    with open('install.pyd', 'w') as u: 
        u.write(master) 
        u.close 
    print('Installing...') 
    with open('install.pyd', 'r') as u: 
       with open('PyTunes.py', 'w', encoding='utf-8', newline='') as p: 
           p.write(master) 
           p.close() 
           u.close() 
           os.remove('install.pyd') 
    print('Installed! Now starting...') 
    time.sleep(2) 
    os.startfile('PyTunes.py') 
    exit()
else:
    exit()
