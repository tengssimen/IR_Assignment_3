import gensim

def main(bags, dictionary):

  #Builds a TF-IDF model using the corpus from the previous task.
  tfidf_model = gensim.models.TfidfModel(bags)

  #Maps the bags into TF-IDF Weights, represented in pairs of index and weight.
  tfidf_corpus = tfidf_model[bags]

  #Makes a MatrixSimilarity object to calculate similarity between paragraphs and queries.
  matrix_sim = gensim.similarities.MatrixSimilarity(tfidf_corpus)

  #LSI model: represent each paragrtaph with a list of 100 pairs of index and LSI-topic-weights.
  lsi_model = gensim.models.LsiModel(tfidf_corpus, id2word=dictionary, num_topics=100)
  lsi_corpus = lsi_model[bags]
  lsi_matrix = gensim.similarities.MatrixSimilarity(lsi_corpus)

  #print(lsi_model.show_topics(3,100))

  return tfidf_model, tfidf_corpus, matrix_sim, lsi_matrix, lsi_model