import random
 #κάνει import την βιβλιοθήκη random
 
def DiceRoller():  
    while True:
        
        # Παράγει ένα τυχαίο νούμερο ανάμεσα απο 1 και 6 , περιέχοντας το 1 και 6 
        no = random.randint(1,6)
        
        if no == 1:
            
            print("[-----]")
            print("[  0  ]")
            print("[-----]")
            
        elif no == 2:
            print("[-----]")
            print("[ 0   ]")
            print("[   0 ]")
            print("[-----]")
            
        elif no == 3:
            
            print("[-----]")
            print("[0 0 0]")
            print("[-----]")
            
        elif no == 4:
            print("[-----]")
            print("[0   0]")
            print("[0   0]")
            print("[-----]")
        elif no == 5:
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
        else:
            print("[-----]")
            print("[0 0 0]")
            print("[0 0 0]")
            print("[-----]")
        #αναπαριστώνται τα σχήματα των ζαριών     
        ans = input("Πληκτρολόγησε Ν αν θες να συνεχίσεις ή Ο αν θες να σταματήσεις")
        if ans == "Ν":
            print("Τέλεια!")
        elif ans == "Ο":
            break
        else:
            print("Λάθος απάντηση")
    