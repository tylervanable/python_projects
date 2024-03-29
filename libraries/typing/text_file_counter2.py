"""
    Determine how many sentences, words, and characters a text 
    file that the user inputs contains. 

    <sidenote>: this program uses "with"-"as" structure for easier 
    resource management. 
"""

import typing
import os.path
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


# Annotate the variables
file_counter: typing.TextIO
text_file_name: str
num_sentences: int
num_words: int
num_characters: int

# Obtain text file name from the user, else print logging message, and read the file.
text_file_name = input("Please enter the name of the text file: ")
if os.path.isfile(text_file_name):
      with open(text_file_name, "r") as file_counter:
            text_file = file_counter.read()

      # Tokenize the text file for the number of sentences, words, and characters.

      num_sentences = len(sent_tokenize(text_file))
      num_words = len(word_tokenize(text_file))
      num_characters = len(text_file)

      # Print the amount of sentences, words, and characters in the text file. 
      print("\nThe number of sentences in the text file is: {}"
            .format(num_sentences))
      print("\nThe number of words in the text file is: {}"
            .format(num_words))
      print("\nThe number of characters in the text file is: {}"
            .format(num_characters))
    
else:
      print("The file does not exist. Please try again.")
      text_file_name = input("Please enter the name of the text file: ")

