import string
from nltk.stem.porter import PorterStemmer
import codecs

stemmer = PorterStemmer()

def remove_specific_word(word, strings):

  for s in strings:
      if s.__contains__(word):
          strings.remove(s)
  return strings

def tokenize(pars):
  for i, p in enumerate(pars):
    pars[i] = p.split(" ")
    
  return pars

def remove_punctuation(pars):
  # takes in a two dimentianal array
  for i, word_list in enumerate(pars):
    words = remove_punctuation_single(word_list)
    pars[i] = words
  return pars

def remove_punctuation_single(word_list):

    words = []
    for word in word_list:
        w = ""
        for letter in word:
            if (string.punctuation + "\n\r\t").__contains__(letter):
                if w != "":
                    words.append(w.lower())
                    w = ""
                continue
            w += letter
        if w != "":
            words.append(w.lower())
    return words

def get_stop_words(f):
  
  stop_words_list = []
  for i in f.readlines():
    stop_words_list.append(i.rstrip('\n'))
  
  return stop_words_list

def makeParagraphArray(f):

  paragraph = ""
  paragraphs = []
  for line in f.readlines():
      if line.isspace():
          if paragraph != "":
              paragraphs.append(paragraph)
          paragraph = ""
          continue
      paragraph += line
  return paragraphs


def stem(paragraphs):

    for i, p in enumerate(paragraphs):
        paragraphs[i] = stem_list(p)
    return paragraphs

def stem_list(words):

  # This function takes an array and stems every string (word) in it.
  # It then returns the array.

  for i, word in enumerate(words):
      words[i] = stemmer.stem(word.lower())
      #print(words[i])
  return words

def get_stop_wordids(stop_words, dictionary):
  #Finds word-indexes of every stopword
  id_arr = []
  for word in stop_words:
    try: id_arr.append(dictionary.token2id[word])
    except:
      pass
  return id_arr


def process(q):
  # Removes punctuation and tokenizes query
  q = q.split(" ")
  q = remove_punctuation_single(q)
  q = stem_list(q)
  return q

def make_bags_of_words(stemmed_pars, dictionary):
  bags = []
  for i in stemmed_pars:
    bags.append(dictionary.doc2bow(i))
  return bags