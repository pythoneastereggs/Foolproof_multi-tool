from random import choice


def password_generator():
    ###################################################################################################
    # ένα απλό pasword generator στο οποίο ο χρήστης μπορεί να δημιουργίσει έναν κωδικό αρκετά ασφαλές#
    ###################################################################################################

    def users_inputs(start, finish):  # general user's inputs

        global user_input
        flag_continue = True  # https://fixrelationshipnow.net/wp-content/uploads/2020/03/hello-there-general-kenobi.jpg
        while flag_continue:
            user_input = int(input("gime a number [" + str(start) + "," + str(finish) + "]:"))
            if start <= user_input <= finish:
                flag_continue = False
            else:
                print("wrong input please try again")
        return user_input

    def pass_lenght():

        while True:
            pass_len = int(input("give me how many characters you want to have in your password (greater than 8): "))
            if pass_len >= 8:
                break
            else:
                print("password at least 8 characters")
        return pass_len

    print("""
    1-strong generator
    2-configurable generator
    0-exit""")

    user_input = users_inputs(0, 2)

    password = ""
    if user_input == 1:  # strong table

        table_strong = "abcdefghigklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(?)_+-=*/\'\";:[{]}.<,>|`~"

        pass_len = pass_lenght()

        for i in range(pass_len):
            password += choice(table_strong)
        print("password= ", password)

    elif user_input == 2:

        table_lower = "abcdefghigklmnopqrstuvwxyz"
        table_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        table_numbers = "0123456789"
        table_special_char = "`~!@#$%^&*)(-_=+}{][\|\"\'/?.>,<"

        flag_table_lower = False
        flag_table_upper = False
        flag_table_numbers = False
        flag_table_special_char = False

        while True:
            # selectivly tables in whatever order
            if not flag_table_lower:
                print("\n1-use lower")
            if not flag_table_upper:
                print("2-use upper")
            if not flag_table_numbers:
                print("3-use numbers")
            if not flag_table_special_char:
                print("4-use special characters")
            print("0-exit")
            user_input = users_inputs(0, 4)
            # only once input a table and if the user doen't input a number [1,4] then the program  exits
            if user_input == 0:
                break
            elif user_input == 1:
                flag_table_lower = True
            elif user_input == 2:
                flag_table_upper = True
            elif user_input == 3:
                flag_table_numbers = True
            elif user_input == 4:
                flag_table_special_char = True
            if flag_table_lower and flag_table_upper and flag_table_numbers and flag_table_special_char:
                break

        if flag_table_upper or flag_table_lower or flag_table_numbers or flag_table_special_char:
            # the final table assebly if atleast one table's falg is true
            final_table = ""
            if flag_table_lower:
                final_table += table_lower
            if flag_table_upper:
                final_table += table_upper
            if flag_table_numbers:
                final_table += table_numbers
            if flag_table_special_char:
                final_table += table_special_char
            # password lenght at least 8 characters
            pass_len = pass_lenght()
            for i in range(pass_len):
                password += choice(final_table)
            print("password= ", password)
