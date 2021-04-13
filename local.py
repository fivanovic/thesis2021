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
P.add_anchor('Station2',(100,0))
P.add_anchor('Station3',(0,100))
P.add_anchor('Station4',(100,100))

device,label=P.add_target()

device.add_measure('Station1',70.71)
device.add_measure('Station2',70.71)
device.add_measure('Station3',70.71)
device.add_measure('Station4',70.71)
P.solve()
print(device.loc)
