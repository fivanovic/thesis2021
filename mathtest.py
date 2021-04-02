import math
import numpy as np
import sympy as sym

Station1 = np.array((100,100))
Station2 = np.array((100,0))
Station3 = np.array((0,0))
Station4 = np.array((0,100))

device = np.array((32,50))

dist1 = np.linalg.norm(device-Station1)
dist2 = np.linalg.norm(device-Station2)
dist3 = np.linalg.norm(device-Station3)
dist4 = np.linalg.norm(device-Station4)

radsq1 = dist1**2
radsq2 = dist2**2
radsq3 = dist3**2
radsq4 = dist4**2

finrad1 = radsq1 - Station1[0]**2 - Station1[1]**2
finrad2 = radsq2 - Station2[0]**2 - Station2[1]**2
finrad3 = radsq3 - Station3[0]**2 - Station3[1]**2
finrad4 = radsq4 - Station4[0]**2 - Station4[1]**2

x,y = sym.symbols('x,y')
eq1 = sym.Eq(x**2+y**2-(2*Station1[0])*x-(2*Station1[1])*y,finrad1)
eq2 = sym.Eq(x**2+y**2-(2*Station2[0])*x-(2*Station2[1])*y,finrad2)
eq3 = sym.Eq(x**2+y**2-(2*Station3[0])*x-(2*Station3[1])*y,finrad3)
eq4 = sym.Eq(x**2+y**2-(2*Station4[0])*x-(2*Station4[1])*y,finrad4)
result = sym.solve([eq1,eq2,eq3,eq4],(x,y))
print(result)


#A = np.array([[1,0,1,0],[1,-200,1,0],[1,0,1,-200],[1,-200,1,-200]])
#print(A)
#B = np.array([[7877],[1923],[-6923],[-16723]])
#print(B)
