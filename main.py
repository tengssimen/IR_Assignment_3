import task_1
import task_2
import task_3
import task_4

def main():

  #task 1
  pars, stemmed_pars = task_1.main()

  #for p in pars:
    #print(p)

  #for p in stemmed_pars:
    #print(p)

  res = task_2.main(stemmed_pars)

  #for i in res:
    #print(i)

  #task 2
  bags, dictionary = task_2.main(stemmed_pars)

  #for i in bags:
    #print(i)

  #task_3
  tfidf_model, tfidf_corpus, matrix_sim, lsi_matrix, lsi_model = task_3.main(bags, dictionary)

  #task_4
  task_4.main(dictionary, tfidf_model, tfidf_corpus, matrix_sim, lsi_matrix, lsi_model, pars)

if __name__ == "__main__":
    main()