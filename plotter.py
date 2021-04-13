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
    x = 50
    y = 40
    plt.scatter(x,y)
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.draw()
    plt.pause(0.5)
    plt.clf()
   