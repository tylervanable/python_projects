"""
    Determine how many sentences, words, and characters a text 
    file that the user inputs contains. 

    <sidenote>: this program requests from the user how many lines 
    the text file has and also uses an accumulator variable.
"""

import typing
import os.path
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


# Annotate the variables
file_counter: typing.TextIO
text_file_name: str
text_file_lines: int = 0
line: str = ""
line_content_accumulator: str = ""
num_sentences: int = 0
num_words: int = 0
num_characters: int = 0

# Obtain text file name from the user, else print logging message.
text_file_name = input("Please enter the name of the text file: ")
text_file_lines = int(input("Please enter the number of lines in the text file: "))

if os.path.isfile(text_file_name):
      file_counter = open(text_file_name, "r")
      for i in range(text_file_lines):
            line = file_counter.readline()
            line_content_accumulator += line

      # Read the file and tokenize for the number of sentences, words, and characters.

      num_sentences = len(sent_tokenize(line_content_accumulator))
      num_words = len(word_tokenize(line_content_accumulator))
      num_characters = len(line_content_accumulator)

      # Print the amount of sentences, words, and characters in the text file. 
      print("\nThe number of sentences in the text is: {}"
            .format(num_sentences))
      print("\nThe number of words in the text is: {}"
            .format(num_words))
      print("\nThe number of characters in the text is: {}"
            .format(num_characters))
    
else:
      print("The file does not exist. Please try again.")
      text_file_name = input("Please enter the name of the text file: ")

