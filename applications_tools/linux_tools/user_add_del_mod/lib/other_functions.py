def users_inputs(start, finish): #general user's inputs
    flag_continue=True
    while flag_continue:                                 
        user_input = int(input("gime a number ["+ str(start) + ","+ str(finish)+ "]:"))
        if user_input >= start and user_input <= finish:
            flag_continue=False
        else:
            print("wrong input please try again")
    return user_input

def user_continue():
    while True:
        user_input=str(input("\n Do you want to continue(Y/n): "))
        if user_input == "n" or user_input == "N":
            return False
        elif user_input == "y" or user_input == "Y":
            return True
        else:
            print("wrong input please try again")
