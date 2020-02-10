import os
import shutil
from pathlib import Path
import eyed3
import unidecode
from datetime import datetime
from tkinter import *
from tkinter import filedialog

fulllist=[]

#String sanitization function that approximates illegal characters
def namesafe(argument):
    illegal = r'<.>\|?*:"/'
    legallist = []
    legal = ''
    for character in argument:
        if character not in illegal:
            legallist.append(character)
        else:
            legallist.append('-')
    legal = ''.join(legallist)
    return(unidecode.unidecode_expect_ascii(legal))

Window = Tk()
Window.title('Boomer Music Manager')
Window.geometry('640x480')

# Chooses initial directory
def Get_Initial():
    Initial_Dir = filedialog.askdirectory(initialdir = os.path.dirname('C:\\Users\Ja\Downloads\MediaHuman\Music'))
    Label_Initial.configure(text = Initial_Dir)

# Chooses target directory
def Get_Target():
    Target_Dir = filedialog.askdirectory(initialdir = os.path.dirname('C:\\Users\\Ja\\Music'))
    Label_Target.configure(text = Target_Dir)

Button_Initial = Button(Window, text = "Select initial directory", command = Get_Initial)
Button_Initial.grid(column = 1, row = 1)
Button_Target = Button(Window, text = "Select target directory", command = Get_Target)
Button_Target.grid(column = 1, row = 3)

Label_Initial = Label(Window, width = 50) 
Label_Initial.grid(column = 2, row = 1)
Label_Target = Label(Window, width = 50)
Label_Target.grid(column = 2, row = 3)


def Sort ():

    #Reads the directory names from the two labels and converts them to an appropriate format
    Initial_Dir = Path(Label_Initial.cget('text'))
    Target_Dir = Path(Label_Target.cget('text'))
    print(Initial_Dir, Target_Dir)

    if Initial_Dir == Target_Dir:
        return('error')

    # Builds a list of new and existing media
    List_Initial = os.listdir(Initial_Dir)
    List_Target = os.listdir(Target_Dir)
    print('List of new tracks:')
    for file in List_Initial:
        if file.endswith('.mp3'):
            print(file)

    # Makes a 2D list of relevant track metadata
    os.chdir(Initial_Dir)
    for file in List_Initial:
        if file.endswith('.mp3'):
            # Load metadata from each new file
            audiofile = eyed3.load(file)
            artist = audiofile.tag.artist
            album = audiofile.tag.album
            # Builds a list where [0] is artist, [1] is album and [2] is filename
            filedata = [artist, album, file]
            fulllist.append(filedata)

    print('List of all track metadata:')
    print(fulllist)

    for element in fulllist:
        os.chdir(Target_Dir)

        # Checks for illegal characters in the metadata, replaces missing data with "Unknown album/artist"
        if namesafe(element[0]):
            ArtistSafe = namesafe(element[0])
        else:
            ArtistSafe = 'Unknown Artist'
        
        if namesafe(element[1]):
            AlbumSafe = namesafe(element[1])
        else:
            AlbumSafe = 'Unknown Album'

        # Checks if the artist already has a legal designated folder and makes one if not
        if ArtistSafe not in List_Target:
            os.mkdir(ArtistSafe)
        ArtistFolder = Target_Dir / ArtistSafe
        os.chdir(ArtistFolder)
        

        # Checks if the album already has a legal designated folder and makes one if not
        if AlbumSafe not in os.listdir(ArtistFolder):
            os.mkdir(AlbumSafe)
        AlbumFolder = ArtistFolder / AlbumSafe
        os.chdir(AlbumFolder)
        print('Current directory is ' + os.getcwd())

        # Moves the new file into the correct directory
        print('Current directory is ' + os.getcwd())
        shutil.move(Initial_Dir / element[2], AlbumFolder / element[2])

    # Leaves a timestamped log of moved media in the initial directory
    os.chdir(Initial_Dir)
    # Build and apply timestamp to log
    now = datetime.now()
    current_time = now.strftime("%Y %m %d - %H - %M - %S.txt")
    # Populate log
    f = open(current_time,"w+")
    f.write('List of moved tracks: \n')
    for element in fulllist:
        f.write(element[2] + ' (' + element[1] +') \n')                      


Run = Button(Window, text = "Sort files", command = Sort)
Run.grid(column = 1, row = 5)

Window.mainloop()
