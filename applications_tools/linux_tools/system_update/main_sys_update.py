import os
import configparser

# το os.system(...) δημιουργεί ένα shell shell 
os.system("bash -c \"source $(pwd)/applications-tools/linux-tools/tools/system_update/script.sh\"")
#dependecies για update
config = ConfigParser.ConfigParser()
config.read("")
based_on = config.get('', '')
apt = config.get('', '')
snap = config.get('', '')
flatpak = config.get('', '')
pacman = config.get('', '')

###########################
# non working prototype!!!#
###########################
# 18/03/22 02:47 AM