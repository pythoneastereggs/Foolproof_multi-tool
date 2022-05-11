import random

words = ["Beautiful", "Abyss", "Crystal", "Lemon", "Tiger", "Mortality"]

def get_word():
    word = random.choice(words)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Time to play Hangman!")
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not a valid word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job", guess, "is the word!")
                guessed_words.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not words.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print("Time to play Hangman!")
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the words! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
    

word = get_word()
play(word)
while input("Do you want to play again? (Y/N) ").upper() == "Y":
    word = get_word()
    play(word)