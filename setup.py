import requests

print("Welcome to the Script Downloader")
print("The downloader will download the assets shortly")

filefound = requests.get("https://raw.githubusercontent.com/NandemoStudios/FileDownloader/main/installer.py")

Installer = open("Installer.py", "w+")
Installer.write(filefound.text)
Installer.close()

print("Download Completed")
