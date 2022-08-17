import os
import subprocess
from applications_tools.linux_tools.user_add_del_mod.lib.other_functions import (
    user_continue, users_inputs)
from termcolor import colored


def options(main_command, flag_table, ip_or_site_to_ping):
        
    print("do you want help for the ping commands?")
    flag_help = user_continue()
    if  flag_help:
        print("""
    DESCRIPTION:
        ping uses the ICMP protocol's mandatory ECHO_REQUEST datagram to
        elicit an ICMP ECHO_RESPONSE from a host or gateway. ECHO_REQUEST
        datagrams (“pings”) have an IP and ICMP header, followed by a
        struct timeval and then an arbitrary number of “pad” bytes used
        to fill out the packet.

        ping works with both IPv4 and IPv6. Using only one of them
        explicitly can be enforced by specifying -4 or -6.

        ping can also send IPv6 Node Information Queries (RFC4620).
        Intermediate hops may not be allowed, because IPv6 source routing
        was deprecated (RFC5095).""")
    print("\nPing\n")
    #################################
   # command output                #
  # active (green) or             #
 # not permited/not active (red) #
#################################
    
    while True:                                    # disabled = red = not active / not permited
        if not flag_table["-4"]:                   # enabled = green = active and ready to use
            print("1-\033[0;49;31m Use IPv4 only") # print red text (\003[0;49;31m {and the text})
        elif flag_table["-4"]:
            print("1-\033[0;49;32m Use IPv4 only") # print green text (\003[0;49;32m {and the text})
        
        if not flag_table["-6"]:
            print("2-\033[0;49;31m Use IPn6 only")
        elif flag_table["-6"]:
            print("2-\033[0;49;32m Use IPn6 only")

        if not flag_table["-a"]:    
            print("3-\033[0;49;31m Audible ping")
        elif flag_table["-a"]:
            print("3-\033[0;49;32m Audible ping")

        if not flag_table["-A"]:
            print("4-\033[0;49;31m Adaptive ping")
        elif flag_table["-A"]:
            print("4-\033[0;49;32m Adaptive ping")

        if not flag_table["-b"]:
            print("5-\033[0;49;31m Allow pinging a broadcast address")
        elif flag_table["-b"]:
            print("5-\033[0;49;32m Allow pinging a broadcast address")

        if not flag_table["-B"]:
            print("6-\033[0;49;31m Do not allow ping to change source address of probes")
        elif flag_table["-B"]:
            print("6-\033[0;49;32m Do not allow ping to change source address of probes")

        if not flag_table["-c"]:
            print("7-\033[0;49;31m Stop after sending count ECHO_REQUEST packets")
        elif flag_table["-c"]:
            print("7-\033[0;49;32m Stop after sending count ECHO_REQUEST packets")

        if not flag_table["-d"]:
            print("8-\033[0;49;31m  Set the SO_DEBUG option on the socket being used")
        elif flag_table["-d"]:
            print("8-\033[0;49;32m  Set the SO_DEBUG option on the socket being used")

        if not flag_table["-D"]:
            print("9-\033[0;49;31m  Print timestamp before each line")
        elif flag_table["-D"]:
            print("9-\033[0;49;32m  Print timestamp before each line")

        if not flag_table["-f"]:
            print("10-\033[0;49;31m Flood ping")
        elif flag_table["-f"]:
            print("10-\033[0;49;32m Flood ping")

        if not flag_table["-F"]:
            print("""11-\033[0;49;31m IPv6 only. Allocate and set 20 bit flow label (in hex) on echo request packets. If value is
zero, kernel allocates random flow label.""")
        elif flag_table["-F"]:
            print("""11-\033[0;49;32m IPv6 only. Allocate and set 20 bit flow label (in hex) on echo request packets. If value is
zero, kernel allocates random flow label.""")
            
        if not flag_table["-i"]:
            print("12-\033[0;49;31m Wait interval seconds between sending each packet")
        elif flag_table["-i"]:
            print("12-\033[0;49;32m Wait interval seconds between sending each packet")

        if not flag_table["-I"]:
            print("13-\033[0;49;31m either interface name or address")
        elif flag_table["-I"]:
            print("13-\033[0;49;32m either interface name or address")

        if not flag_table["-l"]:
            print("14-\033[0;49;31m send preload number of packages while waiting replies")
        elif flag_table["-l"]:
            print("14-\033[0;49;32m send preload number of packages while waiting replies")

        if not flag_table["-L"]:
            print("15-\033[0;49;31m suppress loopback of multicast packets")
        elif flag_table["-L"]:
            print("15-\033[0;49;32m suppress loopback of multicast packets")

        if not flag_table["-m"]:
            print("16-\033[0;49;31m tag the packets going out")
        elif flag_table["-m"]:
            print("16-\033[0;49;32m tag the packets going out")

        if not flag_table["-M"]:
            print("17-\033[0;49;31m Select Path MTU Discovery strategy")
        elif flag_table["-M"]:
            print("17-\033[0;49;32m Select Path MTU Discovery strategy")

        if not flag_table["-n"]:
            print("18-\033[0;49;31m no dns name resolution")
        elif flag_table["-n"]:
            print("18-\033[0;49;32m no dns name resolution")

        if not flag_table["-O"]:
            print("19\033[0;49;31m report outstanding replies")
        elif flag_table["-O"]:
            print("19\033[0;49;32m report outstanding replies")

        if not flag_table["-p"]:
            print("20-\033[0;49;31m contents of padding byte")
        elif flag_table["-p"]:
            print("20-\033[0;49;32m contents of padding byte")

        if not flag_table["-q"]:
            print("21\033[0;49;31m quiet output")
        elif flag_table["-q"]:
            print("21\033[0;49;32m quiet output")

        if not flag_table["-Q"]:
            print("22-\033[0;49;31m use quality of service tclass bits")
        elif flag_table["-Q"]:
            print("22-\033[0;49;32m use quality of service tclass bits")

        if not flag_table["-r"]:
            print("23-\033[0;49;31m Bypass the normal routing tables and send directly to a host on an attached interface")
        elif flag_table["-r"]:
            print("23-\033[0;49;32m Bypass the normal routing tables and send directly to a host on an attached interface")

        if not flag_table["-R"]:
            print("24-\033[0;49;31m ping only. Record route.")
        elif flag_table["-R"]:
            print("24-\033[0;49;32m ping only. Record route.")

        if not flag_table["-s"]:
            print("25-\033[0;49;31m Specifies the number of data bytes to be sent")
        elif flag_table["-s"]:
            print("25-\033[0;49;32m Specifies the number of data bytes to be sent")

        if not flag_table["-S"]:
            print("26-\033[0;49;31m Set socket sndbuf")
        elif flag_table["-S"]:
            print("26-\033[0;49;32m Set socket sndbuf")

        if not flag_table["-t"]:
            print("27\033[0;49;31m define time to live")
        elif flag_table["-t"]:
            print("27\033[0;49;32m define time to live")

        if not flag_table["-T"]:
            print("28-\033[0;49;31m Set special IP timestamp options")
        elif flag_table["-T"]:
            print("28-\033[0;49;32m Set special IP timestamp options")

        if not flag_table["-U"]:
            print("29-\033[0;49;31m Print full user-to-user latency (the old behaviour)")
        elif flag_table["-U"]:
            print("29-\033[0;49;32m Print full user-to-user latency (the old behaviour)")

        if not flag_table["-v"]:
            print("30-\033[0;49;31m Verbose output")
        elif flag_table["-v"]:
            print("30-\033[0;49;32m Verbose output")

        if not flag_table["-w"]:
            print("""31-\033[0;49;31m Specify a timeout, in seconds, before ping exits regardless of how many packets have been sent
or received""")
        elif flag_table["-w"]:
            print("""31-\033[0;49;32m Specify a timeout, in seconds, before ping exits regardless of how many packets have been sent
or received""")

        if not flag_table["-W"]:
            print("32-\033[0;49;31m Time to wait for a response, in seconds")
        elif flag_table["-W"]:
            print("32-\033[0;49;32m Time to wait for a response, in seconds")
        print("0-exit")
        user_input = users_inputs(0, 32)
        ##################
       #  command logic #
      ################## 
        if user_input == 0:
            break
        elif user_input == 1:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-4"] = not flag_table["-4"]

        elif user_input == 2:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-6"] = not flag_table["-6"]

        elif user_input == 3:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-a"] = not flag_table["-a"]

        elif user_input == 4:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-A"] = not flag_table["-A"]

        elif user_input == 5:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-b"] = not flag_table["-b"]

        elif user_input == 6:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-B"] = not flag_table["-B"]

        elif user_input == 7:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-c"] = not flag_table["-c"]

        elif user_input == 8:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-d"] = not flag_table["-d"]

        elif user_input == 9:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-D"] = not flag_table["-D"]

        elif user_input == 10:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-f"] = not flag_table["-f"]

        elif user_input == 11:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-F"] = not flag_table["-F"]

        elif user_input == 12:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-i"] = not flag_table["-i"]

        elif user_input == 13:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-I"] = not flag_table["-I"]

        elif user_input == 14:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-l"] = not flag_table["-l"]

        elif user_input == 15:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-L"] = not flag_table["-L"]

        elif user_input == 16:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-m"] = not flag_table["-m"]

        elif user_input == 17:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-M"] = not flag_table["-M"]

        elif user_input == 18:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-n"] = not flag_table["-n"]

        elif user_input == 19:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-O"] = not flag_table["-O"]

        elif user_input == 20:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-p"] = not flag_table["-p"]

        elif user_input == 21:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-q"] = not flag_table["-q"]

        elif user_input == 22:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-Q"] = not flag_table["-Q"]

        elif user_input == 23:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-r"] = not flag_table["-r"]

        elif user_input == 24:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-R"] = not flag_table["-R"]

        elif user_input == 25:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-s"] = not flag_table["-s"]

        elif user_input == 26:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-S"] = not flag_table["-S"]

        elif user_input == 27:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-T"] = not flag_table["-T"]

        elif user_input == 28:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-U"] = not flag_table["-U"]

        elif user_input == 29:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-v"] = not flag_table["-v"]

        elif user_input == 30:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-w"] = not flag_table["-w"]

        elif user_input == 31:
            if flag_help:
                print("""
    Help:
        """)

            flag_table["-W"] = not flag_table["-W"]

    ###################
   # command compile #
  ###################
    if flag_table["-4"]:
        main_command += "-4 "
    if flag_table["-6"]:
        main_command += "-6 "
    if flag_table["-a"]:
        main_command += "-a "
    if flag_table["-A"]:
        main_command += "-A "
    if flag_table["-b"]:
        main_command += "-b "
    if flag_table["-B"]:
        main_command += "-B "
    if flag_table["-c"]:
        main_command += "-c "
    if flag_table["-d"]:
        main_command += "-d "
    if flag_table["-D"]:
        main_command += "-D "
    if flag_table["-f"]:
        main_command += "-f "
    if flag_table["-F"]:
        main_command += "-F "
    if flag_table["-i"]:
        main_command += "-i "
    if flag_table["-I"]:
        main_command += "-I "
    if flag_table["-l"]:
        main_command += "-l "
    if flag_table["-L"]:
        main_command += "-L "
    if flag_table["-m"]:
        main_command += "-m "
    if flag_table["-M"]:
        main_command += "-M "
    if flag_table["-n"]:
        main_command += "- "
    if flag_table["-O"]:
        main_command += "-O "
    if flag_table["-p"]:
        main_command += "-p "
    if flag_table["-q"]:
        main_command += "-q "
    if flag_table["-Q"]:
        main_command += "-Q "
    if flag_table["-r"]:
        main_command += "-r "
    if flag_table["-R"]:
        main_command += "-R "
    if flag_table["-s"]:
        main_command += "-s"
    if flag_table["-S"]:
        main_command += "-S "
    if flag_table["-t"]:
        main_command += "-t "
    if flag_table["-T"]:
        main_command += "-T "
    if flag_table["-U"]:
        main_command += "-U "
    if flag_table["-v"]:
        main_command += "-v "
    if flag_table["-w"]:
        main_command += "-w "
            