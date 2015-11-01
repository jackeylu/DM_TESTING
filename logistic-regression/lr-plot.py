__author__ = 'Administrator'

import matplotlib.pyplot as plt
import numpy as np

def main():
    x = [i/100.0 for i in range(-1000,1000)]
    y = [(1/(1+np.exp(-i))) for i in x]
    z = [np.exp(-i)/((1+np.exp(-i))**2) for i in x]
    plt.plot(x,y,'r-',linewidth='1',label='DF of logistic, \miu=0,\gama=1')
    plt.plot(x,z,'g-',linewidth='1',label='density of logistic')
    plt.vlines(0,0,1)
    plt.legend(loc='upper left')
    #plt.show()
    plt.savefig("logistic-function.png")

if __name__ == '__main__':
    main()