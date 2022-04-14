import os

# Το tool θα χρησιμοποιηθεί για να προσθέσει να αφερέσει και να (modify) οποιονδίποτε χρήστη του συστήματος
#   δεν παίζει ρόλο αν είναι debian ή arch το σύστημα στο οποίο θα τρέξει το προγραμμα γιατί και τα δύο συστήματα
#   έχουν τα usermod, userdel & useradd
#####################################################################################################################################
# command in terminal: man useradd usermod & userdel αντίστοιχα (man είναι το manual για κάθε πρόγραμμα που το έχει)                #
# ενμέρη βέβαια και ελάχειστα modified                                                                                              #
#DESCRIPTIONS:                                                                                                                      #
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
    # προς το παρών είναι μόνο για τα useradd & userdell (aka comming soon for usermod)
    flag_table={"--badnames" : False, "--base-dir" : False, "--btrfs-subvolume-home" : False, "--comment" : False,
          "--home-dir" : False, "--defaults" : False, "--expiredate" : False, "--inactive" : False, "--gid" : False,
          "--groups" : False, "--skel" : False, "--key" : False, "--no-log-init" : False, "--create-home" : False, 
          "--no-create-home" : False, "--no-user-group" : False, "--non-unique" : False, "--password" : False, 
          "--system" : False, "--root" : False, "--prefix" : False, "--shell" : False, "--uid" : False, 
          "--user-group" : False, "--selinux-user" : False, "--extrausers" : False, "temp --base-dir" : False,
          "temp --expiredate" : False, "temp --inactive" : False, "temp --gid" : False, "temp --shell" : False,
          "usrD--force" : False, "usrD--remove" : False, "usrD--root" : False, "usrD--prefix" : False, "usrD--extrausers" : False,
          "usrD--selinux-user" : False }
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
    
    main_command+="add" # εδώ απλός ολοκληρώνω το command useradd
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
        
        print("do you want help for the commands?(1-yes(recomended), 2-no)")
        user_input=users_inputs(1, 2)
        if user_input == 1:
            flag_help=True
        elif user_input == 2:
            flag_help=False
        
        flag_table=flags_zero()
        
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
            # λίστα καθώς και το switch αυτό θα προσθεθεί μόνο μια φορά στο main_command
            #ΕΠΕΙΣΗΣ RTFM (aka man useradd)
            if user_input == 0:

                flag_continue=False

            elif user_input == 1 and flag_table["--badnames"] == False:

                if flag_help == True:
                    print("Allow names that do not conform to standards.")

                flag_table.update({"--badnames" : True})
                main_command +=" --badnames"

            elif user_input == 2 and flag_table["--base-dir"] == False:
                
                if flag_help == True:
                    print("""
    The default base directory for the system if -d HOME_DIR is not specified.  BASE_DIR is concatenated with the account name to define
    the home directory. If the -m option is not used, BASE_DIR must exist.

    If this option is not specified, useradd will use the base directory specified by the HOME variable in /etc/default/useradd, or /home
    by default.""")

                flag_table.update({"--base-dir" : True})
                main_command = main_command + " --base-dir " + str(input("Give a base directory for the home directory of the new account: "))

            elif user_input == 3 and flag_table["--btrfs-subvolume-home"] == False:
                
                if flag_help == True:
                    print("""
    Traditionally, a user's home directory is a subdirectory of /home. Ownership and privileges are tailored to the owner, but there are 
    no special functions for managing them. The enterprise server environment is another scenario. Often, a directory is reserved for use 
    by a particular application and its user. You can take advantage of Btrfs to manage and apply constraints to these directories.

To accommodate Btrfs subvolumes as user homes, there is a new option to the useradd command: --btrfs-subvolume-home. Although the man pages 
have not been updated (as of this writing), you can see the option by running useradd --help. By passing this option when adding a new user, 
a new Btrfs subvolume will be created. It functions just like the -d option does for creating a regular directory:

# useradd --btrfs-subvolume-home student2""") # 1-1 from https://opensource.com/article/20/11/btrfs-linux

                flags_table.update({"--btrfs-subvolume-home" : True})
                main_command+=" --btrfs-subvolume-home"

            elif user_input == 4 and flag_table["--comment"] == False:

                if flag_help == True:
                    print("Any text string. It is generally a short description of the login, and is currently used as the field for the user's full name.")

                flag_table.update({"--comment" : True})
                main_command +=" --comment " + str(input("Give me the comment for the new account:"))

            elif user_input == 5 and flag_table["--home-dir"] == False:
                
                if flag_help == True:
                    print("""
    The new user will be created using HOME_DIR as the value for the user's login directory. The default is to append the LOGIN name to
    BASE_DIR and use that as the login directory name. If the directory HOME_DIR does not exist, then it will be created unless the -M
    option is specified.""")

                flag_table.update({"--home-dir" : True})
                main_command+=" --home-dir " + str(input("Give me the home directory of the new account (e.g. /home/USER_NAME): "))

            elif user_input == 6 and flag_table["--defaults"] == False:

                flag_table.update({"--defaults" : True})
                
                flag_continue_sec=True
                while flag_continue_sec:# ahh yes menu inside a menu feels like programming inception XD
                    print("""
    1-see the defaults
    2-change the defaults values
    3-exit""")
                    user_input=users_inputs( 1, 3)# γενικότερα εδώ γίνεται configure τα defaults από το useradd 
                    if user_input == 1:           # regret that project allready :_( current last line 760 X|
                        os.system("useradd -D")
                    elif user_input == 2:
                        secondary_command="sudo useradd -D "
                        flag_continue_sec_2=True
                        while flag_continue_sec_2:
                            if flag_table["temp --base-dir"] == False:
                                print("1-base directory for the home directory of the new account")
                            if flag_table["temp --expiredate"] == False:
                                print("2-expiration date of the new account")
                            if flag_table["temp --inactive"] == False:
                                print("3-password inactivity period of the new account")
                            if flag_table["temp --gid"] == False:
                                print("4-name or ID of the primary group of the new account")
                            if flag_table["temp --shell"] == False:
                                print("5-login shell of the new account")
                            print("0-exit")
                            user_input=users_inputs(0,5)

                            if user_input == 0:
                                flag_continue_sec_2=False
                            elif user_input == 1 and flag_table["temp --base-dir"] == False:

                                flag_table.update({"temp --base-dir" : True})
                                secondary_command+= " --base-dir " + str(input("Give me the BASE of the default home directory"))

                            elif user_input == 2 and flag_table["temp --expiredate"] == False:

                                if flag_help == True:
                                    print("""
        The date on which the user account will be disabled. The date is
        specified in the format YYYY-MM-DD.

        If not specified, useradd will use the default expiry date
        specified by the EXPIRE variable in /etc/default/useradd, or an
        empty string (no expiry) by default.""")
                            
                                flag_table.update({"temp --expiredate" : True})
                                secondary_command+= " --expiredate " + str(input("Give me the expiredate for the default expiredate YYYY-MM-DD: "))
                                
                            elif user_input == 3 and flag_table["temp --inactive"] == False:
                                
                                if flag_help == True:
                                    print("""
        The number of days after a password expires until the account is
        permanently disabled. A value of 0 disables the account as soon as
        the password has expired, and a value of -1 disables the feature.

        If not specified, useradd will use the default inactivity period
        specified by the INACTIVE variable in /etc/default/useradd, or -1
        by default.""")
                                
                                flag_table.update({"temp --inactive" : True})
                                secondary_command+= " --inactive " + str(input("Give me a number of days after a password expires: "))
                                
                            elif user_input == 4 and flag_table["temp --gid"] == False:
                                
                                if flag_help == True:
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
        /etc/default/useradd, or 100 by default.""")
                                    
                                flag_table.update({"temp --gid" : True})
                                secondary_command+= " --gid " + str(input("Give me a name of the group that must exist: "))
                            
                            elif user_input == 5 and flag_table["temp --shell"] == False:
                                
                                if flag_help == True:
                                    print("""
        The name of the user's login shell. The default is to leave this
        field blank, which causes the system to select the default login
        shell specified by the SHELL variable in /etc/default/useradd, or
        an empty string by default.""")
                                    
                                flag_table.update({"temp --shell" : True })
                                secondary_command+= " --skell " + str(input("Give me the new path of the new shell for the default skelleton: "))
                        print("command= \"" + secondary_command + "\"")
                        os.system(secondary_command)
                    else: 
                        flag_continue_sec = False

            elif user_input == 7 and flag_table["--expiredate"] == False:

                flag_table.update({"--expiredate" : True})
                
                if flag_help == True:
                    print("""
    The date on which the user account will be disabled. The date is
    specified in the format YYYY-MM-DD.
    
    If not specified, useradd will use the default expiry date
    specified by the EXPIRE variable in /etc/default/useradd, or an
    empty string (no expiry) by default.""")
                
                main_command +=" --expiredate " + str(input("Give me the expiredate for the new account YYYY-MM-DD: "))

            elif user_input == 8 and flag_table["--inactive"] == False:
                
                flag_table.update({"--inactive" : True})
                if flag_help == True:
                    print("""
    The number of days after a password expires until the account is
    permanently disabled. A value of 0 disables the account as soon as
    the password has expired, and a value of -1 disables the feature.

    If not specified, useradd will use the default inactivity period
    specified by the INACTIVE variable in /etc/default/useradd, or -1
    by default.""")

                main_command +=" --inactive " + str(input("Give me the days after a password expires: "))
    
            elif user_input == 9 and flag_table["--gid"] == False:
                
                if flag_help == True:
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
                
                main_command +=" --inactive " + str(input("Give me the days after a password expires: "))

                flag_table.update({"--gid" : True})
                
                main_command +=" --gid " + str(input("Give me a id or name of an already group name that must exist: "))
                

            elif user_input == 10 and flag_table["--groups"] == False:
                
                if flag_help == True:               
                    print("""
    A list of supplementary groups which the user is also a member of.
    Each group is separated from the next by a comma, with no
    intervening whitespace. The groups are subject to the same
    restrictions as the group given with the -g option. The default is
    for the user to belong only to the initial group.\n""")

                flag_table.update({"--groups" : True})
                
                main_command +=" --groups " + str(input("Give me a secondary_group1,secondary_group2,... : "))

            elif user_input == 11 and flag_table["--skel"] == False:

                flag_table.update({"--skel" : True})
                
                if flag_help == True:
                    print("""
    The skeleton directory, which contains files and directories to be
    copied in the user's home directory, when the home directory is
    created by useradd.\n""")
                
                main_command +=" --skel " + str(input(""))

            elif user_input == 12 and flag_table["--key"] == False:
                
                if flag_help == True:
                    print("""
    Overrides /etc/login.defs defaults (UID_MIN, UID_MAX, UMASK,
    PASS_MAX_DAYS and others).

    Example: -K PASS_MAX_DAYS=-1 can be used when creating system
    account to turn off password aging, even though system account has
    no password at all. Multiple -K options can be specified, e.g.:
    -K UID_MIN=100  -K UID_MAX=499""")

                flag_table.update({"--key" : True})
                main_command+=" --key "
                print("""what you want to change from the default?
