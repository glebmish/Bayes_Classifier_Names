# coding=utf-8
import codecs
from Bayes_Classifier import *

def guess():
    name = raw_input("Write name: ")
    while name != '0':
        print BC.classify(name)
        name = raw_input("Write surname: ")

train, test = divide(DataSet("dataset_surnames.txt"), 10, 20)
BC = BayesClassifier(lambda x: {'last': x[-1], '2nd-last': x[-2], '3rd-last': x[-3]})
BC.train(train)
print zip(['recall:', 'precision:'], BC.check(test))
guess()
