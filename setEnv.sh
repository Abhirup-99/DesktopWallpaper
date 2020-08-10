# export DBUS_SESSION_BUS_ADDRESS environment variable
PID=$(pgrep -o gnome-session)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

#replace with your path
#TODO: get path dynamically depending on output
wallpaper=`find "/home/abhirup/Documents/selfProjects/extensionPractice/images/" -type f` 
echo "Wallpaper path"
echo $wallpaper
gsettings set org.gnome.desktop.background picture-uri $wallpaper
