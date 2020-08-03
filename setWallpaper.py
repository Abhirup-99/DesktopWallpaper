import subprocess
from os import listdir,getcwd
from os.path import isfile, join,dirname

def setWallpaper():
    try:
        getImgDirectory = join(dirname(__file__), 'images')
        onlyfiles = [f for f in listdir(getImgDirectory) if isfile(join(getImgDirectory, f))]
        getFileLocation = join(getImgDirectory,onlyfiles[0])
        
        #linux command to change wallpaper
        command = "gsettings set org.gnome.desktop.background picture-uri '"+\
            getFileLocation+"'"
        subprocess.run(command,shell=True)
        return "success"
    except Exception as e:
        return "failure"

