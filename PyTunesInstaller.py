##pytunes installer 0.4##
import time 
import os 
import urllib.request
if not os.path.exists("PyTunes.py"):
    print("Welcome to the PyTunes installer!")
    print("Press 1 to install PyTunes now, or 2 to exit.")
    install = input("")
    if install == ("1"):
        print("Downloading PyTunes...")
        update = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/PyTunes.py/master/PyTunes.py') 
        response = urllib.request.urlopen(update) 
        newcode = response.read() 
        master = newcode.decode()
        soundef1 = ('https://raw.githubusercontent.com/SimLoads/PyTunes.py/master/StartSnd.ogg')
        soundef2 = ('https://raw.githubusercontent.com/SimLoads/PyTunes.py/master/err.ogg')
        with open('installcode.pyd', 'w') as u: 
            u.write(master) 
            u.close 
        print('Installing...') 
        with open('installcode.pyd', 'r') as u: 
           with open('PyTunes.py', 'w', encoding='utf-8', newline='') as p: 
               p.write(master)
               urllib.request.urlretrieve(soundef1, 'StartSnd.ogg')
               urllib.request.urlretrieve(soundef2, 'err.ogg')
               os.system("attrib +s +h err.ogg")
               os.system("attrib +s +h StartSnd.ogg")
               p.close() 
               u.close() 
               os.remove('installcode.pyd') 
        print('Installed! Now starting...') 
        time.sleep(2) 
        os.startfile('PyTunes.py') 
        exit()
    else:
        exit()
else:
    print("PyTunes is already installed!")
    os.system("pause")
    exit()
