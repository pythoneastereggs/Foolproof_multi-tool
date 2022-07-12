from applications_tools.linux_tools.user_add_del_mod.lib.other_functions import users_inputs, user_continue, get_all_current_processes, kill_processes
import os
import subprocess


def userdel(main_command, flag_table):

    global flag_help
    main_command += "del"
    print("\nUser Delete\n")
    user_name = str(input("gime a username that you want to delete from the system: "))

    print("""1- Simple account dellition
2- Configurable account de1lition
""")

    user_input = users_inputs(1, 2)

    if user_input == 1:

        main_command += " " + user_name

    elif user_input == 2:

        print("do you want help for the commands?")
        flag_help = user_continue()
        
        while True:
            if not flag_table["usrD--force"]:
                print("1-force removal of files, even if not owned by user")

            if not flag_table["usrD--remove"]:
                print("2-remove home directory and mail spool")

            if not flag_table["usrD--root"]:
                print("3-directory to chroot into")

            if not flag_table["usrD--prefix"]:
                print("4-prefix directory where are located the /etc/* files")

            if not flag_table["usrD--selinux-user"]:
                print("5-remove any SELinux user mapping for the user")

            print("0-exit and run the command")

            user_input = users_inputs(0, 5)

            if user_input == 1 and flag_table["userD--force"] == False:

                if flag_help:
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

                what_to_do = user_continue()
                if what_to_do:
                    flag_table["userD--force"] = True
                    main_command += " -- force "

                    if str(input("User group Enable?(yes or no): ")) == "yes":
                        main_command += "USERGROUPS_ENAB true"
                    else:
                        main_command += "USERGROUPS_ENAB false"

            elif user_input == 2 and flag_table["userD--remove"] == False:

                if flag_help:
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

                what_to_do = user_continue()
                if what_to_do:
                    flag_table["usrD--remove"] = True
                    main_command += " --remove " + str(input("give me the configuration: "))

            elif user_input == 3 and not flag_table["userD--root"]:

                if flag_help:
                    print("""
    Apply changes in the CHROOT_DIR directory and use the configuration files from the CHROOT_DIR directory.""")

                what_to_do = user_continue()
                if what_to_do:
                    flag_table["usrD--root"] = True
                    main_command += " --root"

            elif user_input == 4 and not flag_table["userD--prefix"]:

                if flag_help:
                    print("""
    Apply changes in the PREFIX_DIR directory and use the configuration files from the PREFIX_DIR directory. This option does not chroot
    and is intended for preparing a cross-compilation target. Some limitations: NIS and LDAP users/groups are not verified. PAM
    authentication is using the host files. No SELINUX support.""")

                what_to_do = user_continue()
                if what_to_do:
                    flag_table["usrD--prefix"] = True
                    main_command += " --prefix"

            elif user_input == 5 and not flag_table["userD--selinux-user"]:

                if flag_help:
                    print("""
    Remove any SELinux user mapping for the user's login.""")

                what_to_do = user_continue()
                if what_to_do:
                    flag_table["usrD--selinux-user"] = True
                    main_command += " --selinux-user"

            elif user_input == 0:
                break
            
    kill_processes(get_all_current_processes(user_name))
    os.system(main_command)

# userdel Options:
# -f, --force                   force some actions that would fail otherwise e.g. removal of user still logged in or files, even if not owned by the user
# -r, --remove                  remove home directory and mail spool
# -R, --root CHROOT_DIR         directory to chroot into
# -P, --prefix PREFIX_DIR       prefix directory where are located the /etc/* files
# -Z, --selinux-user Remove any SELinux user mapping for the user's login.
