import os

def flags_zero():
    flag_table={"bad names" : False, "base dir" : False, "btrfs subvolume home" : False, "comment" : False,
          "home dir" : False, "defaults" : False, "expiredate" : False, "inactive" : False, "gid" : False,
          "groups" : False, "skel" : False, "key" : False, "no log init" : False, "create home" : False, 
          "no create home" : False, "no user group" : False, "non-unique" : False, "password" : False, 
          "system" : False, "root" : False, "prefix" : False, "shell" : False, "uid" : False, 
          "user group" : False, "selinux user" : False, "extra users" : False}

    
def users_inputs(users_input, start, finish): #general user's inputs
    flag=True
    while flag:
        user_input = int(input("gime a number [1,3]:"))
        if user_input >= start and user_input <= finish:
            flag=False
        else:
            print("wrong input please try again")
    

main_user="sudo user"

print("""In dev release is not have the users automaticly displayed
probablly in the other versions will have all the modifyable users???\n\n""")


print("""what you want to do in user?
1-add a user?
2-modify a user?
3-delete a user?""")


users_inputs(users_input, 1, 3)

if user_input == 1:
    
    main_user+="add"
    user_name=str(input("gime a username that you want to add to the system: "))
    print("menu 2")
    print("""
1-procceed as all default
2-manually control(???)
""")
    
    users_inputs(user_input, 1, 2)

    if user_input == 1:
        
        main_user = main_user + " --shell /bin/bash --create-home --system " + user_name + " && echo'' && sudo passwd " + user_name
        print(main_user)
        os.system(main_user)
    elif user_input == 2:
        flags_zero()
        print("""
What do you whant to do with this new user?\n
1-bad names do not check for bad names
2-base directory for the home directory of the new account
3-use BTRFS subvolume for home directory
4-GECOS field of the new account
5-home directory of the new account
6-print or change default useradd configuration
7-expiration date of the new account
8-password inactivity period of the new account
9-name or ID of the primary group of the new account
10-list of supplementary groups of the new account
11-use this alternative skeleton directory
12-override /etc/login.defs defaults
13-do not add the user to the lastlog and faillog databases
14-create the user's home directory
15-do not create the user's home directory
16-do not create a group with the same name as the user
17-allow to create users with duplicate (non-unique) UID
18-encrypted password of the new account
19-create a system account
20-directory to chroot into
21-prefix directory where are located the /etc/* files
22-login shell of the new account
23-user ID of the new account
24-create a group with the same name as the user
25-use a specific SEUSER for the SELinux user mapping
26-Use the extra users database
""")
        users_inputs(user_input, 1, 26)
        if user_input == 1:
            flag_table.update({"bad names" : True})
        elif user_input == 2:
            flag_table.update({"base dir" : True})
        elif user_input == 3:
            flags_table.update({"btrfs subvolume home" : True})
        elif user_input == 4:
            flag_table.update({"comment" : True})
        elif user_input == 5:
            flag_table.update({"home dir" : True})
        elif user_input == 6:
            flag_table.update({"defaults" : True})
        elif user_input == 7:
            flag_table.update({"expiredate" : True})
        elif user_input == 8:
            flag_table.update({"inactive" : True})
        elif user_input == 9:
            flag_table.update({"gid" : True})
        elif user_input == 10:
            flag_table.update({"groups" : True})
        elif user_input == 11:
            flag_table.update({"skel" : True})
        elif user_input == 12:
            flag_table.update({"key" : True})
        elif user_input == 13:
            flag_table.update({"no log init" : True})
        elif user_input == 14:
            flag_table.update({"create home" : True})
        elif user_input == 15:
            flag_table.update({"no create home" : True})
        elif user_input == 16:
            flag_table.update({"no user group" : True})
        elif user_input == 17:
            flag_table.update({"non-unique" : True})
        elif user_input == 17:
            flag_table.update({"password" : True})
        elif user_input == 18:
            flag_table.update({"system" : True})
        elif user_input == 19:
            flag_table.update({"root" : True})
        elif user_input == 20:
            flag_table.update({"prefix" : True})
        elif user_input == 21:
            flag_table.update({"shell" : True})
        elif user_input == 22:
            flag_table.update({"uid" : True})
        elif user_input == 23:
            flag_table.update({"user group" : True})
        elif user_input == 24:
            flag_table.update({"selinux user" : True})
        elif user_input == 25:
            flag_table.update({"extra users" : True})
        elif user_input == 26:
            flag_table.update({"" : True})
    
elif user_input == 2:
    
    main_user+="mod"
    user_name=str(input("gime a username that you want to modify from the system: "))

elif user_input == 3:
    
    main_user+="del"
    user_name=str(input("gime a username that you want to delete from the system: "))
    
print("end")

#Options
  #    --badnames                do not check for bad names
  #-b, --base-dir BASE_DIR       base directory for the home directory of the
  #                              new account
  #    --btrfs-subvolume-home    use BTRFS subvolume for home directory
  #-c, --comment COMMENT         GECOS field of the new account
  #-d, --home-dir HOME_DIR       home directory of the new account
  #-D, --defaults                print or change default useradd configuration
  #-e, --expiredate EXPIRE_DATE  expiration date of the new account
  #-f, --inactive INACTIVE       password inactivity period of the new account
  #-g, --gid GROUP               name or ID of the primary group of the new
  #                              account
  #-G, --groups GROUPS           list of supplementary groups of the new
  #                              account
  #-k, --skel SKEL_DIR           use this alternative skeleton directory
  #-K, --key KEY=VALUE           override /etc/login.defs defaults
  #-l, --no-log-init             do not add the user to the lastlog and
  #                              faillog databases
  #-m, --create-home             create the user's home directory
  #-M, --no-create-home          do not create the user's home directory
  #-N, --no-user-group           do not create a group with the same name as
  #                              the user
  #-o, --non-unique              allow to create users with duplicate
  #                              (non-unique) UID
  #-p, --password PASSWORD       encrypted password of the new account
  #-r, --system                  create a system account
  #-R, --root CHROOT_DIR         directory to chroot into
  #-P, --prefix PREFIX_DIR       prefix directory where are located the /etc/* files
  #-s, --shell SHELL             login shell of the new account
  #-u, --uid UID                 user ID of the new account
  #-U, --user-group              create a group with the same name as the user
  #-Z, --selinux-user SEUSER     use a specific SEUSER for the SELinux user mapping
  #    --extrausers              Use the extra users database