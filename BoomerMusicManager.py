import os
import eyed3
import shutil
from datetime import datetime
from datetime import date

fulllist=[]

# The initial and target directory
MediaHuman = 'C:\\Users\Ja\Downloads\MediaHuman\Music'
Music = 'C:\\Users\Ja\Music'

# Builds a list of new and existing media
listMH = os.listdir(MediaHuman)
listMU = os.listdir(Music)
print('List of new tracks:')
for file in listMH:
    if file.endswith('.mp3')
        print(file)

# Makes a 2D list of relevant track metadata
os.chdir(MediaHuman)
for file in listMH:
    if file.endswith('.mp3')
        # Load metadata each new file
        audiofile = eyed3.load(file)
        artist = audiofile.tag.artist
        album = audiofile.tag.album
        # Builds a list where [0] is artist, [1] is album and [2] is filename
        filedata = [artist, album, file]
        fulllist.append(filedata)

print('List of all track metadata:')
print(fulllist)


for element in fulllist:
    os.chdir(Music)

    # Checks for illegal characters in the metadata
    ArtistSafe = element[0].replace('/', '-')
    AlbumSafe = element[1].replace('/', '-')
    ArtistSafe = ArtistSafe.replace('ö', 'o')

    # Checks if the artist already has a legal designated folder and makes one if not
    if ArtistSafe not in listMU:
        os.mkdir(ArtistSafe)
    artistfolder = Music + '\\' + ArtistSafe
    os.chdir(artistfolder)
    print('Current directory is ' + os.getcwd())

    # Checks if the album already has a legal designated folder and makes one if not
    if AlbumSafe not in os.listdir(artistfolder):
        os.mkdir(AlbumSafe)
    os.chdir(artistfolder + '\\' + AlbumSafe)

    # Moves the new file into the correct directory
    print('Current directory is ' + os.getcwd())
    shutil.move(MediaHuman + '\\' + element[2], os.getcwd() + '\\' + element[2])                      


# Leaves a timestamped log of moved media in the initial directory (Add date to timestamp)
os.chdir(MediaHuman)
# Build and apply timestamp to log
today = date.today()
now = datetime.now()
current_time = now.strftime(today + "%H-%M-%S")
# Populate log
f = open(current_time,"w+")
f.write('List of moved tracks:')
for element in fulllist:
    f.write(element[2] + ' (' + element[1] +')')
