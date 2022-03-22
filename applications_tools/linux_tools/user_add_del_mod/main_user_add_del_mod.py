import os

# Το tool θα χρησιμοποιηθεί για να προσθέσει να αφερέσει και να (modify) οποιονδίποτε χρήστη του συστήματος
#   δεν παίζει ρόλο αν είναι debian ή arch το σύστημα στο οποίο θα τρέξει το προγραμμα γιατί και τα δύο συστήματα
#   έχουν τα usermod, userdel & useradd
#####################################################################################################################################
# command in terminal: man useradd usermod & userdel αντίστοιχα (man είναι το manual για κάθε πρόγραμμα που το έχει)                                             #
# ενμέρη βέβαια και ελάχειστα modified                                                                                              #
#DESCRIPTIONS:                                                                                                                       #
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

def flags_zero():
# Μπορεί να χρειαστώ να μηδενήσω τα flags για το usermod 
    # γενικά αυτά είναι τα switches που μπορεις να έχει για τα useradd, userdel & usermod
    # προς το παρών είναι μόνο για το useradd (aka comming soon)
    flag_table={"--badnames" : False, "--base-dir" : False, "--btrfs-subvolume-home" : False, "--comment" : False,
          "--home-dir" : False, "--defaults" : False, "--expiredate" : False, "--inactive" : False, "--gid" : False,
          "--groups" : False, "--skel" : False, "--key" : False, "--no-log-init" : False, "--create-home" : False, 
          "--no-create-home" : False, "--no-user-group" : False, "--non-unique" : False, "--password" : False, 
          "--system" : False, "--root" : False, "--prefix" : False, "--shell" : False, "--uid" : False, 
          "--user-group" : False, "--selinux-user" : False, "--extrausers" : False}
    #τα flags θα τα χρησιμοποιήσω στο να εμφανίζει στο terminal τα ανάλογα switches στον χρηστη.
    
def users_inputs(start, finish): #general user's inputs
    flag_continue=True
    while flag_continue:                                 
        user_input = int(input("gime a number ["+ str(start) + ","+ str(finish)+ "]:"))
        if user_input >= start and user_input <= finish:
            flag_continue=False
        else:
            print("wrong input please try again")
    return user_input

main_command="sudo user"# τα useradd, userdel & usermod προαπετούν να τρέχουν σε super user (sudo ή root) για να τρέξουν και
                        # να κάνουν αλαγες στο σύστημα

print("""In dev release is not have the users automaticly displayed(????)
probablly in the other versions will have all the modifyable users(???)\n\n""")
# to be continue... jojo end music referene (anime)

print("""what you want to do?
1-add a user?
2-modify a user?
3-delete a user?""")

user_input=users_inputs(1, 3)

