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

