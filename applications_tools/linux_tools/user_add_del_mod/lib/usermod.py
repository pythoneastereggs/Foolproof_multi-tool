from applications_tools.linux_tools.user_add_del_mod.lib.other_functions import users_inputs, user_continue, \
    get_all_current_processes, kill_processes
import os


def usermod(main_command, flag_table):
    main_command += "mod"
    print("\nUser modify\n")
    user_name = str(input("gime a username that you want to modify from the system: "))

    print("do you want help for the commands?")
    flag_help = user_continue()

    while True:
        if not flag_table["userM--badnames"]:
            print("    1-Allow bad names")

        if not flag_table["userM--comment"]:
            print("    2- New value of the GECOS field")

        if not flag_table["userM--home"]:
            print("    3- New home directory for the user account")

        if not flag_table["userM--expiredate"]:
            print("    4- set account expiration date to EXPIRE_DATE")

        if not flag_table["userM--inactive"]:
            print("    5- set password inactive after expiration to INACTIVE")

        if not flag_table["userM--gid"]:
            print("    6- force use GROUP as new primary group")

        if not flag_table["userM--groups"]:
            print("    7- new list of supplementary GROUPS")

        if not flag_table["userM--login"]:
            print("    8- new value of the login name")

        if not flag_table["userM--lock"]:
            print("    9- lock the user account")

        if not flag_table["userM--password"]:
            print("10- use encrypted password for the new password")

        if not flag_table["userM--root"]:
            print("    11- directory to chroot into")

        if not flag_table["userM--prefix"]:
            print("    12- prefix directory where are located the /etc/* files")

        if not flag_table["userM--shell"]:
            print("    13- new login shell for the user account")

        if not flag_table["userM--uid"]:
            print("    14- new UID for the user account")

        if not flag_table["userM--unlock"]:
            print("    15- unlock the user account")

        if not flag_table["userM--add-subuids"]:
            print("    16- add range of subordinate uids")

        if not flag_table["userM--del-subuids"]:
            print("    17- remove range of subordinate uids")

        if not flag_table["userM--add-subgids"]:
            print("    18- add range of subordinate gids")

        if not flag_table["userM--del-subgids"]:
            print("    19- remove range of subordinate gids")

        if not flag_table["userM--selinux-user"]:
            print("    20- new SELinux user mapping for the user account")
        print("    0- exit")

        user_input = users_inputs(0, 20)

        if user_input == 0:
            break
        elif user_input == 1 and not flag_table["userM--badnames"]:
            if flag_help:
                print("""Allow names that do not conform to standards.""")

            user_input = user_continue()
            if user_input:
                flag_table["userM--badnames"] = True
                main_command += " --badnames"

        elif user_input == 2 and not flag_table["userM--comment"]:
            if flag_help:
                print(
                    """The new value of the user's password file comment field. It is normally modified using the chfn(1) utility.""")

            user_input = user_continue()
            if user_input:
                flag_table["userM--comment"] = True
                main_command += " --comment " + str(input("give me a comment for the account: "))

        elif user_input == 3 and not flag_table["userM--home"]:
            if flag_help:
                print("""
    Help:
        The user's new login directory.

        If the -m option is given, the contents of the current home directory will be moved to the new home directory, which is created if it does not already
        exist. If the current home directory does not exist the new home directory will not be created.""")

            user_input = user_continue()
            if user_input:

                flag_table["userM--home"] = True
                print("do you want to move the content of the user's home directory[y/n]: ")
                if flag_help:
                    print("""
    Help:
        Move the content of the user's home directory to the new location. If the current home directory does not exist the new home directory will not be
        created.

        This option is only valid in combination with the -d (or --home) option.

        usermod will try to adapt the ownership of the files and to copy the modes, ACL and extended attributes, but manual changes might be needed afterwards.""")
                user_input = user_continue()
                if user_input == "Y" or user_input == "y":
                    flag_table["userM--move-home"] = True
                    main_command += " --move-home"
                main_command += " --home" + str(input("give me the new user's home directory: "))

        elif user_input == 4 and not flag_table["userM--expiredate"]:
            if flag_help:
                print("""
    Help:
        The date on which the user account will be disabled. The date is specified in the format YYYY-MM-DD.

        An empty EXPIRE_DATE argument will disable the expiration of the account.

        This option requires a /etc/shadow file. A /etc/shadow entry will be created if there were none.
        flag_table["userM--expiredate"]=True
        main_command += """)

            user_input = user_continue()
            if user_input:
                flag_table["userM--epxiredate"] = True
                main_command += " --expiredate " + str(input("give me the EXPIRE_DATE: "))

        elif user_input == 5 and not flag_table["userM--inactive"]:
            if flag_help:
                print("""
    Help:
        The date on which the user account will be disabled. The date is specified in the format YYYY-MM-DD.

        An empty EXPIRE_DATE argument will disable the expiration of the account.

        This option requires a /etc/shadow file. A /etc/shadow entry will be created if there were none.
""")

            user_input = user_continue()
            if user_input:
                flag_table["userM--inactive"] = True
                main_command += " --inactive " + str(
                    input("give me the number of days the user account will be disabled YYYY-MM-DD: "))

        elif user_input == 6 and not flag_table["userM--gid"]:
            if flag_help:
                print("""
    Help:
        The group name or number of the user's new initial login group. The group must exist.

        Any file from the user's home directory owned by the previous primary group of the user will be owned by this new group.

        The group ownership of files outside of the user's home directory must be fixed manually.

        The change of the group ownership of files inside of the user's home directory is also not done if the home dir owner uid is different from the current
        or new user id. This is a safety measure for special home directories such as /.""")

            user_input = user_continue()
            if user_input:
                flag_table["userM--gid"] = True
                main_command += " --gid " + str(
                    input("give me the name or number of the group of the user's new initial login group: "))

        elif user_input == 7 and not flag_table["userM--groups"]:
            if flag_help:
                print("""
    Help:
        A list of supplementary groups which the user is also a member of. Each group is separated from the next by a comma, with no intervening whitespace. The
        groups are subject to the same restrictions as the group given with the -g option.

        If the user is currently a member of a group which is not listed, the user will be removed from the group. This behaviour can be changed via the -a
        option, which appends the user to the current supplementary group list.""")

            user_input = user_continue()
            if user_input:

                flag_table["userM--groups"] = True
                while True:
                    user_input = str(input(" do you want to appent the groups to the uer's account[y,n]"))
                    if (user_input == "y" or user_input == "Y") and not flag_table["userM--append"]:
                        main_command += " --append"
                        break
                    elif user_input == "n" or user_input == "N":
                        break
                    else:
                        print("wrong input please try again.")
                main_command += " --groups" + str(input("give me a list of supplementary groups (separated with a ,)"))

        elif user_input == 8 and not flag_table["userM--login"]:
            if flag_help:
                print("""
    Help:
        The name of the user will be changed from LOGIN to NEW_LOGIN. Nothing else is changed. In particular, the user's home directory or mail spool should
        probably be renamed manually to reflect the new login name.""")

            user_input = user_continue()
            if user_input:
                flag_table["userM--login"] = True
                main_command += " --login " + str(input("give me the new login for the new user: "))

        elif user_input == 9 and not flag_table["userM--lock"]:
            if flag_help:
                print("""
    Help:
        Lock a user's password. This puts a '!' in front of the encrypted password, effectively disabling the password. You can't use this option with -p or -U.

        Note: if you wish to lock the account (not only access with a password), you should also set the EXPIRE_DATE to 1.""")

            print("the --password and --unlock will be disabled.")
            user_input = user_continue()
            if user_input and not flag_table["userM--unlock"] and not flag_table["userM--password"]:
                flag_table["userM--password"] = True
                flag_table["userM--unlock"] = True
                flag_table["userM--lock"] = True
                main_command += " --lock"

        elif user_input == 10 and not flag_table["userM--password"]:
            if flag_help:
                print("""
    Help:
        The encrypted password, as returned by crypt(3).

        Note: This option is not recommended because the password (or encrypted password) will be visible by users listing the processes.

        You should make sure the password respects the system's password policy.""")

            user_input = user_continue()
            if user_input:

                print("the --lock and --unlock will be disabled.")
                user_input = user_continue()
                if user_input and not flag_table["userM--unlock"] and not flag_table["userM--lock"]:
                    flag_table["userM--unlock"] = True
                    flag_table["userM--lock"] = True
                    flag_table["userM--password"] = True
                    main_command += " --password " + str(input("give me a password: "))

        elif user_input == 11 and not flag_table["userM--root"]:
            if flag_help:
                print("""
    Help:
        Apply changes in the CHROOT_DIR directory and use the configuration files from the CHROOT_DIR directory.""")

            user_input = user_continue()
            if user_input:
                flag_table["userM--root"] = True
                main_command += " --root " + str(input("give me the CHROOT_DIR: "))

        elif user_input == 12 and not flag_table["userM--prefix"]:
            if flag_help:
                print("""
    Help:
        Apply changes in the PREFIX_DIR directory and use the configuration files from the PREFIX_DIR directory. This option does not chroot and is intended for
        preparing a cross-compilation target. Some limitations: NIS and LDAP users/groups are not verified. PAM authentication is using the host files. No
        SELINUX support.""")

            user_input = user_continue()
            if user_input:
                flag_table["userM--prefix"] = True
                main_command += " --prefix " + str(input("give me the PREFIX_DIR: "))

        elif user_input == 13 and not flag_table["userM--shell"]:
            if flag_help:
                print("""
    Help:
        The path of the user's new login shell. Setting this field to blank causes the system to select the default login shell.""")

            user_input = user_continue()
            if user_input:
                flag_table["userM--shell"] = True
                main_command += " --shell " + str(
                    input("give me the new absolute path of the shell that will be used: "))

        elif user_input == 14 and not flag_table["userM--uid"]:
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

            user_input = user_continue()
            if user_input:
                print("do you want to be a non unique value?")
                if flag_help:
                    print("""
    Help:
        When used with the -u option, this option allows to change the user ID to a non-unique value.""")
                user_input = user_continue()
                if user_input:
                    flag_table["userM--non-unique"] = True
                    main_command += " --non-unique "
                flag_table["userM--uid"] = True
                main_command += " --uid " + str(input("give me the new user's id: "))

        elif user_input == 15 and not flag_table["userM--unlock"]:
            if flag_help:
                print("""
    Help:
        Unlock a user's password. This removes the '!' in front of the encrypted password. You can't use this option with -p or -L.

        Note: if you wish to unlock the account (not only access with a password), you should also set the EXPIRE_DATE (for example to 99999, or to the EXPIRE
        value from /etc/default/useradd).""")

            user_input = user_continue()
            if user_input:

                print("the --password and --lock will be disabled.")
                user_input = user_continue()
                if user_input and not flag_table["userM--unlock"] and not flag_table["userM--password"]:
                    flag_table["userM--password"] = True
                    flag_table["userM--unlock"] = True
                    flag_table["userM--lock"] = True
                    main_command += " --unlock "

        elif user_input == 16 and not flag_table["userM--add-subuids"]:
            if flag_help:
                print("""
    Help:
        Add a range of subordinate uids to the user's account.

        This option may be specified multiple times to add multiple ranges to a users account.

        No checks will be performed with regard to SUB_UID_MIN, SUB_UID_MAX, or SUB_UID_COUNT from /etc/login.defs.""")

            user_input = user_continue()
            if user_input:
                flag_table["userM--add-subuids"] = True
                main_command += " --add-subuids " + str(
                    input("give me the range of subordinate to add uids from the user's account FIRST-LAST: "))

        elif user_input == 17 and not flag_table["userM--del-subuids"]:
            if flag_help:
                print("""
    Help:
        Remove a range of subordinate uids from the user's account.

        This option may be specified multiple times to remove multiple ranges to a users account. When both --del-subuids and --add-subuids are specified, the
        removal of all subordinate uid ranges happens before any subordinate uid range is added.

        No checks will be performed with regard to SUB_UID_MIN, SUB_UID_MAX, or SUB_UID_COUNT from /etc/login.defs.""")

            user_input = user_continue()
            if user_input:
                flag_table["userM--del-subuids"] = True
                main_command += " --del-subuids " + str(
                    input("give me the range of subordinate to remove uids from the user's account FIRST-LAST: "))

        elif user_input == 18 and not flag_table["userM--add-subgids"]:
            if flag_help:
                print("""
    Help:
        Add a range of subordinate gids to the user's account.

        This option may be specified multiple times to add multiple ranges to a users account.

        No checks will be performed with regard to SUB_GID_MIN, SUB_GID_MAX, or SUB_GID_COUNT from /etc/login.defs.""")

            user_input = user_continue()
            if user_input:
                flag_table["userM--add-subgids"] = True
                main_command += " --add-subgids " + str(
                    input("give me the range of subordinate gids to add gids from the user's account FIRST-LAST: "))

        elif user_input == 19 and not flag_table["userM--del-subgids"]:
            if flag_help:
                print("""
    Help:
        Remove a range of subordinate gids from the user's account.

        This option may be specified multiple times to remove multiple ranges to a users account. When both --del-subgids and --add-subgids are specified, the
        removal of all subordinate gid ranges happens before any subordinate gid range is added.

        No checks will be performed with regard to SUB_GID_MIN, SUB_GID_MAX, or SUB_GID_COUNT from /etc/login.defs.""")

            user_input = user_continue()
            if user_input:
                flag_table["userM--del-subgids"] = True
                main_command += " --del-subgids " + str(
                    input("give me the range of subordinate gids to remove uids from the user's account FIRST-LAST: "))

        elif user_input == 20 and not flag_table["userM--selinux-user"]:
            if flag_help:
                print("""
    Help:
        The new SELinux user for the user's login.

        A blank SEUSER will remove the SELinux user mapping for user LOGIN (if any).""")

            user_input = user_continue()
            if user_input:
                flag_table["userM--selinux-user"] = True
                main_command += " --selinux-user " + str(input("give me the SELinux user mapping: "))

    if main_command != "sudo usermod":
        kill_processes(get_all_current_processes(user_name))
        os.system(main_command)
