import socket
import time
import threading
import math
import numpy as np
import sympy as sym
import localization as lx
import matplotlib.pyplot as plt
import pickle
plt.style.use('seaborn-whitegrid')

while(True):
    vals = pickle.load(open('plotvals.txt','rb'))
    x = vals[0]
    y = vals[1]
    plt.scatter(x,y)
    plt.xlim(0,3)
    plt.ylim(0,3)
    plt.draw()
    plt.pause(0.5)
    plt.clf()
