import functions

def main(dictionary, tfidf_model, tfidf_corpus, matrix_sim, lsi_matrix, lsi_model, paragraphs):

  # Processes the query with the same function as used in task 1, and convert to BOW representation.
  #q = "What is the function of money?"
  q = "How taxes influence Economics?"
  q = functions.process(q)
  
  q = dictionary.doc2bow(q)

  # Converts BOW to TF-IDF representation.
  tfidf_index = tfidf_model[q]
  #print(r)

  # 3 most relevant paragraph for q according to TF-IDF model
  doc2similarity = enumerate(matrix_sim[tfidf_index])
  docs = sorted(doc2similarity, key=lambda kv: -kv[1])[:3]

  print("# 3 most relevant paragraph for q according to TF-IDF model for q:")
  print("\n" + "[paragraph " + str(docs[0][0]) + "]")
  print(paragraphs[docs[0][0]])
  print("\n" + "[paragraph " + str(docs[1][0]) + "]")
  print(paragraphs[docs[1][0]])
  print("\n" + "[paragraph " + str(docs[2][0]) + "]")
  print(paragraphs[docs[2][0]])
  
  #Compare TF-IDF representation for the query with LSI-topic representation
  print("Comparing TF-IDF representation for the query with LSI-topic representation:\n")
  
  lsi_query = lsi_model[q]
  topics = sorted(lsi_query, key=lambda kv: -abs(kv[1]))[:3]

  for topic in enumerate(topics):
    top = topic[1][0]
    print("\n[Topic #" + str(top) + "]")
    print(lsi_model.show_topics()[top])
      
  doc2similarity= enumerate(lsi_matrix[lsi_query])
  docs = sorted(doc2similarity, key=lambda kv: -kv[1])[:3]
  for document in docs:
    d = document[0]
    print("\n[Paragraph #" + str(d) + "]")
    print(paragraphs[d])



  