if user_input == 1:
    
    main_command+="add"# εδώ απλός ολοκληρώνω το command useradd
    user_name=str(input("gime a username that you want to add to the system: "))
    print("""1-procceed as all default
2-manually control(???) (manual of useradd command)
""")
    
    user_input=users_inputs(1, 3)

    if user_input == 1:
          
        main_command = main_command + " --shell /bin/bash --create-home --system " + user_name + " && echo'' && sudo passwd " + user_name
        print(main_command)# δείχνει το command που θα τρέξει στον χρήστη
        os.system(main_command)# τρέχει το command στο terminal και δείχνει το output στον χρήστη
        
    elif user_input == 2:
        
        print("do you want help for the commands?(1-yes, 2-no)")
        user_input=users_inputs(1, 2)
        
        flags_zero()
        
        flag_continue=True
        while flag_continue:
            
            # έδώ απλός ο χρήστης θα μπορέσει να χρησημοποιήσει το κάθε ένα switch μόνο μια φορά 
            
            print("What do you whant to do with this new user?\n")
            
            if flag_table["--badnames"] == False:
                
                print("1-bad names do not check for bad names")
                
            if flag_table["--base-dir"] == False:

                print("2-base directory for the home directory of the new account")

            if flag_table["--btrfs-subvolume-home"] == False:

                print("3-use BTRFS subvolume for home directory")

            if flag_table["--comment"] == False:

                print("4-GECOS field of the new account")

            if flag_table["--home-dir"] == False:

                print("5-home directory of the new account")

            if flag_table["--defaults"] == False:

                print("6-print or change default useradd configuration")

            if flag_table["--expiredate"] == False:

                print("7-expiration date of the new account")

            if flag_table["--inactive"] == False:

                print("8-password inactivity period of the new account")

            if flag_table["--gid"] == False:

                print("9-name or ID of the primary group of the new account")

            if flag_table["--groups"] == False:

                print("10-list of supplementary groups of the new account")

            if flag_table["--skel"] == False:

                print("11-use this alternative skeleton directory")

            if flag_table["--key"] == False:

                print("12-override /etc/login.defs defaults")

            if flag_table["--no-log-init"] == False:

                print("13-do not add the user to the lastlog and faillog databases")

            if flag_table["--create-home"] == False:

                print("14-create the user's home directory")

            if flag_table["--no-create-home"] == False:

                print("15-do not create the user's home directory")

            if flag_table["--no-user-group"] == False:

                print("16-do not create a group with the same name as the user")

            if flag_table["--non-unique"] == False:

                print("17-allow to create users with duplicate (non-unique) UID")

            if flag_table["--password"] == False:

                print("18-encrypted password of the new account")

            if flag_table["--system"] == False:

                print("19-create a system account")

            if flag_table["--root"] == False:

                print("20-directory to chroot into")

            if flag_table["--prefix"] == False:

                print("21-prefix directory where are located the /etc/* files")

            if flag_table["--shell"] == False:

                print("22-login shell of the new account")

            if flag_table["--uid"] == False:

                print("23-user ID of the new account")

            if flag_table["--user-group"] == False:

                print("24-create a group with the same name as the user")

            if flag_table["--selinux-user"] == False:

                print("25-use a specific SEUSER for the SELinux user mapping")

            if flag_table["--extrausers"] == False:

                print("26-Use the extra users database")

            print("0-to exit")
            
            user_input=users_inputs(0, 26)
            
            # εδώ αν ο χρήστης επιλέξει ένα από αυτά τα switch θα το προσθεθεί στο main_command και θα κάνει update την ανάλογη
            # λίστα (δεν είμαι βέβαιος για αν λέγεται λίστα ή κάτι άλλο) καθός και το switch αυτό θα προσθεθεί μόνο μια φορά
            # στο main_command
            if user_input == 0:

                flag_continue=False

            elif user_input == 1 and flag_table["--badnames"] == False:

                flag_table.update({"--badnames" : True})

                main_command +=" --badnames"

            elif user_input == 2 and flag_table["--base-dir"] == False:

                flag_table.update({"--base-dir" : True})

                main_command = main_command + " --base-dir " + str(input("Give a base directory for the home directory of the new account: "))

            elif user_input == 3 and flag_table["--btrfs-subvolume-home"] == False:

                flags_table.update({"--btrfs-subvolume-home" : True})
                
                main_command+=" --btrfs-subvolume-home"

            elif user_input == 4 and flag_table["--comment"] == False:

                flag_table.update({"--comment" : True})

                main_command +=" --comment " + str(input("give me the comment for the new account:"))

            elif user_input == 5 and flag_table["--home-dir"] == False:

                flag_table.update({"--home-dir" : True})
                
                main_command+=" --home-dir " + str(input("give me the home directory of the new account (e.g. /home/USER_NAME): "))

            elif user_input == 6 and flag_table["--defaults"] == False:

                flag_table.update({"--defaults" : True})

            elif user_input == 7 and flag_table["--expiredate"] == False:

                flag_table.update({"--expiredate" : True})
                
                print("""
    The date on which the user account will be disabled. The date is
    specified in the format YYYY-MM-DD.
    
    If not specified, useradd will use the default expiry date
    specified by the EXPIRE variable in /etc/default/useradd, or an
    empty string (no expiry) by default.""")
                
                main_command +=" --expiredate " + str(input("give me the expiredate for the new account YYYY-MM-DD: "))

            elif user_input == 8 and flag_table["--inactive"] == False:
                
                flag_table.update({"--inactive" : True})
                
                print("""
    The number of days after a password expires until the account is
    permanently disabled. A value of 0 disables the account as soon as
    the password has expired, and a value of -1 disables the feature.

    If not specified, useradd will use the default inactivity period
    specified by the INACTIVE variable in /etc/default/useradd, or -1
    by default.""")

                main_command +=" --inactive " + str(input("Give me the days after a password expires: "))
    
            elif user_input == 9 and flag_table["--gid"] == False:
                print("""
    The group name or number of the user's initial login group. The
    group name must exist. A group number must refer to an already
    existing group.

    If not specified, the behavior of useradd will depend on the
    USERGROUPS_ENAB variable in /etc/login.defs. If this variable is
    set to yes (or -U/--user-group is specified on the command line), a
    group will be created for the user, with the same name as her
    loginname. If the variable is set to no (or -N/--no-user-group is
    specified on the command line), useradd will set the primary group
    of the new user to the value specified by the GROUP variable in
    /etc/default/useradd, or 100 by default.\n""")

                flag_table.update({"--gid" : True})
                
                main_command +=" --gid " + str(input("Give me a id or name of an already group name that must exist: "))
                

            elif user_input == 10 and flag_table["--groups"] == False:
                
                print("""
    A list of supplementary groups which the user is also a member of.
    Each group is separated from the next by a comma, with no
    intervening whitespace. The groups are subject to the same
    restrictions as the group given with the -g option. The default is
    for the user to belong only to the initial group.\n""")

                flag_table.update({"--groups" : True})
                
                main_command +=" --groups " + str(input("Give me a GROUP1[,GROUP2,...[,GROUPN]]]: "))

            elif user_input == 11 and flag_table["--skel"] == False:

                flag_table.update({"--skel" : True})

            elif user_input == 12 and flag_table["--key"] == False:

                flag_table.update({"--key" : True})

            elif user_input == 13 and flag_table["--no-log-init"] == False:

                flag_table.update({"--no-log-init" : True})

            elif user_input == 14 and flag_table["--create-home"] == False:

                flag_table.update({"--create-home" : True})

            elif user_input == 15 and flag_table["--no-create-home"] == False:

                flag_table.update({"--no-create-home" : True})

                main_command +=" --no-create-home"

            elif user_input == 16 and flag_table["--no-user-group"] == False:

                flag_table.update({"--no-user-group" : True})

                main_command +=" --no-user-group"

            elif user_input == 17 and flag_table["--non-unique"] == False:

                flag_table.update({"--non-unique" : True})

            elif user_input == 18 and flag_table["--password"] == False:

                flag_table.update({"--password" : True})

                main_command +=" --password " + str(input("gime the password for the account: "))

            elif user_input == 19 and flag_table["--system"] == False:

                flag_table.update({"--system" : True})

                main_command +=" --system"

            elif user_input == 20 and flag_table["--root"] == False:

                flag_table.update({"--root" : True})

            elif user_input == 21 and flag_table["--prefix"] == False:

                flag_table.update({"--prefix" : True})

            elif user_input == 22 and flag_table["--shell"] == False:

                flag_table.update({"--shell" : True})

                main_command +=" --shell "+ str(input("give me the shell that you want to use: "))

            elif user_input == 23 and flag_table["--uid"] == False:

                flag_table.update({"--uid" : True})

            elif user_input == 24 and flag_table["--user-group"] == False:

                flag_table.update({"--user-group" : True})

            elif user_input == 25 and flag_table["--selinux-user"] == False:

                flag_table.update({"--selinux-user" : True})

            elif user_input == 26 and flag_table["--extrausers"] == False:

                flag_table.update({"--extrausers" : True})

                
        main_command +=" " + user_name + " && passwd " + user_name
        os.system(main_command)
        
    elif user_input == 3:
        
        main_command = "man useradd"
        os.system(main_command)
        
