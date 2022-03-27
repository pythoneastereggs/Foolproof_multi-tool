from random import choice

###################################################################################
# ένα απλό pasword manager στο οποίο ο χρήστης μπορεί να δημιουργίσει έναν κωδικό.#
###################################################################################

def users_inputs(start, finish): #general user's inputs
    flag_continue=True
    while flag_continue:                                 
        user_input = int(input("gime a number ["+ str(start) + ","+ str(finish)+ "]:"))
        if user_input >= start and user_input <= finish:
            flag_continue=False
        else:
            print("wrong input please try again")
    return user_input

def pass_lenght():
    while True:
        pass_len=int(input("give me how many characters you want to have in your password (greater than 8): "))
        if pass_len >= 8:
            break
        else:
            print("password at least 8 characters")
    return pass_len

print("""
1-strong generator
2-configurable generator
0-exit""")

user_input=users_inputs(0, 2)
    
password=""
if user_input == 1:
    table_strong= "abcdefghigklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(?)_+-=*/\'\";:[{]}.<,>|`~"

    pass_len=pass_lenght()

    for i in range(pass_len):
        password+=choice(table_strong)
    print("password= ", password)
    
elif user_input == 2:
    table_lower="abcdefghigklmnopqrstuvwxyz"
    table_upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table_numbers="0123456789"
    table_special_char="`~!@#$%^&*)(-_=+{[}]\|\"\'/?.>,<"
   
    flag_table_lower=False
    flag_table_upper=False
    flag_table_numbers=False
    flag_table_special_char=False
    
    while True:
        if flag_table_lower == False:
            print("\n1-use lower")   
        if flag_table_upper == False:    
            print("2-use upper")
        if flag_table_numbers == False:
            print("3-use numbers")
        if flag_table_special_char== False:
            print("4-use special characters")
        print("0-exit")
        user_input=users_inputs(0,4)
        
        if user_input == 0:
            break
        elif user_input == 1:
            flag_table_lower=True
        elif user_input == 2:
            flag_table_upper=True
        elif user_input == 3:
            flag_table_numbers=True
        elif user_input == 4:
            flag_table_special_char=True
        if flag_table_lower == True and flag_table_upper  == True and flag_table_numbers == True and flag_table_special_char ==True :
            break
        
    if flag_table_upper or flag_table_lower or flag_table_numbers or flag_table_special_char:
        final_table=""
        if flag_table_lower:
            final_table+=table_lower
        if flag_table_upper:
            final_table+=table_upper
        if flag_table_numbers:
            final_table+=table_numbers
        if flag_table_special_char:
            final_table+=table_special_char

        pass_len=pass_lenght()

        for i in range(pass_len):
            password+=choice(final_table)
        print("password= ", password)