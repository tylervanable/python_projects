"""
    Determine how many sentences, words, and characters a text 
    that the user inputs contains. 
"""


import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize


# Annotate the variables
text: str
num_sentences: int
num_words: int
num_characters: int

# Obtain text from the user.
text = input("Please input some text: ")

# Tokenize the text into sentences, words, and characters.
num_sentences = len(sent_tokenize(text))
num_words = len(word_tokenize(text))
num_characters = len(text)

print("\nThe number of sentences in the text is: {}"
      .format(num_sentences))
print("\nThe number of words in the text is: {}"
      .format(num_words))
print("\nThe number of characters in the text is: {}"
      .format(num_characters))
