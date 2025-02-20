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
    #The values are taken from the save location and plotted onto a graph
    vals = pickle.load(open('plotvals.txt','rb'))
    x = vals[0]
    y = vals[1]
    plt.scatter(x,y)
    plt.xlim(0,3.9)
    plt.ylim(0,3.2)
    plt.draw()
    plt.pause(0.01)
    plt.clf()
