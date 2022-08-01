import os
import subprocess
from applications_tools.linux_tools.user_add_del_mod.lib.other_functions import users_inputs
from applications_tools.linux_tools.ping.lib.opt_general import options

def ping():
    flag_table={"-4":False,"-6":False,"-a":False,"-A":False,"-b":False,"-B":False,"-c":False,"-d":False,"-D":False,"-f":False,"-F":False,"-i":False
                ,"-I":False,"-l":False,"-L":False,"-m":False,"-M":False,"-n":False,"-O":False,"-p":False,"-q":False,"-Q":False,"-r":False,"-R":False
                ,"-s":False,"-S":False,"-t":False,"-T":False,"-U":False,"-v":False,"-w":False,"-W":False}
    
    main_command = "ping "
    print("""
\n ping \n
    1-Ping infinite (Ctrl+c to stop)
    2-Configurable ping
    3-Chad ping XD
    0-exit""")
    users_input = users_inputs(0,3)
    
    ip_or_site_to_ping = str(input("Give me a Site or an ip to ping: "))
    
    if users_input == 1:
        main_command += ip_or_site_to_ping
        
    elif user_input == 2:
        options(main_command, flag_table, ip_or_site_to_ping)
        
    elif users_input == 3:
        main_command += str(input("Give me commands: ")) + ip_or_site_to_ping
    
    os.system(main_command)
    
    nothing = input("press enter to exit: ")
    
    print("\n\n")