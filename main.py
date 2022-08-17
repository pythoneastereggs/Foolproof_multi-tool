from applications_tools.linux_tools.user_add_del_mod.main_user_add_del_mod import user_add_del_mod
from applications_tools.linux_tools.system_update.main_sys_update import sys_update
from applications_tools.linux_tools.install_packages.main_sys_install_packages import package_installer
from applications_tools.linux_tools.password_generator.main_password_generator import password_generator
from applications_tools.linux_tools.calculator.main_calculator import calculator
from applications_tools.linux_tools.Currency_Converter.main_converter import currency_converter
from applications_tools.linux_tools.Web_checker.web_check import website_cheker
from applications_tools.linux_tools.ping.main_ping import ping
from applications_tools.linux_tools.ssh.ssh import ssh
from applications_tools.games.main_games import games

from applications_tools.linux_tools.user_add_del_mod.lib.other_functions import users_inputs

print("\nWelcome to Fool proof Multitool\n")
while True:
    print("""What do you want to do?
    1- password generate
    2- user add, delete, modify
    3- ping a server
    4- ssh to a server
    5- system update
    6- calculate staff
    7- install packages
    8- currency Converter
    9- website cheaker
    10- games...
    0- exit""")
    
    user_input = users_inputs(0, 10)
    if user_input == 0:
        break
    elif user_input == 1:
        password_generator()
    elif user_input == 2:
        user_add_del_mod()
    elif user_input == 3:
        ping()
    elif user_input == 4:
        ssh()
    elif user_input == 5:
        sys_update()
    elif user_input == 6:
        calculator()
    elif user_input == 7:
        package_installer()
    elif user_input == 8:
        currency_converter()
    elif user_input == 9:
        website_cheker()
    elif user_input == 10:
        games()
#test
