import os
import subprocess

def user_add_del_mod():
    from applications_tools.linux_tools.user_add_del_mod.lib.useradd import useradd
    from applications_tools.linux_tools.user_add_del_mod.lib.userdel import userdel
    from applications_tools.linux_tools.user_add_del_mod.lib.usermod import usermod
    from applications_tools.linux_tools.user_add_del_mod.lib.other_functions import users_inputs, user_continue, get_all_current_processes, kill_processes

    ###################################################################################################################
    # Το tool θα χρησιμοποιηθεί για να προσθέσει να αφερέσει και να (modify) οποιονδίποτε χρήστη του συστήματος       #
    #   δεν παίζει ρόλο αν είναι debian ή arch το σύστημα στο οποίο θα τρέξει το προγραμμα γιατί και τα δύο συστήματα #
    #   έχουν τα usermod, userdel & useradd                                                                           #
    #####################################################################################################################################
    # command in terminal: man useradd usermod & userdel αντίστοιχα (man είναι το manual για κάθε πρόγραμμα που το έχει)                #
    # ενμέρη βέβαια και ελάχειστα modified                                                                                              #
    # DESCRIPTIONS:                                                                                                                      #
    #   useradd is a low level utility for adding users. On Debian, administrators should usually use adduser(8) instead.               #
    #                                                                                                                                   #
    #      When invoked without the -D option, the useradd command creates a new user account using the values specified on the command #
    #       line plus the default values from the system. Depending on command line options, the useradd command will update system     #
    #       files and may also create the new user's home directory and copy initial files.                                             #
    #                                                                                                                                   #
    #       By default, a group will also be created for the new user (see -g, -N, -U, and USERGROUPS_ENAB)                             #
    #####################################################################################################################################
    #       The usermod command modifies the system account files to reflect the changes that are specified on the command line.        #
    #####################################################################################################################################
    #       userdel is a low level utility for removing users. On Debian, administrators should usually use deluser(8) instead.         #
    #                                                                                                                                   #
    #       The userdel command modifies the system account files, deleting all entries that refer to the user name LOGIN. The named    #
    #       user must exist.                                                                                                            #
    #####################################################################################################################################

    # Μπορεί να χρειαστώ να μηδενήσω τα flags για το usermod 
    # γενικά αυτά είναι τα switches που μπορεις να έχει για τα useradd, userdel & usermod
    # προς το παρών είναι μόνο για τα useradd & userdell (aka comming soon for usermod)
    flag_table={"--badnames" : False, "--base-dir" : False, "--btrfs-subvolume-home" : False, "--comment" : False,
            "--home-dir" : False, "--defaults" : False, "--expiredate" : False, "--inactive" : False, "--gid" : False,
            "--groups" : False, "--skel" : False, "--key" : False, "--no-log-init" : False, "--create-home" : False, 
            "--no-create-home" : False, "--no-user-group" : False, "--non-unique" : False, "--password" : False, 
            "--system" : False, "--root" : False, "--prefix" : False, "--shell" : False, "--uid" : False, 
            "--user-group" : False, "--selinux-user" : False, "--extrausers" : False, "temp --base-dir" : False,
            "temp --expiredate" : False, "temp --inactive" : False, "temp --gid" : False, "temp --shell" : False,
            "userD--force" : False, "userD--remove" : False, "userD--root" : False, "userD--prefix" : False, "userD--extrausers" : False,
            "userD--selinux-user" : False, "userM--badnames" : False, "userM--append" : False, "userM--comment" : False, "--home" : False, 
            "userM--expiredate" : False, "userM--inactive" : False, "userM--groups" : False, "userM--login" : False,
            "userM--move-home" : False, "userM--non-unique" : False, "userM--password" : False, "userM--remove" : False, "userM--root" : False, "userM--prefix" : False
            , "userM--shell" : False, "userM--uid" : False, "userM--unlock" : False, "userM--add-subuids" : False, "userM--del-subuids" : False, "userM--selinux-user" : False,
            "userM--add-subgids" :False, "userM--del-subgids" :False, "userM--comment" : False, "userM--home" : False, "userM--expiredate" : False,
             "userM--gid" : False,"userM--lock" : False}
    #τα flags θα τα χρησιμοποιήσω στο να εμφανίζει στο terminal τα ανάλογα switches στον χρηστη.
        
    main_command="sudo user"# τα useradd, userdel & usermod προαπετούν να τρέχουν σε super user (sudo ή root) για να τρέξουν και
                            # να κάνουν αλαγες στο σύστημα

    print("""\n\nIn dev release does not have the users automaticly displayed(????)
probablly in the other versions will have all the modifyable users in the modify category(???)\n\n""")
    # to be continue... jojo end music referene (anime)
    #aka https://music.youtube.com/watch?v=cPCLFtxpadE&feature=share
    while True:
        print("""
User add, delete, modify
What you want to do?

    1-add a user?
    2-modify a user?
    3-delete a user?
    0-exit the program.""")

        user_input=users_inputs(0, 3)

        if user_input == 0:
            break

        elif user_input == 1:
            ################################
            # changing stracture now eachone have it's own dedicated file
            #
            
            useradd(main_command, flag_table)
                
        elif user_input == 2:
            
            usermod(main_command, flag_table)
            
        elif user_input == 3:

            userdel(main_command, flag_table)
            
    print("exit user, add delete, modify")

    ##################################
    # στο περίπου τρέχει ο κώδικας!!!#
    ##################################