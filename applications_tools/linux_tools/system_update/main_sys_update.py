import os
from os import getcwd, system
import configparser

def sys_update():
    # το os.system(...) δημιουργεί ένα shell shell 
    system("bash -c \"source $(pwd)/applications_tools/linux_tools/system_update/script.sh\"")
    #dependecies για update
    config = configparser.ConfigParser()
    config.read(getcwd()+"/applications_tools/linux_tools/sys_info.ini")
    based_on = config.get('System_properties', 'distro_based')
    apt = config.get('System_properties', 'package_manager_apt')
    snap = config.get('System_properties', 'package_manager_snap')
    flatpak = config.get('System_properties', 'package_manager_flatpak')
    pacman = config.get('System_properties', 'package_manager_pacman')

    if apt == "True":
        system("echo\"\" && echo \" apt updating\" && echo \"\" && sudo apt update && echo\"\" && echo \"apt upgrading\" && echo \"\" && sudo apt upgrade")

    if pacman == "True":
        system("echo\"\" && echo \"pacman updating & upgrading\" && echo \"\" && sudo pacman -Suyy")

    if flatpak == "True":
        system("echo\"\" && echo \"flatpak updating\" && echo \"\" && sudo flatpak update && echo\"\" && echo \"flatpak upgrading\" && echo \"\" && sudo flatpak upgrade")

    if snap == "True":
        system("echo\"\" && echo \"snap updating\" && echo\"\" && snap refresh")

    ########################
    # working prototype!!! #
    ########################
    # 28/03/22 10:42 PM