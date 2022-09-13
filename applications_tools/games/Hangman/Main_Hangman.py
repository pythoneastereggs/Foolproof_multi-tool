# Hangman game
import random
import os
from applications_tools.linux_tools.user_add_del_mod.lib.other_functions import user_continue
def Hangman_game():

    WORDLIST_FILENAME = "words.txt"
    os.chdir("../Hangman")
    while True:
        def ImportWords():
            """
            Returns a list of valid words. Words are strings of lowercase letters.
            
            Depending on the size of the word list, this function may
            take a while to finish.
            """
            print("Loading word list from file...")
            # inFile: file
            inFile = open(WORDLIST_FILENAME, 'r')
            # line: string
            line = inFile.readline()
            # wordlist: list of strings
            wordlist = line.split()
            print("  ", len(wordlist), "words loaded.")
            return wordlist

        def ReturnWord(wordlist):
            """
            wordlist (list): list of words (strings)
            Returns a word from wordlist at random
            """
            return random.choice(wordlist)

        # -----------------------------------
        wordlist = ImportWords()

        def CheckAnswer(HiddenWord, FoundLetters):
            '''
            HiddenWord: string, the word the user is guessing
            FoundLetters: list, what letters have been guessed so far
            returns: boolean, True if all the letters of HiddenWord are in FoundLetters;
            False otherwise
            '''
            c=0
            for i in FoundLetters:
                if i in HiddenWord:
                    c+=1
            if c==len(HiddenWord):
                return True
            else:
                return False


        def GetFoundLetters(HiddenWord, FoundLetters):
            '''
            HiddenWord: string, the word the user is guessing
            FoundLetters: list, what letters have been guessed so far
            returns: string, comprised of letters and underscores that represents
            what letters in HiddenWord have been guessed so far.
            '''
            s=[]
            for i in HiddenWord:
                if i in FoundLetters:
                    s.append(i)
            ans=''
            for i in HiddenWord:
                if i in s:
                    ans+=i
                else:
                    ans+='_ '
            return ans



        def SecretLetters(FoundLetters):
            '''
            FoundLetters: list, what letters have been guessed so far
            returns: string, comprised of letters that represents what letters have not
            yet been guessed.
            '''
            import string
            ans=list(string.ascii_lowercase)
            for i in FoundLetters:
                ans.remove(i)
            return ''.join(ans)

        def hangman(HiddenWord):
            '''
            HiddenWord: string, the secret word to guess.
            Starts up an interactive game of Hangman.
            * At the start of the game, let the user know how many 
            letters the HiddenWord contains.
            * Ask the user to supply one guess (i.e. letter) per round.
            * The user should receive feedback immediately after each guess 
            about whether their guess appears in the computers word.
            * After each round, you should also display to the user the 
            partially guessed word so far, as well as letters that the 
            user has not yet guessed.
            Follows the other limitations detailed in the problem write-up.
            '''
            print("Welcome to the game, Hangman!")
            print("I am thinking of a word that is",len(HiddenWord),"letters long.")
            
            global FoundLetters
            mistakeMade=0
            FoundLetters=[]
            
            while 8 - mistakeMade > 0:
                
                if CheckAnswer(HiddenWord, FoundLetters):
                    print("-------------")
                    print("Congratulations, you won!")
                    break
                    
                else:
                    print("-------------")
                    print("You have",8-mistakeMade,"guesses left.")
                    print("Available letters:",SecretLetters(FoundLetters))
                    guess=str(input("Please guess a letter: ")).lower()
                    
                    if guess in FoundLetters:
                        print("Oops! You've already guessed that letter:",GetFoundLetters(HiddenWord,FoundLetters))
                        
                    elif guess in HiddenWord and guess not in FoundLetters:
                        FoundLetters.append(guess)
                        print("Good guess:",GetFoundLetters(HiddenWord,FoundLetters))
                        
                    else:
                        FoundLetters.append(guess)
                        mistakeMade += 1
                        print("Oops! That letter is not in my word:",GetFoundLetters(HiddenWord,FoundLetters))
                        
                if 8 - mistakeMade == 0:
                    print("-------------")
                    print("Sorry, you ran out of guesses. The word was else.",HiddenWord)
                    nothing = input("press enter to exit: ")
                    break
                
                else:
                    continue
        print("Do you want to continue?")
        flag = user_continue()
        if flag == False:
            break
            
        HiddenWord = ReturnWord(wordlist).lower()
        hangman(HiddenWord)