elif user_input == 2:
    
    main_command+="mod"
    user_name=str(input("gime a username that you want to modify from the system: "))

elif user_input == 3:
    # basic command for now just a prototype for this section....
    # AKA comming soon...
    main_command += "del"
    user_name = str(input("gime a username that you want to delete from the system: "))
    main_command += " " + user_name
    os.system(main_command)
    
print("end")
# αυτά είναι τα options για το useradd το command που χρησημοποιήθηκε είναι: useradd --help
#
#useradd Options
  #    --badnames                do not check for bad names
  #-b, --base-dir BASE_DIR       base directory for the home directory of the new account
  #    --btrfs-subvolume-home    use BTRFS subvolume for home directory
  #-c, --comment COMMENT         GECOS field of the new account
  #-d, --home-dir HOME_DIR       home directory of the new account
  #-D, --defaults                print or change default useradd configuration
  #-e, --expiredate EXPIRE_DATE  expiration date of the new account
  #-f, --inactive INACTIVE       password inactivity period of the new account
  #-g, --gid GROUP               name or ID of the primary group of the new account
  #-G, --groups GROUPS           list of supplementary groups of the new account
  #-k, --skel SKEL_DIR           use this alternative skeleton directory
  #-K, --key KEY=VALUE           override /etc/login.defs defaults
  #-l, --no-log-init             do not add the user to the lastlog and faillog databases
  #-m, --create-home             create the user's home directory
  #-M, --no-create-home          do not create the user's home directory
  #-N, --no-user-group           do not create a group with the same name as the user
  #-o, --non-unique              allow to create users with duplicate (non-unique) UID
  #-p, --password PASSWORD       encrypted password of the new account
  #-r, --system                  create a system account
  #-R, --root CHROOT_DIR         directory to chroot into
  #-P, --prefix PREFIX_DIR       prefix directory where are located the /etc/* files
  #-s, --shell SHELL             login shell of the new account
  #-u, --uid UID                 user ID of the new account
  #-U, --user-group              create a group with the same name as the user
  #-Z, --selinux-user SEUSER     use a specific SEUSER for the SELinux user mapping
  #    --extrausers              Use the extra users database

