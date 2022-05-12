from lib.other_functions import users_inputs, user_continue, get_all_current_processes, kill_processes
import os
def usermod(main_command, flag_table):
    main_command+="mod"
    user_name=str(input("gime a username that you want to modify from the system: "))

    print("do you want help for the commands?")
    flag_help = user_continue()    

    while True:
        if flag_table["usrM--badnames"] == False:
            print("1-Allow bad names")
        
        if flag_table["userM--comment"] == False:
            print("2- New value of the GECOS field")
        
        if flag_table["userM--home"] == False:
            print("3- New home directory for the user account")
        
        if flag_table["userM--expiredate"] == False:
            print("4- set account expiration date to EXPIRE_DATE")
        
        if flag_table["userM--inactive"] == False:
            print("5- set password inactive after expiration to INACTIVE")
        
        if flag_table["userM--gid"] == False:
            print("6- force use GROUP as new primary group")
        
        if flag_table["userM--groups"] == False:
            print("7- new list of supplementary GROUPS")
        
        if flag_table["userM--append"] == False:
            print("""8- append the user to the supplemental GROUPS mentioned by the -G option 
without removing the user from other groups""")
        
        if flag_table["userM--login"] == False:
            print("9- new value of the login name")
        
        if flag_table["userM--lock"] == False:
            print("10- lock the user account")
        
        if flag_table["userM--move-home"] == False:
            print("11- move contents of the home directory to the new location (use only with -d)")
        
        if flag_table["userM--non-unique"] == False:
            print("12- allow using duplicate (non-unique) UID")
        
        if flag_table["userM--password"] == False:
            print("13- use encrypted password for the new password")
        
        if flag_table["userM--root"] == False:
            print("14- directory to chroot into")
        
        if flag_table["userM--prefix"] == False:
            print("15- prefix directory where are located the /etc/* files")
        
        if flag_table["userM--shell"] == False:
            print("16- new login shell for the user account")
        
        if flag_table["userM--uid"] == False:
            print("17- new UID for the user account")
        
        if flag_table["userM--unlock"] == False:
            print("18- unlock the user account")
        
        if flag_table["userM--add-subuids"] == False:
            print("19- add range of subordinate uids")
        
        if flag_table["userM--del-subuids"] == False:
            print("20- remove range of subordinate uids")
        
        if flag_table["userM--add-subgids"] == False:
            print("21- add range of subordinate gids")
        
        if flag_table["userM--del-subgids"] == False:
            print("22- remove range of subordinate gids")
        
        if flag_table["userM--selinux-user"] == False:
            print("23- new SELinux user mapping for the user account")
        print("0- exit")
        
        user_input = users_inputs(0,23)
        
        if user_input == 1 and flag_table["userM--badnames"] == False:
            if flag_help:
                print("""Allow names that do not conform to standards.""")
                
            user_iput = user_continue()
            if user_input:
                    
                lag_table["userM--badnames"]=True
                main_command += " --badnames"
        
        elif user_input == 2 and flag_table["userM--comment"] == False:
            if flag_help:
                print("""The new value of the user's password file comment field. It is normally modified using the chfn(1) utility.""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--comment"]=True
                main_command += ""
        
        elif user_input == 3 and flag_table["userM--home"] == False:
            if flag_help:
                print("""
    Help:
        The user's new login directory.

        If the -m option is given, the contents of the current home directory will be moved to the new home directory, which is created if it does not already
        exist. If the current home directory does not exist the new home directory will not be created.""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--home"]=True
                main_command += ""
            
        elif user_input == 4 and flag_table["userM--expiredate"] == False:
            if flag_help:
                print("""
    Help:
        The date on which the user account will be disabled. The date is specified in the format YYYY-MM-DD.

        An empty EXPIRE_DATE argument will disable the expiration of the account.

        This option requires a /etc/shadow file. A /etc/shadow entry will be created if there were none.
        flag_table["userM--expiredate"]=True
        main_command += """)
                
            user_iput = user_continue()
            if user_input:
                flag_table["userM--epxiredate"]=True
                main_command += ""
                
        elif user_input == 5 and flag_table["userM--inactive"] == False:
            if flag_help:
                print("""
    Help:
        The date on which the user account will be disabled. The date is specified in the format YYYY-MM-DD.

        An empty EXPIRE_DATE argument will disable the expiration of the account.

        This option requires a /etc/shadow file. A /etc/shadow entry will be created if there were none.
""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--inactive"]=True
                main_command += ""
            
        elif user_input == 6 and flag_table["userM--gid"] == False:
            if flag_help:
                print("""
    Help:
        """)
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--gid"]=True
                main_command += ""
        
        elif user_input == 7 and flag_table["userM--groups"] == False:
            if flag_help:
                print("""
    Help:
        The group name or number of the user's new initial login group. The group must exist.

        Any file from the user's home directory owned by the previous primary group of the user will be owned by this new group.

        The group ownership of files outside of the user's home directory must be fixed manually.

        The change of the group ownership of files inside of the user's home directory is also not done if the home dir owner uid is different from the current
        or new user id. This is a safety measure for special home directories such as /.""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--groups"]=True
                main_command += ""
            
        elif user_input == 8 and flag_table["userM--append"] == False:
            if flag_help:
                print("""
    Help:
        Add the user to the supplementary group(s). Use only with the -G(--groups) option.""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--append"]=True
                main_command += ""
            
        elif user_input == 9 and flag_table["userM--login"] == False:
            if flag_help:
                print("""
    Help:
        The name of the user will be changed from LOGIN to NEW_LOGIN. Nothing else is changed. In particular, the user's home directory or mail spool should
        probably be renamed manually to reflect the new login name.""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--login"]=True
                main_command += ""
            
        elif user_input == 10 and flag_table["userM--lock"] == False:
            if flag_help:
                print("""
    Help:
        Lock a user's password. This puts a '!' in front of the encrypted password, effectively disabling the password. You can't use this option with -p or -U.

        Note: if you wish to lock the account (not only access with a password), you should also set the EXPIRE_DATE to 1.""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--lock"]=True
                main_command += ""
        
        elif user_input == 11 and flag_table["userM--move-home"] == False:
            if flag_help:
                print("""
    Help:
        Move the content of the user's home directory to the new location. If the current home directory does not exist the new home directory will not be
        created.

        This option is only valid in combination with the -d (or --home) option.

        usermod will try to adapt the ownership of the files and to copy the modes, ACL and extended attributes, but manual changes might be needed afterwards.""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--move-home"]=True
                main_command += ""
        
        elif user_input == 12 and flag_table["userM--non-unique"] == False:
            if flag_help:
                print("""
    Help:
        When used with the -u option, this option allows to change the user ID to a non-unique value.""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--non-unique"]=True
                main_command += ""
        
        elif user_input == 13 and flag_table["userM--password"] == False:
            if flag_help:
                print("""
    Help:
        The encrypted password, as returned by crypt(3).

        Note: This option is not recommended because the password (or encrypted password) will be visible by users listing the processes.

        You should make sure the password respects the system's password policy.""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--password"]=True
                main_command += ""
        
        elif user_input == 14 and flag_table["userM--root"] == False:
            if flag_help:
                print("""
    Help:
        Apply changes in the CHROOT_DIR directory and use the configuration files from the CHROOT_DIR directory.""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--root"]=True
                main_command += ""
            
        elif user_input == 15 and flag_table["userM--prefix"] == False:
            if flag_help:
                print("""
    Help:
        Apply changes in the PREFIX_DIR directory and use the configuration files from the PREFIX_DIR directory. This option does not chroot and is intended for
        preparing a cross-compilation target. Some limitations: NIS and LDAP users/groups are not verified. PAM authentication is using the host files. No
        SELINUX support.""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--prefix"]=True
                main_command += ""
            
        elif user_input == 16 and flag_table["userM--shell"] == False:
            if flag_help:
                print("""
    Help:
        The path of the user's new login shell. Setting this field to blank causes the system to select the default login shell.""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--shell"]=True
                main_command += ""
            
        elif user_input == 17 and flag_table["userM--uid"] == False:
            if flag_help:
                print("""
    Help:
        The new numerical value of the user's ID.

        This value must be unique, unless the -o option is used. The value must be non-negative.

        The user's mailbox, and any files which the user owns and which are located in the user's home directory will have the file user ID changed
        automatically.

        The ownership of files outside of the user's home directory must be fixed manually.

        The change of the user ownership of files inside of the user's home directory is also not done if the home dir owner uid is different from the current
        or new user id. This is a safety measure for special home directories such as /.

        No checks will be performed with regard to the UID_MIN, UID_MAX, SYS_UID_MIN, or SYS_UID_MAX from /etc/login.defs.""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--uid"]=True
                main_command += ""
            
        elif user_input == 18 and flag_table["userM--unlock"] == False:
            if flag_help:
                print("""
    Help:
        Unlock a user's password. This removes the '!' in front of the encrypted password. You can't use this option with -p or -L.

        Note: if you wish to unlock the account (not only access with a password), you should also set the EXPIRE_DATE (for example to 99999, or to the EXPIRE
        value from /etc/default/useradd).""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--unlock"]=True
                main_command += ""
            
        elif user_input == 19 and flag_table["userM--add-subuids"] == False:
            if flag_help:
                print("""
    Help:
        Add a range of subordinate uids to the user's account.

        This option may be specified multiple times to add multiple ranges to a users account.

        No checks will be performed with regard to SUB_UID_MIN, SUB_UID_MAX, or SUB_UID_COUNT from /etc/login.defs.""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--add-subuids"]=True
                main_command += ""
            
        elif user_input == 20 and flag_table["userM--del-subuids"] == False:
            if flag_help:
                print("""
    Help:
        Remove a range of subordinate uids from the user's account.

        This option may be specified multiple times to remove multiple ranges to a users account. When both --del-subuids and --add-subuids are specified, the
        removal of all subordinate uid ranges happens before any subordinate uid range is added.

        No checks will be performed with regard to SUB_UID_MIN, SUB_UID_MAX, or SUB_UID_COUNT from /etc/login.defs.""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--del-subuids"]=True
                main_command += ""
            
        elif user_input == 21 and flag_table["userM--add-subgids"] == False:
            if flag_help:
                print("""
    Help:
        Add a range of subordinate gids to the user's account.

        This option may be specified multiple times to add multiple ranges to a users account.

        No checks will be performed with regard to SUB_GID_MIN, SUB_GID_MAX, or SUB_GID_COUNT from /etc/login.defs.""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--add-subgids"]=True
                main_command += ""
            
        elif user_input == 22 and flag_table["userM--del-subgids"] == False:
            if flag_help:
                print("""
    Help:
        Remove a range of subordinate gids from the user's account.

        This option may be specified multiple times to remove multiple ranges to a users account. When both --del-subgids and --add-subgids are specified, the
        removal of all subordinate gid ranges happens before any subordinate gid range is added.

        No checks will be performed with regard to SUB_GID_MIN, SUB_GID_MAX, or SUB_GID_COUNT from /etc/login.defs.""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--del-subgids"]=True
                main_command += ""
            
        elif user_input == 23 and flag_table["userM--selinux-user"] == False:
            if flag_help:
                print("""
    Help:
        The new SELinux user for the user's login.

        A blank SEUSER will remove the SELinux user mapping for user LOGIN (if any).""")
                
            user_iput = user_continue()
            if user_input:
                
                flag_table["userM--selinux-user"]=True
                main_command += ""
        
    
    kill_processes(get_all_current_processes(user_name))
    os.system(main_command)
#usemod Options:
   #1 -b, --badnames                allow bad names
   #2 -c, --comment COMMENT         new value of the GECOS field
   #3 -d, --home HOME_DIR           new home directory for the user account
   #4 -e, --expiredate EXPIRE_DATE  set account expiration date to EXPIRE_DATE
   #5 -f, --inactive INACTIVE       set password inactive after expiration to INACTIVE
   #6 -g, --gid GROUP               force use GROUP as new primary group
   #7 -G, --groups GROUPS           new list of supplementary GROUPS
   #8-a, --append                  append the user to the supplemental GROUPS mentioned by the -G option without removing the user from other groups
   #9 -l, --login NEW_LOGIN         new value of the login name
   #10 -L, --lock                    lock the user account
   #11 -m, --move-home               move contents of the home directory to the new location (use only with -d)
   #12 -o, --non-unique              allow using duplicate (non-unique) UID
   #13 -p, --password PASSWORD       use encrypted password for the new password
   #14 -R, --root CHROOT_DIR         directory to chroot into
   #15 -P, --prefix PREFIX_DIR       prefix directory where are located the /etc/* files
   #16 -s, --shell SHELL             new login shell for the user account
   #17 -u, --uid UID                 new UID for the user account
   #18 -U, --unlock                  unlock the user account
   #19 -v, --add-subuids FIRST-LAST  add range of subordinate uids
   #20 -V, --del-subuids FIRST-LAST  remove range of subordinate uids
   #21 -w, --add-subgids FIRST-LAST  add range of subordinate gids
   #22 -W, --del-subgids FIRST-LAST  remove range of subordinate gids
   #23 -Z, --selinux-user SEUSER     new SELinux user mapping for the user account