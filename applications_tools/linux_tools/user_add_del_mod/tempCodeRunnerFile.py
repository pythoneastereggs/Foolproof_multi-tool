def users_inputs(users_input, start, finish): #general user's inputs
    flag_continue=True
    while flag_continue:                                 
        user_input = int(input("gime a number [", start, ",", finish, "]:"))
        if user_input >= start and user_input <= finish:
            flag_continue=False
        else:
            print("wrong input please try again")