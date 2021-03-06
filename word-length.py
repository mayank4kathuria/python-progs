# Implementing matplotlib along with nltk's word_tokenizer

from matplotlib import pyplot as plt
from nltk.tokenize import word_tokenize

def main():

    text = "Many of the goods and services we depend on daily are now supplied by intelligent, automated machines rather than human beings. Robots build cars and other goods on assembly lines, where once there were human workers. Many of our phone conversations are now conducted not with people but with sophisticated technologies. We can now buy goods at a variety of stores without the help of a human cashier. Automation is generally seen as a sign of progress, but what is lost when we replace humans with machines? Given the accelerating variety and prevalence of intelligent machines, it is worth examining the implications and meaning of their presence in our lives."
    data = word_tokenize(text)

    l = [len(word) for word in words]
    plt.hist(l)
    plt.show()



if __name__ == "__main__":
    main()

    