# usemod Options:
# 1 -b, --badnames                allow bad names
# 2 -c, --comment COMMENT         new value of the GECOS field
# 3 -d, --home HOME_DIR           new home directory for the user account
# 4 -e, --expiredate EXPIRE_DATE  set account expiration date to EXPIRE_DATE
# 5 -f, --inactive INACTIVE       set password inactive after expiration to INACTIVE
# 6 -g, --gid GROUP               force use GROUP as new primary group
# 7 -G, --groups GROUPS           new list of supplementary GROUPS
# 8-a, --append                  append the user to the supplemental GROUPS mentioned by the -G option without removing the user from other groups
# 9 -l, --login NEW_LOGIN         new value of the login name
# 10 -L, --lock                    lock the user account
# 11 -m, --move-home               move contents of the home directory to the new location (use only with -d)
# 12 -o, --non-unique              allow using duplicate (non-unique) UID
# 13 -p, --password PASSWORD       use encrypted password for the new password
# 14 -R, --root CHROOT_DIR         directory to chroot into
# 15 -P, --prefix PREFIX_DIR       prefix directory where are located the /etc/* files
# 16 -s, --shell SHELL             new login shell for the user account
# 17 -u, --uid UID                 new UID for the user account
# 18 -U, --unlock                  unlock the user account
# 19 -v, --add-subuids FIRST-LAST  add range of subordinate uids
# 20 -V, --del-subuids FIRST-LAST  remove range of subordinate uids
# 21 -w, --add-subgids FIRST-LAST  add range of subordinate gids
# 22 -W, --del-subgids FIRST-LAST  remove range of subordinate gids
# 23 -Z, --selinux-user SEUSER     new SELinux user mapping for the user account
