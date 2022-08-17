import subprocess
import os   
from termcolor import colored

def users_inputs(start, finish):
    flag_continue = True
    while flag_continue:
        user_input = int(input("gime a number [" + str(start) + "," + str(finish) + "]:"))
        if start <= user_input <= finish:
            flag_continue = False
        else:
            print("wrong input please try again")
    return user_input

def user_continue():
    while True:
        user_input = str(input("\n Do you want to continue(Y/n): "))
        if user_input == "n" or user_input == "N":
            return False
        elif user_input == "y" or user_input == "Y" or user_input == "":
            return True
        else:
            print("wrong input please try again")

def get_all_current_processes(username):
    
    flag = False
    
    command = "ps -u " + username + " -o pid"
    current_processes = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.readlines()

    for i in range(len(current_processes)):
        current_processes[i] = str(current_processes[i]).replace("b", "")
        current_processes[i] = str(current_processes[i]).replace("'", "")
        current_processes[i] = str(current_processes[i]).replace(" ", "")
        current_processes[i] = str(current_processes[i]).replace("n", "/")
        current_processes[i] = str(current_processes[i]).replace("\/", "")
        if i > 0:
            current_processes[i] = int(current_processes[i])
            flag = True
        if flag == True:
            print(
                "\n current user(" + username + ") processes are fount! \n I will terminate them for the changes to take place!")
    return current_processes


def kill_processes(table_of_pids):
    for i in range(len(table_of_pids)):
        if table_of_pids[i] != "PID":
            command = "sudo kill -q 9 " + str(table_of_pids[i])
            print("command: " + command)
            os.system(command)


def enabled_option(text):
    print(colored(text,"green"))

def disabled_option(text):
    print(colored(text,"red"))