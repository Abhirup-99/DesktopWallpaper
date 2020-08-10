<center>**<h1>Automatic WallPaper Changing script</h1>**</center>
# Requirements
- python preferably 3, 2 would also do
- gnome terminal

# Get started
- To get started clone this repo
- In setEnv.sh update the path of the folder
>For me it was "/home/abhirup/Documents/selfProjects/extensionPractice/images/"
- Go to the terminal and write the following commands
    - pip3 install -r requirements.txt
    - crontab -e<br>
    >Think of a time when your computer is almost certain to be connected to the internet<br>
    >Add the following line
    - minValue hourValue * * * cd /<your-folder-path-here> && <your-python-path> main.py && bash setEnv.sh
    >For me it was
    >50 12 * * * cd /home/abhirup/Documents/selfProjects/extensionPractice && /usr/bin/python3 main.py && bash setEnv.sh


