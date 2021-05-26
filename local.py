import math
import numpy as np
import sympy as sym
from sympy.plotting import plot
from sympy.plotting import plot_parametric
import matplotlib
import matplotlib.pyplot as plt
import localization as lx

P=lx.Project(mode='2D',solver='LSE')

P.add_anchor('Station1',(0,0))
P.add_anchor('Station2',(10,0))
P.add_anchor('Station3',(0,10))
P.add_anchor('Station4',(10,10))

device,label=P.add_target()

device.add_measure('Station1',5.79)
device.add_measure('Station2',6.36)
device.add_measure('Station3',3.57)
device.add_measure('Station4',4.44)

P.solve()
print(device.loc)
