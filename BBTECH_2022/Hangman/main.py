import hangman_art
import hangman_list
from random import choice
###
word = choice(hangman_list.word_list)
logo = hangman_art.logo
stage = hangman_art.stages
###
# Step 1: Check type of variables above
# Step 2: Create loop that will run x time, x correspond to the word length
    #There would be two ways to end the program
    #1. Correctly guessed the word
    #2. Ran out of guessing chance

    #Requirements:
    # If the user has entered a letter they've already guessed, print the letter and let them know.
    # If the letter is not in the chosen_word, print out the letter
    