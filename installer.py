import requests

files = ['https://raw.githubusercontent.com/NandemoStudios/FileDownloader/main/Test/test.py']

downloadfiles = []

for x in range(0,len(files)):
    # Display all the files that can be downloaded
    for x in files:
        print(x)
    # Ask the user which file they want to download
    file = input('Which file do you want to download? ')
    # Check if the data is in range
    if file in files:
        # add the file to the download list
        downloadfiles.append(file)
    elif file.lower() == 'done':
        for x in downloadfiles:
            r = requests.get(x, allow_redirects=True)
            newfile = open(x.split('/')[-1], 'w+')
            newfile.write(r.text)
            newfile.close()
    else:
        print('Invalid file')
