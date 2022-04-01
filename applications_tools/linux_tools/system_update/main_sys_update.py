import os
from os import getcwd, system
import configparser

# το os.system(...) δημιουργεί ένα shell shell 
system("bash -c \"source $(pwd)/applications-tools/linux-tools/tools/system_update/script.sh\"")
#dependecies για update
config = configparser.ConfigParser()
config.read(getcwd()+"/applications_tools/linux_tools/system_update/sys_update.ini")
based_on = config.get('System_properties', 'distro_based')
apt = config.get('System_properties', 'package_manager_apt')
snap = config.get('System_properties', 'package_manager_snap')
flatpak = config.get('System_properties', 'package_manager_flatpak')
pacman = config.get('System_properties', 'package_manager_pacman')

print("flags =", apt, snap, flatpak, pacman, based_on)

if apt == True:
    system("echo\"\" && echo \"updating\" && echo \"\" && sudo apt update && echo\"\" && echo \"upgrading\" && echo \"\" && sudo apt upgrade")

if pacman == True:
    system("echo\"\" && echo \"updating & upgrading\" && echo \"\" && sudo -Suuy")

if flatpak == True:
    system("echo\"\" && echo \"updating\" && echo \"\" && sudo flatpak update && echo\"\" && echo \"upgrading\" && echo \"\" && sudo flatpak upgrade")

if snap == True:
    system("echo\"\" && echo \"updating && echo\"\" && snap refresh")

########################
# working prototype!!! #
########################
# 28/03/22 10:42 PM