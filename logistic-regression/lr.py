# !env python
#  coding=utf-8

__author__ = 'Administrator'

import numpy as np

class Logistic:
    def __init__(self):
        __lamb = 0.001
        __alpha = 0.1

    def train(self, data, maxIterate):
        pass

    def pred(self, x):
        '''
        predicate x
        :param x:
        :return: the predicated result
        '''
        pass

    def sigmoid(self, x):
        '''
        sigmoid function
        :param x:
        :return:y
        '''
        return 1/(1+np.exp(-x))

    def __str__(self, *args, **kwargs):
        return super().__str__(*args, **kwargs)


def load_train_data():
    data = {}
    return data

def load_test_data():
    """

    :rtype : object
    """
    test = {}
    return test

if __name__ == '__main__':
    data = load_train_data()
    print("load trainning data: %d" %(len(data)))
    maxIterate = 1000;
    lr = Logistic()
    lr.train(data, maxIterate)
    x = load_test_data()
    print("load testing data: %d" %(len(x)))
    lr.pred(x)
