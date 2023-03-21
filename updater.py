import requests
import time

def CheckForUpdate(filename, url):
    filecheck = requests.get(url)
    file = open(filename, 'rb')

    if file.read() != filecheck.text:
        print("the file"+filename+' Needs updating')
        file.close()
        file = open(filename, 'w')
        file.write(filecheck.text)
        file.close()
        print("the file"+filename+" Has been updated")
    else:
        file.close()

CheckForUpdate('Installer.py', 'https://raw.githubusercontent.com/NandemoStudios/FileDownloader/main/installer.py')
time.sleep(.5)
CheckForUpdate('Updater.py', 'https://raw.githubusercontent.com/NandemoStudios/FileDownloader/main/updater.py')
time.sleep(.5)
CheckForUpdate('Setup.py', 'https://raw.githubusercontent.com/NandemoStudios/FileDownloader/main/setup.py')
