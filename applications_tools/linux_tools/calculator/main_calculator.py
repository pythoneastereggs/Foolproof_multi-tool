
import cmath
import math

def calculator():
    while True:
        print("    1 Πρόσθεση")
        print("    2 Αφέραιση")
        print("    3 Πολλαπλασιασμός")
        print("    4 Διαίρεση")
        print("    5 δύναμη")
        print("    6 τετραγονική ρίζα")
        print("    7 για τις ριζες δευτεροβάθμιας εξίσωσης")
        print("    8 ημίτονο")
        print("    9 συνημίτονο")
        print("    10 εφαπτομένη")
        print("    11 λογάριθμο")
        print("    12 παραγοντικό")
        print("    Επίλεξε q ή Q για έξοδο")

        choice = input("Επίλεξε μια πράξη: ")
        if choice != "q" and choice != "Q":
            number1 = int(input("Πληκτρολόγησε αριθμό 1: "))
            number2 = float(input("Πληκτρολόγησε αριθμό 2: "))

        if choice == 'q' or choice == 'Q' :
            break
        elif choice == "1":
            print(number1, "+" , number2, "=" , (number1+number2))
        elif choice == "2":     
            print(number1, "-" , number2, "=" , (number1-number2))
        elif choice == "3":
            print(number1, "*" , number2, "=" , (number1*number2))
        elif choice == "4":
            if number2 == 0.0:
                print("Διέραιση με μηδενικό στον παρανομαστή, σφάλμα")
            else: print(number1, "/" , number2, "=" , (float(number1)/number2))
        elif choice == "5" :
            print(number1, "^" , number2, "=" , (number1**number2))
        elif choice == "6" :
            #χρησιμοποιείται η βιβλιοθήκη math για να γίνει η πράξη της ρίζας
            print (math.sqrt(number1),"και", math.sqrt(number2))
        elif choice == "7" :
            a = input("δώσε 1η παράμετρο")
            b = input("δώσε 2η παράμετρο")
            c = input("δώσε 3η παράμετρο")
            d = 0
            print ("η διακρίνουσα είναι", d = (b**2) - (4*a*c) )
            #Χρησιμοποιείται η βιβλιοθήκη cmath για να βρεθούν οι λύσεις της εξίσωσης
            sol1 = (-b-cmath.sqrt(d))/(2*a)
            sol2 = (-b+cmath.sqrt(d))/(2*a)
            print ("οι δύο ρίζες είναι", format(sol1,sol2)) #η format δίνει τα αποτελέσματα των sol1 και sol2 στον χρήστη
        elif choice == "8" :
            print(math.sin(number1), "και", math.sin(number2))
        elif choice == "9":
                print(math.cos(number1), "και" , math.cos(number2))
        elif choice =="10":
                print(math.tan(number1), "και" , math.tan(number2))
        elif choice == "11":
            ans2 = input("με τι βάση;")
            e = 2.71828
            if ans2 == e or ans2 == 2.71828:
                print("ο φυσικός λογάριθμος είναι :", end="")
                print (math.log(number1))
                print (math.log(number2))
            else: 
                print("ο λογάριθμος με βάση το" ,ans2 , "είναι", end="")
                print(math.log(number1,ans2))
                print(math.log(number2,ans2))
        elif choice == "12":
            ans3 = int(input("Δώσε αριθμό: "))   
            if ans3 < 0:
                print("ο παραγοντικός δεν γίνεται με αρνητικούς")
            elif ans3 == 0:
                print("ο παραγοντικός του 0 είναι 1")
            else: 
                for i in range(1,ans3 + 1):
                    factorial = factorial*i
                print("ο παραγοντικός του", ans3 , "είναι", factorial)
        else: 
            print("λάθος επιλογή")
            #test gpg key verification
            