#usemod Options:
   #-b, --badnames                allow bad names
   #-c, --comment COMMENT         new value of the GECOS field
   #-d, --home HOME_DIR           new home directory for the user account
   #-e, --expiredate EXPIRE_DATE  set account expiration date to EXPIRE_DATE
   #-f, --inactive INACTIVE       set password inactive after expiration
   #                              to INACTIVE
   #-g, --gid GROUP               force use GROUP as new primary group
   #-G, --groups GROUPS           new list of supplementary GROUPS
   #-a, --append                  append the user to the supplemental GROUPS
   #                              mentioned by the -G option without removing
   #                              the user from other groups
   #-h, --help                    display this help message and exit
   #-l, --login NEW_LOGIN         new value of the login name
   #-L, --lock                    lock the user account
   #-m, --move-home               move contents of the home directory to the
   #                              new location (use only with -d)
   #-o, --non-unique              allow using duplicate (non-unique) UID
   #-p, --password PASSWORD       use encrypted password for the new password
   #-R, --root CHROOT_DIR         directory to chroot into
   #-P, --prefix PREFIX_DIR       prefix directory where are located the /etc/* files
   #-s, --shell SHELL             new login shell for the user account
   #-u, --uid UID                 new UID for the user account
   #-U, --unlock                  unlock the user account
   #-v, --add-subuids FIRST-LAST  add range of subordinate uids
   #-V, --del-subuids FIRST-LAST  remove range of subordinate uids
   #-w, --add-subgids FIRST-LAST  add range of subordinate gids
   #-W, --del-subgids FIRST-LAST  remove range of subordinate gids
   # -Z, --selinux-user SEUSER     new SELinux user mapping for the user account
   
#userdel Options:
  #-f, --force                   force removal of files, even if not owned by user
  #-h, --help                    display this help message and exit
  #-r, --remove                  remove home directory and mail spool
  #-R, --root CHROOT_DIR         directory to chroot into
  #-P, --prefix PREFIX_DIR       prefix directory where are located the /etc/* files
  #    --extrausers              Use the extra users database
  #-Z, --selinux-user            remove any SELinux user mapping for the user
##################################
# στο περίπου τρέχει ο κώδικας!!!#
##################################