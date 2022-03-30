while True: 
    print("Πληκτρολόγησε 1 για Δολλάριο")
    print("Πληκτρολόγησε 2 για Ευρό")
    print("Πληκτρολόγησε 3 για Αγγλική λίρα")
    print("Πληκτρολόγησε 4 για Καναδικό δολλάριο")
    print("Πληκτρολόγησε 5 για Κινέζικο Yuan Renminbi")
    print("Πληκτρολόγησε 6 για Ιαπωνικό Yen")
    print("Πληκτρολόγησε q ή Q για έξοδο")
    choice1 = input(int("Επίλεξε το αρχικό νόμισμα σου"))
    ammount = input(float("Πληκτρολόγησε το ποσό που θέλεις να μετατρέψεις"))
    if choice1 == 'q' or choice1 == 'Q' :
        break
    elif choice1 == 1:
         choice2 = input(int("Επίλεξε το νόμισμα που θέλεις να μετατρέψεις το αρχικό σου"))
         if choice2 == 1:
             print("Λάθος επιλογή")
         elif choice2 == 2:
             Result = ammount*0.898230
         elif choice2 == 3:
             Result = ammount*0.75967983
         elif choice2 == 4:
              Result = ammount*1.2485194
         elif choice2 == 5:
             Result = ammount*6.3514865
         else:
             Result = ammount*121.80500
    elif choice1 == 2:
         choice2 = input(int("Επίλεξε το νόμισμα που θέλεις να μετατρέψεις το αρχικό σου"))
         if choice2 == 1:
            Result = ammount*0.898230
         elif choice2 == 2:
             print("Λάθος επιλογή")
         elif choice2 == 3:
             Result = ammount*0.85
         elif choice2 == 4: 
             Result = ammount*1.39 
         elif choice2 == 5:
             Result = ammount*7.0624671
         else: 
             Result = ammount*135.57
    elif choice1 == 3:
         choice2 = input(int("Επίλεξε το νόμισμα που θέλεις να μετατρέψεις το αρχικό σου"))
         if choice2 == 1:
             Result = ammount*1.32
         elif choice2 == 2:
             Result = ammount*1.18
         elif choice2 == 3:
             print("Λάθος επιλογή") 
         elif choice2 == 4:
             Result = ammount*1.64
         elif choice2 == 5:
             Result = ammount*8.3576397
         else: 
             Result = ammount*160.32
    elif choice1 == 4:
         choice2 = input(int("Επίλεξε το νόμισμα που θέλεις να μετατρέψεις το αρχικό σου"))
         if choice2 == 1:
             Result = ammount*0.80
         elif choice2 == 2:
             Result = ammount*0.72
         elif choice2 == 3:
             Result = ammount*0.61
         elif choice2 == 4:
             print("Λάθος επιλογή")
         elif choice2 == 5:
             Result = ammount*5.0961898
         else: 
             Result = ammount*97.77
    elif choice1 == 5:
         choice2 = input(int("Επίλεξε το νόμισμα που θέλεις να μετατρέψεις το αρχικό σου"))
         if choice2 == 1:
             Result = ammount*0.15742974
         elif choice2 == 2:
             Result = ammount*0.14149625
         elif choice2 == 3:
             Result = ammount*0.1196892
         elif choice2 == 4:
             Result = ammount*0.19613971
         elif choice2 == 5:
             print("Λάθος επιλογή")
         else:
             Result = ammount*19.187744
    else: 
         choice2 = input(int("Επίλεξε το νόμισμα που θέλεις να μετατρέψεις το αρχικό σου"))
         if choice2 == 1:
             Result = ammount*0.0082
         elif choice2 == 2:
             Result = ammount*0.0074
         elif choice2 == 3:
             Result = ammount*0.0062
         elif choice2 == 4:
             Result = ammount*0.010
         elif choice2 == 5:
             Result = ammount*0.052120939
         else:
             print("Λάθος επιλογή") 
    print("Το μετατροποιημένο πόσο είναι", Result)          
          
             
             
       
    