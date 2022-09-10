from os import system


def users_inputs(start, finish):  # general user's inputs
    global user_input
    flag_continue = True
    while flag_continue:
        user_input = int(input("gime a number [" + str(start) + "," + str(finish) + "]:"))
        if start <= user_input <= finish:
            flag_continue = False
        else:
            print("wrong input please try again")
    return user_input


def user_continue():
    while True:
        user_inpt = str(input("\n Do you want to continue(Y/n): "))
        if user_inpt == "n" or user_inpt == "N":
            return False
        elif user_inpt == "y" or user_inpt == "Y" or user_inpt == "":
            return True
        else:
            print("wrong input please try again")


def crt_script():
    script = open("applications_tools/linux_tools/g_lib/script.sh", "w+")
    script.write("""
#!/bin/bash

# ναι ξέρω πως δεν είναι python είναι shell γιατί δεν μπορεσα να το γράψω σε python 
# και για αυτό ήθελε bash shell script (probably the first and the last shell script for this project)
# μπορεί να το κάνω σε μια γραμή και να το γράψω σε pyrhon οπότε ναι δεν είναι μόνιμο
# Tέλος πάντων το script αυτό κάνει ένα νέο config file στο οποίο θα γίνεται κάθε φορά update
# για να φύγει το γεγονός του distro hopping.
# τι είναι αυτό?? είναι μια διαδικασία που ο χρήστης αλάζει το linux συστημα σε διαφορετικές διανομές
# και μπορεί να τύχει να γίνεται μετάβαση από debian σε arch βασησμένα συστήματα ή και το αντίθετο
# για αυτό βρήσκει ποιά package manager έχει εγκατεστημένα και σε τι είναι βασησμένα το τορινό σύστημα

# εδώ τρέχει το command ls /etc/debian_version και επιστρέφει το path αν υπάρχει το αρχείο αυτο
# αν δεν υπάρχει το αρχείο αυτό δεν επιστρέφει τίποτα
output=$(ls /etc/debian_version)

if [[ $output == "/etc/debian_version" ]]; then
    distro_based="debian"
else
    distro_based="arch"
fi

output=$(ls /bin/apt)

if [[ $output == "/bin/apt" ]]; then
    flag_apt="True"
else
    flag_apt="False"
fi

output=$(ls /bin/snap)

if [[ $output == "/bin/snap" ]]; then
    flag_snap="True"
else
    flag_snap="False"
fi

output=$(ls /bin/flatpak)

if [[ $output == "/bin/flatpak" ]]; then
    flag_flatpak="True"
else
    flag_flatpak="False"
fi

output=$(ls /bin/pacman)

if [[ $output == "/bin/pacman" ]]; then
    flag_pacman="True"
else
    flag_pacman="False"
fi
# τα flag apt, pacman, snap και flatpak είναι για να δεει αν είναι εγκατεστημένο ή όχι το συγκεκριμένο package manager

#εδώ γράφει στο sys_update.ini και σε config τυπου που μπορεί να διαβάσει η βιβλιοθίκη configparser
# που θα χρησιμοποιηθεί ποιο μετά για να γίνει update στο σύστημα & για το install packages
echo "[System_properties]" > $(pwd)/applications_tools/linux_tools/g_lib/sys_info.ini
echo "distro_based = $distro_based" >> $(pwd)/applications_tools/linux_tools/g_lib/sys_info.ini
echo "package_manager_apt = $flag_apt" >> $(pwd)/applications_tools/linux_tools/g_lib/sys_info.ini
echo "package_manager_flatpak = $flag_flatpak" >> $(pwd)/applications_tools/linux_tools/g_lib/sys_info.ini
echo "package_manager_snap = $flag_snap" >> $(pwd)/applications_tools/linux_tools/g_lib/sys_info.ini
echo "package_manager_pacman = $flag_pacman" >> $(pwd)/applications_tools/linux_tools/g_lib/sys_info.ini
""")
    system("chmod +x $(pwd)/applications_tools/linux_tools/g_lib/script.sh")
