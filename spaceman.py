import random

letters_guessed = [] #list to store guessed letters
guesses_left = 7 #this determines the variable
game_play = True


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # Step 1: Have the user enter a letter.

    # Step 2: Once that letter is entered,  display text that will either say if that letter is in the secret word, or is not in the secret word.

    # Step 3: Display text, based off of how many wrong guesses they have left. 

    # Step 4: Display what letters they have they have correct.

    # Step 5: Display what letters have not been guessed yet.

    # Step 6: Repeat these steps, for each letter guessed, until the user has gotten the word, or went through all their number of wrong guesses.
    
    # Loops through the letters in the secret_word and check if a letter is not in lettersGuessed

    user_guess = ""
    
    for x in range(len(secret_word)):
       
        if secret_word[x] in letters_guessed:
            user_guess += secret_word[x]
        
    if secret_word == user_guess:
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    # Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    underscore = "_" * len(secret_word)
   
    for x in range(len(secret_word)):
        
        if secret_word[x] in letters_guessed:
            underscore = underscore[:x] + secret_word[x] + underscore[x+1:]
       
    for letter in underscore:
            print(letter, end="")


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this
          round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''

    # make the secret_word = banana, guess = b
    # secret_word = cat, guess = a or guess = z valid vs invalid
    # user input two letters, a message shows up as 'please only use one letter'
    
    # check if the letter guess is in the secret word
    if guess in secret_word: 
        print("Yay! Your guess is in the secret word!")
        return True
    else:
        print("Darn, your guess was not in the word, try again!")
        return False

def alphabet_storage(guess, alphabet):
    if guess in alphabet:
        alphabet.remove(guess)
    else:
        pass
    print(f"\nHere are the letters that have not been guessed yet!: {alphabet}")

def end_game():

    letters_guessed.clear()
    another_round = input("Do you want to play again? (Y/N): ").lower()
    if another_round == 'y':
        print("Welcome to a new round of Spaceman!")
        secret_word = load_word()
        spaceman(secret_word, 7)
    else:
        print("\n Thank you for playing! Hope you enjoyed the game! \n")
        return
    
def user_turn():
    while True:
        print ("-----------------------------------------------\n")
        guessed_letter = input("Please enter a letter: ").lower()
        if len(guessed_letter) > 1:
            print("\nSorry, please only enter one letter.\n")
            continue
        elif guessed_letter.isalpha() == False:
            print("Sorry, please enter only letters of the alphabet.")
        elif guessed_letter in letters_guessed:
            print("Sorry, that letter has already been entered this round.")
            continue
        else:
            return guessed_letter

def spaceman(secret_word, guesses_left):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    #Show player the information:
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    print(f"Hello! This is Spaceman! An interactive game, where you must figure out the secret word.\n")
    print(f"\nThe secret word contains {len(secret_word)} letters.\n")

    #Ask Player to enter a letter:

    # You've gotten it to display "You have 7 lives left, the guessed letters, and the Please enter a letter."
    # Next steps: How do I get it to input the letters, I guess and change how many lives are left, when the user inputs something?
    
    while game_play == True:
        guess = user_turn()
        letters_guessed.append(guess)

        if is_guess_in_word(guess, secret_word):
            print(f"Guessed letters so far: ")
            get_guessed_word(secret_word, letters_guessed)

        else:
            print(f"Guessed letters so far:")
            get_guessed_word(secret_word, letters_guessed)
            print("")
            guesses_left -= 1
            if guesses_left <= 0:
                print(f"\n Game Over! The secret word was {secret_word} \n")
                end_game()
                return

            else:
                pass 

        if is_word_guessed(secret_word, letters_guessed):
            print("\n Yay!!! You won!! Congrats!! \n")
            end_game()
            return
        
        alphabet_storage(guess, alphabet)
        print(f"\nThere are {guesses_left} incorrect guesses left.")

#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word, guesses_left)
