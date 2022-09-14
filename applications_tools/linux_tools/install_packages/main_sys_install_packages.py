import configparser
from applications_tools.linux_tools.g_lib.general_library import crt_script
from os import getcwd, system
from applications_tools.linux_tools.install_packages.lib.lib import def_apt, def_snap, def_flatpak, def_pacman
from applications_tools.linux_tools.g_lib.general_library import users_inputs


def package_installer():
    crt_script()
    system("bash $(pwd)/applications_tools/linux_tools/g_lib/script.sh")

    # dependecies για package manager
    config = configparser.ConfigParser()
    config.read(getcwd() + "/applications_tools/linux_tools/sys_info.ini")
    based_on = config.get('System_properties', 'distro_based')
    apt = config.get('System_properties', 'package_manager_apt')
    snap = config.get('System_properties', 'package_manager_snap')
    flatpak = config.get('System_properties', 'package_manager_flatpak')
    pacman = config.get('System_properties', 'package_manager_pacman')

    ##############################
    # see at this folders lib... #
    ##############################

    num_apt = -1
    num_snap = -1
    num_flatpak = -1
    num_pacman = -1
    i = 1

    if apt:
        i += 1
        print(i + "- for using apt")

    if snap:
        i += 1
        print(i + "- for using snap")

    if flatpak:
        i += 1
        print(i + "- for using flatpak")

    if pacman:
        i += 1
        print(i + "- for using pacman")
    print("    0- exit")
    user_input = users_inputs(0, i)

    if user_input == num_apt:
        def_apt()
    elif user_input == num_snap:
        def_snap()
    elif user_input == num_flatpak:
        def_flatpak()
    elif user_input == num_pacman:
        def_pacman()
