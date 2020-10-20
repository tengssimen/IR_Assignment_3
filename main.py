import task_1
import task_2

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

  for i in bags:
    print(i)

if __name__ == "__main__":
    main()