import os
import eyed3
import shutil
from datetime import datetime

fulllist=[]

MediaHuman = 'C:\\Users\Ja\Downloads\MediaHuman\Music'
Music = 'C:\\Users\Ja\Music'

listMH = os.listdir(MediaHuman)
listMU = os.listdir(Music)
print('List of new tracks:')
print(listMH)


os.chdir(MediaHuman)                                         #Makes a 2D list of relevant track metadata
for file in listMH:
    if file.endswith('.mp3')
        audiofile = eyed3.load(file)
        artist = audiofile.tag.artist
        album = audiofile.tag.album
        #print(artist + album)
        filedata = [artist, album, file]
        fulllist.append(filedata)

print('List of all track metadata:')
print(fulllist)


for element in fulllist:
    os.chdir(Music)

    ArtistSafe = element[0].replace('/', '-')
    AlbumSafe = element[1].replace('/', '-')
    ArtistSafe = ArtistSafe.replace('ö', 'o')

    if ArtistSafe not in listMU:                            #Checks if the artist already has a legal designated folder and makes one if not
        os.mkdir(ArtistSafe)
    artistfolder = Music + '\\' + ArtistSafe
    os.chdir(artistfolder)
    print('Current directory is ' + os.getcwd())
    if AlbumSafe not in os.listdir(artistfolder):          #Checks if the album already has a legal designated folder and makes one if not
        os.mkdir(AlbumSafe)
    os.chdir(artistfolder + '\\' + AlbumSafe)
    print('Current directory is ' + os.getcwd())
    shutil.move(MediaHuman + '\\' + element[2], os.getcwd() + '\\' + element[2])  #Moves the new file into the correct directory

os.chdir(MediaHuman)
now = datetime.now()
current_time = now.strftime("%H-%M-%S")                     #Need to add date to the timestamp
f = open(current_time,"w+")
for element in fulllist:
    f.write('List of moved tracks:')
    f.write(element[2] + ' (' + element[1] +')')