1-UID_MIN
2-UID_MAX
3-UMASK
4-PASS_MAX_DAYS
5-others""")
                user_input=users_inputs(1,5)
                
                if user_input == 1:
                    
                    main_command += "UID_MIN=" + str(input("Give me a value for the UID_MIN: "))
                    
                elif user_input == 2:
                    
                    main_command += "UID_MAX=" + str(input("Give me a value for the UID_MAX: "))
                elif user_input == 3:
                    
                    main_command += "UMASK=" + str(input("Give me a value for the UMASK: "))
                elif user_input == 4:
                    
                    main_command += "PASS_MAX_DAYS=" + str(input("Give me a value for the PASS_MAX_DAYS: "))
                elif user_input == 5:
                    KEY=str(input("Give me a KEY:"))
                    VALUE=str(input("Give me a value for that KEY: "))
                    main_command += KEY + "=" + VALUE
                    print(main_command)

            elif user_input == 13 and flag_table["--no-log-init"] == False:

                if flag_help == True:
                    print("""
    Do not add the user to the lastlog and faillog databases.

    By default, the user's entries in the lastlog and faillog databases
    are reset to avoid reusing the entry from a previously deleted
    user.

    If this option is not specified, useradd will also consult the
    variable LOG_INIT in the /etc/default/useradd if set to no the user
    will not be added to the lastlog and faillog databases.""")
                
                flag_table.update({"--no-log-init" : True})
                main_command +=" --no-log-init"

            elif user_input == 14 and flag_table["--create-home"] == False:

                if flag_help == True:
                    print("""
    Create the user's home directory if it does not exist. The files
    and directories contained in the skeleton directory (which can be
    defined with the -k aka --skel option) will be copied to the home directory.

    By default, if this option is not specified and CREATE_HOME is not
    enabled, no home directories are created.

    The directory where the user's home directory is created must exist
    and have proper SELinux context and permissions. Otherwise the
    user's home directory cannot be created or accessed.""")

                flag_table.update({"--create-home" : True})
                main_command +=" --create-home"

            elif user_input == 15 and flag_table["--no-create-home"] == False:
                
                if flag_help == True:
                    print("""
    Do no create the user's home directory, even if the system wide
    setting from /etc/login.defs (CREATE_HOME) is set to yes.""")

                flag_table.update({"--no-create-home" : True})
                main_command +=" --no-create-home"

            elif user_input == 16 and flag_table["--no-user-group"] == False:

                if flag_help == True:
                    print("""
    Do not create a group with the same name as the user, but add the
    user to the group specified by the -g option or by the GROUP
    variable in /etc/default/useradd.

    The default behavior (if the -g, -N, and -U options are not
    specified) is defined by the USERGROUPS_ENAB variable in
    /etc/login.defs.""")

                flag_table.update({"--no-user-group" : True})
                main_command +=" --no-user-group"

            elif user_input == 17 and flag_table["--non-unique"] == False:
                
                if flag_help == True:
                    print("""
    Allow the creation of a user account with a duplicate (non-unique)
    UID.

    This option is only valid in combination with the -u aka --user-group option.""")

                flag_table.update({"--non-unique" : True})
                main_command +=" --non-unique"

            elif user_input == 18 and flag_table["--password"] == False:
                
                if flag_help == True:
                    print("""
    The encrypted password, as returned by crypt(3). The default is to
    disable the password.
    Note: This option is not recommended because the password (or
    encrypted password) will be visible by users listing the processes.

    You should make sure the password respects the system's password
    policy.""")

                flag_table.update({"--password" : True})
                main_command +=" --password " + str(input("gime the password for the account: "))

            elif user_input == 19 and flag_table["--system"] == False:

                flag_table.update({"--system" : True})
                
                if flag_help == True:
                    print("""
    Create a system account.
    
    System users will be created with no aging information in
    /etc/shadow, and their numeric identifiers are chosen in the
    SYS_UID_MIN-SYS_UID_MAX range, defined in /etc/login.defs, instead
    of UID_MIN-UID_MAX (and their GID counterparts for the creation of
    groups).
    
    Note that useradd will not create a home directory for such a user,
    regardless of the default setting in /etc/login.defs (CREATE_HOME).
    You have to specify the -m options if you want a home directory for
    a system account to be created.""")

                main_command +=" --system"

            elif user_input == 20 and flag_table["--root"] == False:
                
                if flag_help == True:
                    print("""
    Apply changes in the CHROOT_DIR directory and use the configuration
    files from the CHROOT_DIR directory.""") 

                flag_table.update({"--root" : True})
                main_command+= " --root " + str(input("Give me the path of the CHROOT_DIR: "))

            elif user_input == 21 and flag_table["--prefix"] == False:
                
                if flag_help == True:
                    print("""
    Apply changes in the PREFIX_DIR directory and use the configuration
    files from the PREFIX_DIR directory. This option does not chroot
    and is intended for preparing a cross-compilation target. Some
    limitations: NIS and LDAP users/groups are not verified. PAM
    authentication is using the host files. No SELINUX support.""")

                flag_table.update({"--prefix" : True})
                main_command += " --prefix " + str(input("Give me the path of PREFIX_DIR directory: "))

            elif user_input == 22 and flag_table["--shell"] == False:
                
                if flag_help == True:
                    print("""
    The name of the user's login shell. The default is to leave this
    field blank, which causes the system to select the default login
    shell specified by the SHELL variable in /etc/default/useradd, or
    an empty string by default.""")

                flag_table.update({"--shell" : True})
                main_command +=" --shell "+ str(input("give me the shell that you want to use: "))

            elif user_input == 23 and flag_table["--uid"] == False:
                
                if flag_help == True:
                    print("""
    The numerical value of the user's ID. This value must be unique,
    unless the -o option is used. The value must be non-negative. The
    default is to use the smallest ID value greater than or equal to
    UID_MIN and greater than every other user.

    See also the -r option and the UID_MAX description.""")

                flag_table.update({"--uid" : True})
                main_command+=" --uid" + str(input("Give me a number for the new user: "))

            elif user_input == 24 and flag_table["--user-group"] == False:

                if flag_help == True:
                        print("""
    Create a group with the same name as the user, and add the user to
    this group.

    The default behavior (if the -g, -N, and -U options are not
    specified) is defined by the USERGROUPS_ENAB variable in
    /etc/login.defs.""")

                flag_table.update({"--user-group" : True})
                main_command+= " --user-group"

            elif user_input == 25 and flag_table["--selinux-user"] == False:

                if flag_help == True:
                    print("""
    The SELinux user for the user's login. The default is to leave this
    field blank, which causes the system to select the default SELinux
    user.""")

                flag_table.update({"--selinux-user" : True})
                main_command+= " --selinux-user" + str(input("Give me a SEUSER"))

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
    user_name=str(input("gime a username that you want to delete from the system: "))
    
    print("""1- Simple account dellition
2- Configurable account delition
""")

    user_input=users_inputs(1,2)

    if user_input == 1:
        
        main_command += " " + user_name

    elif user_input == 2:
        
        user_input=users_inputs(1, 2)
        if user_input == 1:
            flag_help=True
            print("userdel [options] LOGIN")
        elif user_input == 2:
            flag_help=False
        

        flag_table=flags_zero()

        print        
        while True:
            if flag_table["usrD--force"] == False:
                print("1-force removal of files, even if not owned by user")

            if flag_table["usrD--remove"] == False:
                print("2-remove home directory and mail spool")

            if flag_table["usrD--root"] == False:
                print("3-directory to chroot into")

            if flag_table["usrD--prefix"] == False:
                print("4-prefix directory where are located the /etc/* files")

            if flag_table["usrD--selinux-user"] == False:
                print("5-remove any SELinux user mapping for the user")

            print("0-exit and run the command")

            user_input = users_inputs(0,5)

            if user_input == 1 and flag_table["userD--force"] == False:
                flag_table["userD--force"] = True
                
                if flag_help == True:
                    print("""
    This option forces the removal of the user account, even if the user is still logged in. It also forces userdel to remove the user's
    home directory and mail spool, even if another user uses the same home directory or if the mail spool is not owned by the specified
    user. If USERGROUPS_ENAB is defined to yes in /etc/login.defs and if a group exists with the same name as the deleted user, then this
    group will be removed, even if it is still the primary group of another user.

    Note: This option is dangerous and may leave your system in an inconsistent state.
        
        cfg
        USERGROUPS_ENAB (boolean)
            Enable setting of the umask group bits to be the same as owner bits (examples: 022 -> 002, 077 -> 007) for non-root users, if the uid
            is the same as gid, and username is the same as the primary group name.

            If set to yes, userdel will remove the user's group if it contains no more members, and useradd will create by default a group with the
            name of the user.""")
                
                main_command+= " -- force "
                
                if str(input("User group Enable?(yes or no): ")) == "yes":
                    main_command += "USERGROUPS_ENAB true"
                else:
                    main_command += "USERGROUPS_ENAB false"
                    
            elif user_input == 2 and flag_table["userD--remove"] == False:
                flag_table["usrD--remove"]=True
                
                if flag_help == True:
                    print("""
    Files in the user's home directory will be removed along with the home directory itself and the user's mail spool. Files located in
    other file systems will have to be searched for and deleted manually.

    The mail spool is defined by the MAIL_DIR variable in the login.defs file.
    
        cfg
        MAIL_DIR (string)
            The mail spool directory. This is needed to manipulate the mailbox when its corresponding user account is modified or deleted. If not
            specified, a compile-time default is used. The parameter CREATE_MAIL_SPOOL in /etc/default/useradd determines whether the mail spool
            should be created.
        
        MAIL_FILE (string)
            Defines the location of the users mail spool files relatively to their home directory.

            The MAIL_DIR and MAIL_FILE variables are used by useradd, usermod, and userdel to create, move, or delete the user's mail spool.

            If MAIL_CHECK_ENAB is set to yes, they are also used to define the MAIL environment variable.""")
                    
                main_command += " --remove " + str(input("give me the configuration: "))

            elif user_input == 3 and flag_table["userD--root"] == False:
                flag_table["usrD--root"]=True
                
                if flag_help == True:
                    print("""
    Apply changes in the CHROOT_DIR directory and use the configuration files from the CHROOT_DIR directory.""")
                    
                main_command +=" --root"

            elif user_input == 4 and flag_table["userD--prefix"] == False:
                flag_table["usrD--prefix"]=True
                
                if flag_help == True:
                    print("""
    Apply changes in the PREFIX_DIR directory and use the configuration files from the PREFIX_DIR directory. This option does not chroot
    and is intended for preparing a cross-compilation target. Some limitations: NIS and LDAP users/groups are not verified. PAM
    authentication is using the host files. No SELINUX support.""")
                
                main_command += " --prefix"

            elif user_input == 5 and flag_table["userD--selinux-user"] == False:
                flag_table["usrD--selinux-user"]=True
                
                if flag_help == True:
                    print("""
    Remove any SELinux user mapping for the user's login.""")
                    
                main_command +=" --selinux-user"

            elif user_input == 0:
                break

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
   #-f, --inactive INACTIVE       set password inactive after expiration to INACTIVE
   #-g, --gid GROUP               force use GROUP as new primary group
   #-G, --groups GROUPS           new list of supplementary GROUPS
   #-a, --append                  append the user to the supplemental GROUPS mentioned by the -G option without removing the user from other groups
   #-l, --login NEW_LOGIN         new value of the login name
   #-L, --lock                    lock the user account
   #-m, --move-home               move contents of the home directory to the new location (use only with -d)
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
  # -f, --force                   force some actions that would fail otherwise e.g. removal of user still logged in or files, even if not owned by the user
  # -r, --remove                  remove home directory and mail spool
  # -R, --root CHROOT_DIR         directory to chroot into
  # -P, --prefix PREFIX_DIR       prefix directory where are located the /etc/* files
  # -Z, --selinux-user Remove any SELinux user mapping for the user's login.
##################################
# στο περίπου τρέχει ο κώδικας!!!#
##################################