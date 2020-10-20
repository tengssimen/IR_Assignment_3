import string
from nltk.stem.porter import PorterStemmer
import codecs
import functions
import copy

text_file = "./book.txt"

def main():
  #This file contains task 1.1 - 1.6

  f = codecs.open(text_file, "r", "utf-8")
  paragraphs = functions.makeParagraphArray(f)

  #Removes "gutenberg" and makes a copy of the paragraph
  paragraphs = functions.remove_specific_word("Gutenberg", paragraphs)
  paragraphs = functions.remove_specific_word("gutenberg", paragraphs)
  par_copy = copy.copy(paragraphs)

  paragraphs = functions.tokenize(paragraphs)
  paragraphs = functions.rem_pun(paragraphs)
  paragraphs = functions.stem(paragraphs)

  return par_copy, paragraphs