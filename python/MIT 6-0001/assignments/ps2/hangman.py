# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import numpy as np


WORDLIST_FILENAME = "words.txt"


def load_words():
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


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #
    for i in secret_word:
        if i in letters_guessed:
            secret_word = secret_word.replace(i, "", secret_word.count(i))

    if secret_word == "":
        return True
    return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in secret_word:
        if i not in letters_guessed:
            secret_word = secret_word.replace(i, "_ ", secret_word.count(i))
    return secret_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    for letter in letters_guessed:
        alphabet = alphabet.replace(letter, "")
    return alphabet
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    warnings = 3
    available_letters = string.ascii_lowercase
    word = len(secret_word) * ["_ "]
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
    print('You have {} warnings left: '.format(warnings))
    print("-------------")

    while True:
        print('You have {} guesses left.'.format(guesses))
        if warnings < 3 and warnings >= 0:
            print('You have {} warnings left: '.format(warnings))
        print('Available letters: {}'.format(available_letters))
        print(secret_word)
        guess = input('Please guess a letter: ')
        if len(guess) > 1 or (not guess.isalpha()):
            warnings -= 1
            if warnings < 0:
                guesses -= 1
                print("Oops! That is not a valid letter."
                      "You have no warnings left so you lose one guess: {}".format("".join(word)))
            else:
                print('Oops! That is not a valid letter. You have {} warnings left: '.format(warnings))
            print("-------------")

        elif guess.lower() in secret_word:
            if guess in word:
                warnings -= 1
                if warnings < 0:
                    guesses -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one "
                          "guess: {}".format("".join(word)))
                else:
                    print("Oops! You've already guessed that letter. You now have {0} "
                      "warnings left: {1}".format(warnings, "".join(word)))
                print("-------------")
            else:
                for i in range(len(secret_word)):
                    if secret_word[i] == guess:
                        word[i] = guess
                available_letters = available_letters.replace(guess, "")
                print('Good guess: {}'.format("".join(word)))
                print("-------------")

        elif guess.lower() not in secret_word:
            guesses -= 1
            available_letters = available_letters.replace(guess, "")
            print("Oops! That letter is not in my word: {}".format("".join(word)))
            print("-------------")

        if "".join(word) == secret_word:
            total_score = guesses * len(np.unique(word))
            print("Congratulations, you won!")
            print("Your total score for this game is: {}".format(total_score))
            break

        if guesses == 0:
            print("Sorry, you ran out of guesses. The word was else.  ")
            break


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word = ""
    for i in my_word:
        if i != "_ ":
            word += i
        else:
            word += "_"
    if len(word) != len(other_word):
        print("No match")
        return False

    for i in range(len(word)):
        if word[i] != other_word[i]:
            print("No match")
            return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pos_revealed = []
    word = ""
    matches = False
    for i in my_word:
        if i != "_ ":
            word += i
        else:
            word += "_"

    for i in range(len(word)):
        if word[i] != "_":
            pos_revealed.append(i)

    print("Possible word matches are: ")
    for j in wordlist:
        if len(j) == len(word):
            total = 0
            for pos in pos_revealed:
                if j[pos] == word[pos]:
                    total += 1
            if total == len(pos_revealed):
                if not matches:
                    matches = True
                print(j, end=" ")
    if not matches:
        print("No matches found")
    print()


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    warnings = 3
    available_letters = string.ascii_lowercase
    word = len(secret_word) * ["_ "]
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
    print('You have {} warnings left: '.format(warnings))
    print("-------------")

    while True:
        print('You have {} guesses left.'.format(guesses))
        if warnings < 3 and warnings >= 0:
            print('You have {} warnings left: '.format(warnings))
        print('Available letters: {}'.format(available_letters))
        print(secret_word)
        guess = input('Please guess a letter: ')
        if guess == "*":
            show_possible_matches(word)
            continue
        elif guess == "/":
            match = input("What do you think what match is? ")
            match_with_gaps(word, match)
            continue

        elif len(guess) > 1 or (not guess.isalpha()):
            warnings -= 1
            if warnings < 0:
                guesses -= 1
                print("Oops! That is not a valid letter. "
                      "You have no warnings left so you lose one guess: {}".format("".join(word)))
            else:
                print('Oops! That is not a valid letter. You have {} warnings left: '.format(warnings))
            print("-------------")

        elif guess.lower() in secret_word:
            if guess in word:
                warnings -= 1
                if warnings < 0:
                    guesses -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one "
                          "guess: {}".format("".join(word)))
                else:
                    print("Oops! You've already guessed that letter. You now have {0} "
                          "warnings left: {1}".format(warnings, "".join(word)))
                print("-------------")
            else:
                for i in range(len(secret_word)):
                    if secret_word[i] == guess:
                        word[i] = guess
                available_letters = available_letters.replace(guess, "")
                print('Good guess: {}'.format("".join(word)))
                print("-------------")

        elif guess.lower() not in secret_word:
            if guess.lower() not in available_letters:
                warnings -= 1
                if warnings < 0:
                    guesses -= 1
                    print("Oops! You've already guessed that letter."
                          "You have no warnings left so you lose one guess: {}".format("".join(word)))
                else:
                    print("Oops! You've already guessed that letter. "
                          "You have {0} warnings left: {1}".format(warnings, "".join(word)))
                print("-------------")
            else:
                guesses -= 1
                available_letters = available_letters.replace(guess, "")
                print("Oops! That letter is not in my word: {}".format("".join(word)))
            print("-------------")

        if "".join(word) == secret_word:
            total_score = guesses * len(np.unique(word))
            print("Congratulations, you won!")
            print("Your total score for this game is: {}".format(total_score))
            break

        if guesses == 0:
            print("Sorry, you ran out of guesses. The word was else.  ")
            break


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    # hangman(secret_word)
    hangman_with_hints(secret_word)


###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
