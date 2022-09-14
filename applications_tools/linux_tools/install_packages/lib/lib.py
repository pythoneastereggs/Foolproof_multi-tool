######################################################################
# Welcome to internet! (https://www.youtube.com/watch?v=k1BneeJTDcU) #
#####################################################################

##########################################################################################################
# anyway.. this folder is based on a skeleton that helps me shave some minutes of my life                #
# special is a case for snap and pacman that i think does not have the option to re install the packages #
##########################################################################################################

from os import system
from applications_tools.linux_tools.g_lib.general_library import users_inputs


def def_apt():
    skeleton("apt", "install", "reinstall", "remove", "list", "0")


def def_snap():
    skeleton("snap", "install", "remove", "remove", "list", "1")


def def_flatpak():
    skeleton("flatpak", "install", "repair", "uninstall", "search", "0")


def def_pacman():
    skeleton("pacman", "-S", "-R", "-R", "-Ss", "2")


def skeleton(package_manager, install, re_install, remove, search, special):
    while True:
        print("""   0- exit
    1- install package
    2- re-install package
    3- uninstall package
    4- search package""")
        user_input = users_inputs(0, 4)
        if user_input == 0:
            break

        elif user_input == 1:
            system("sudo " + package_manager + " " + install + "" + str(
                input("give me the name of the package to install: ")))

        elif user_input == 2:
            if special == 1:  # special 1 means snap "manual" automated re-installation process
                package = str(input("give me the name of the package to re-install: "))
                system(
                    "sudo " + package_manager + " " + re_install + " " + package + " && sudo " + package_manager + " " + " install" + package)

            elif special == 2:  # special 2 means pacman "manual" automated re-installation process
                package = str(input("give me the name of the package to re-install: "))
                system(
                    "sudo " + package_manager + " " + re_install + " " + package + " && sudo " + package_manager + " " + "-S " + package)

            elif special == 0:
                system("sudo " + package_manager + " " + re_install + " " + str(
                    input("give me the name of the package to re-install: ")))

        elif user_input == 3:
            system("sudo " + package_manager + " " + remove + " " + str(
                input("give me the name of the package to remove: ")))

        elif user_input == 4:
            system("sudo " + package_manager + " " + search + " " + str(
                input("give me the name of the package to search: ")))
