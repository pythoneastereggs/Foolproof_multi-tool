from os import getcwd, system
from applications_tools.linux_tools.g_lib.general_library import crt_script
import configparser


def sys_update():
    # το os.system(...) δημιουργεί ένα shell shell
    crt_script()
    system("bash $(pwd)/applications_tools/linux_tools/g_lib/script.sh")

    # dependencies για update
    config = configparser.ConfigParser()
    config.read(getcwd() + "/applications_tools/linux_tools/g_lib/sys_info.ini")
    based_on = config.get('System_properties', 'distro_based')
    apt = config.get('System_properties', 'package_manager_apt')
    snap = config.get('System_properties', 'package_manager_snap')
    flatpak = config.get('System_properties', 'package_manager_flatpak')
    pacman = config.get('System_properties', 'package_manager_pacman')

    if apt == "True":
        system(
            "echo\"\" && echo \" apt updating\" && echo \"\" && sudo apt update && echo\"\" && echo \"apt upgrading\" && echo \"\" && sudo apt upgrade")

    if pacman == "True":
        system("echo\"\" && echo \"pacman updating & upgrading\" && echo \"\" && sudo pacman -Suyy")

    if flatpak == "True":
        system(
            "echo\"\" && echo \"flatpak updating\" && echo \"\" && sudo flatpak update && echo\"\" && echo \"flatpak upgrading\" && echo \"\" && sudo flatpak upgrade")

    if snap == "True":
        system("echo\"\" && echo \"snap updating\" && echo\"\" && sudo snap refresh")

    ########################
    # working prototype!!! #
    ########################
    # 28/03/22 10:42 PM
