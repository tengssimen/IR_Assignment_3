import codecs
import functions
import gensim
stopwords_file = "./stopwords.txt"

def main(stemmed_pars):

  words = []

  #Reads the stop-words from file
  f = codecs.open(stopwords_file, "r", "utf-8")
  #Puts the stop words in list
  stop_words = functions.get_stop_words(f)

  #generate dictionary
  dictionary = gensim.corpora.Dictionary(stemmed_pars)
  
  #Get an array of the id's of the stopwords
  stop_ids = functions.get_stop_wordids(stop_words, dictionary)
  #Filter the stopwords
  dictionary.filter_tokens(stop_ids)
  # Get bag of words for every paragraph (Document
  bags = functions.make_bags_of_words(stemmed_pars, dictionary)

  return bags, dictionary