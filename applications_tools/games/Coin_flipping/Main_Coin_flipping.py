from random import choice

##############################################################
# ένα πρόγραμμα το οποίο προσομοιώνει τη ρίψη ενός κέρματος #
##############################################################
print("Θέλεις να ρίξεις το κέρμα; ")
c_w=0
c_l=0
answer=str(input("'ΝΑΙ' Ή 'ΟΧΙ'; : "))
while answer=='ΝΑΙ':
    if answer=='NAI':
        list = ['Γ','Κ']
        user_choice = str(input("Επίλεξε ένα γράμμα 'Γ' για γράμματα ή 'Κ' για κορώνα : "))
        result = choice(list)
        if result == 'Γ':
            print("Γράμματα.")
        elif result == 'Κ':
            print("Κορώνα.")
        if result == user_choice:
            print("Σωστό, κέρδισες!")
            c_w=c_w+1
        else:
            print("Λάθος, έχασες!")
            c_l=c_l+1
    answer = str(input("'ΝΑΙ' Ή 'ΟΧΙ'; : "))
print("Κλείσιμο παιχνιδιού")

# Καμία πρόταση για διόρθωση;

