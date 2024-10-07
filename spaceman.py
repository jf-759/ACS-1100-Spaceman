import random

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
    
    # question for the line below: does that mean I have to put all the words in txt. on their own line? in order to comment this out?
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

    # A word is being chosen for the game.
    # Step 1: display intro, ie: "Welcome to Spaceman!"; "The secret word contains (x) of letters" 

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
    
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

    for letter in secret_word:
        # comment for new developer: you cannot put return True on this line because it will be incorrect since more letters have to be guessed.
        if letter not in letters_guessed:

            return False
   
    return True
     
 

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    guessed_word = ''
   
    for letter in secret_word:
        
        if letter in letters_guessed:
            
            guessed_word += letter
        
        else:
            
            guessed_word += '_'
    
    return guessed_word


# This is where step 4 and step 5 come into play.

# Step 4: Display what letters they have they have correct.

# Step 5: Display what letters have not been guessed yet.

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
    #TODO: check if the letter guess is in the secret word

    return guess in secret_word

# This is where step 6 comes into play:

# Step 6: Repeat these steps, for each letter guessed, until the user has gotten the word, or went through all their number of wrong guesses.


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''

# Follow all to-do's.

    #TODO: show the player information about the game according to the project spec

    lives = 7

    letters_guessed = []

    print(f"Hello! This is Spaceman! An interactive game, where you must figure out the secret word.\n")
    print(f"The Secret word contains {len(secret_word)} letters.")

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    while lives > 0 and not is_word_guessed(secret_word, letters_guessed):
        
        print(f"\nYou have {lives} lives left.")
        
        print (f"Guessed letters so far: {get_guessed_word(secret_word, letters_guessed)}")

        guess = input("Please guess a letter: ").lower()

    # You've gotten it to display "You have 7 lives left, the guessed letters, and the Please enter a letter."
    # Next steps: How do I get it to input the letters, I guess and change how many lives are left, when the user inputs something?


    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
