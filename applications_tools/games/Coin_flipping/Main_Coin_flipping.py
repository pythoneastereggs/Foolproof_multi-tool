from random import choice

#############################################################
# ένα πρόγραμμα το οποίο προσομοιώνει τη ρίψη ενός κέρματος #
#############################################################

print("Do you want to flip the coin? ")
win_counter=0
lose_counter=0
list = ['T','H']
answer=str(input("'YES' or 'NO'?: "))
while answer == 'YES':                    #Επανάληψη της ρίψης με εντολή του χρήστη
    if answer == 'YES':
        user_choice = str(input("Choose one letter 'T' for tails or 'H' for heads : "))
        result = choice(list)
        if result == 'T':
            print("Tails.")
        elif result == 'H':
            print("Heads.")
        if result == user_choice:
            print("Correct, you won!")
            win_counter=win_counter+1
        else:
            print("Wrong, you lose!")
            lose_counter=lose_counter+1
    answer = str(input("'YES' or 'NO'?: "))
print("Total Wins:",win_counter)
print("Total Loses:",lose_counter)
print("Terminate Game")

# Καμία πρόταση για διόρθωση;