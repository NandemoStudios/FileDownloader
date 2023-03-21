import requests
import time

def Download(filename, downloadlink):
    file = requests.get(downloadlink)

    filedownloaded = open(filename, 'w+')
    filedownloaded.write(file.text)
    filedownloaded.close()

# Gives the user a quick rundown of what is happening

print("Welcome to the Script Downloader")
time.sleep(.5)
print("The downloader will download the assets shortly")
time.sleep(.5)

# Downloads the file with the name installer.py from the url below

print("Installer the installer.py file")
time.sleep(.5)

Download('Installer.py', 'https://raw.githubusercontent.com/NandemoStudios/FileDownloader/main/installer.py')

print("Downlading the updater.py file")
time.sleep(.5)

Download('Updater.py', 'https://raw.githubusercontent.com/NandemoStudios/FileDownloader/main/updater.py')

time.sleep(.5)

print("Download Completed")
