# !env python
#  coding=utf-8

__author__ = 'Administrator'

import numpy as np


class Logistic:
    def __init__(self):
        self._lamb = 0.001
        self._alpha = 0.1
        self._theta = None


    def err(self, result):
        '''
        lost function of logistic regression
        :param result: training or predicated result
        :return:None
        '''
        pass

    def train(self, data, maxIterate):
        # 初始化theta， 初始值为0
        self._theta = [0.0 for i in range(len(data[0]['x']) + 1)]
        # 将数据整理成齐次形式，即x0 = 1
        for i in range(0, len(self._theta)):
            data[i]['x'].insert(0, 1.0)  # 在数组 data[i].x 的头上插入数据 1.0
        # 随机梯度下降（上升）算法实现
        for i in range(0, maxIterate):
            # 遍历所有样本，每个样本都更新参数
            for j in range(0, len(data)):
                thetaX = sum([theta * data_x for theta, data_x in zip(self._theta, data[j]['x'])])
                hTheta = self.sigmoid(thetaX)

                # 计算梯度并且更新参数
                for k in range(0, len(self._theta)):
                    # 计算梯度
                    deltaTheta_k = (data[j]['y'] - hTheta) * data[j]['x'][k]
                    # update the parameter
                    self._theta[k] = self._theta[k] + self._alpha * deltaTheta_k - self._lamb * self._theta[k]
        # 去掉齐次项
        for i in range(len(data)):
            data[i]['x'].pop(0)


    def pred(self, x):
        '''
        predicate x
        :param x:
        :return: the predicated result
        '''
        x.insert(0, 1.0)

        thetaX = sum([theta * xi for theta, xi in zip(self._theta, x)])
        hTheta = self.sigmoid(thetaX)

        x.pop(0)

        return hTheta

    def sigmoid(self, x):
        '''
        sigmoid function
        :param x:
        :return:y
        '''
        return 1/(1+np.exp(-x))

    def __str__(self, *args, **kwargs):
        return "lambda = %f, alpha = %f, " % \
               (self._lamb, self._alpha)


def load_train_data():
    data = [{'x': [], 'y': 1}]
    return data

def load_test_data():
    """

    :rtype : object
    """
    # test = [{'x': [], 'y': 1}]
    test = [1.2]
    return test

def doTest():
    data = load_train_data()
    print("load trainning data: %d" %(len(data)))
    maxIterate = 1000
    lr = Logistic()
    print(lr)
    lr.train(data, maxIterate)
    x = load_test_data()
    print("load testing data: %d" %(len(x)))
    result = lr.pred(x)
    print("predicated result : %f" % result)


if __name__ == '__main__':
    doTest()
