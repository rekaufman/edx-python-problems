# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

from random import choice

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter in lettersGuessed:
            continue
        else:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

# for each letter in secretWord,
# if in lettersGuessed, add the letter to wordSoFar
# print letter in secretWord,
# if not print underscore
    wordSoFar = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            wordSoFar += letter
        else:
            wordSoFar += "_"
    return wordSoFar


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    # for letter in "abc....", if not in 'lettersGuessed' add to availableLetters, return availableLetters
    availableLetters = ""
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in lettersGuessed:
            availableLetters += letter
    return availableLetters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guesses = 8
    lettersGuessed = ""
    print("The secret word is " + str(len(secretWord)) + " letters long.")
    while guesses != 0 and isWordGuessed(secretWord, lettersGuessed) is False:
        print("You have " + str(guesses) + " guesses remaining.")
        userGuess = input("Please guess a letter ")
        if userGuess in secretWord:
            print("Good guess!")
        elif userGuess in lettersGuessed:
            print("Oops! You already guessed that letter. Try again.")
        else:
            guesses -= 1
            print("That letter is not in the word.")
        lettersGuessed += userGuess
        print(getGuessedWord(secretWord, lettersGuessed))
        print("Available Letters: " + getAvailableLetters(lettersGuessed))
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Game over, you lost. The secret word is: " + secretWord)



    # When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
