import os
def ssh():
    
    command = "ping "
    print("""
\n ping \n
    1-simple ssh
    2-configurable ssh
    0-exit""")
    users_input = users_inputs(0,2)
    
    username = str(input("the username: "))
    ip= str(input("give me the ip: "))
    
    if users_input == 1:
        command =  command + username+"@"+ip
    else:
        command += str(input("""
 """)) + ip_or_site_to_ping
    
    os.system(command)
    
    nothing = input("press enter to exit: ")
    
    print("\n\n")