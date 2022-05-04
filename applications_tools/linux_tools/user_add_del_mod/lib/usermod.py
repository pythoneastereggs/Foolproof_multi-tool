from lib.other_functions import users_inputs, user_continue
import os
def usermod(main_command, flag_table):
    main_command+="mod"
    user_name=str(input("gime a username that you want to modify from the system: "))

    if flag_table["usrM--badnames"] == False:
        print("1-Allow bad names")
    
    if flag_table["userM--"] == False:
        print("2-")
    
    if flag_table["userM--"] == False:
        print("3-")
    
    if flag_table["userM--"] == False:
        print("4-")
    
    if flag_table["userM--"] == False:
        print("5-")
    
    if flag_table["userM--"] == False:
        print("6-")
    
    if flag_table["userM--"] == False:
        print("7-")
    
    if flag_table["userM--"] == False:
        print("8-")
    
    if flag_table["userM--"] == False:
        print("9-")
    
    if flag_table["userM--"] == False:
        print("10-")
    
    if flag_table["userM--"] == False:
        print("11-")
    
    if flag_table["userM--"] == False:
        print("12-")
    
    if flag_table["userM--"] == False:
        print("13-")
    
    if flag_table["userM--"] == False:
        print("14-")
    
    if flag_table["userM--"] == False:
        print("15-")
    
    if flag_table["userM--"] == False:
        print("16-")
    
    if flag_table["userM--"] == False:
        print("17-")
    
    if flag_table["userM--"] == False:
        print("18-")
    
    if flag_table["userM--"] == False:
        print("19-")
    
    if flag_table["userM--"] == False:
        print("20-")
    
    if flag_table["userM--"] == False:
        print("21-")
    
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