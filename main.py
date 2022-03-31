import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, pi,linspace
#draw point at orgin
plt.plot(0,0, color = 'red', marker = 'o')
plt.gca().annotate('O (0, 0)', xy=(0 + 0.1, 0 + 0.1), xycoords='data', fontsize=10)
#draw a circle
angles = linspace(0 * pi, 2 * pi, 100 )
r = 1.5
xs = r * cos(angles)
ys = r * sin(angles)
plt.plot(xs, ys, color = 'green')
#draw daimeter
plt.plot(0.513,1.409, marker = 'o', color = 'blue')
plt.plot(-1.5, 0, marker = 'o', color = 'blue')
plt.plot([0.513,-1.5], [1.409, 0])


plt.plot(0.513,1.409, marker = 'o', color = 'blue')
plt.plot(1.14906,0.964, marker = 'o', color = 'blue')
plt.plot( [0.513,1.14906],[1.409,0.964])

plt.plot(-0.2602,-1.476, marker = 'o', color = 'blue')
plt.plot(1.5, 0, marker = 'o', color = 'blue')
plt.plot([-0.2602,1.5], [-1.476, 0])

plt.plot(1.5,0, marker = 'o', color = 'blue')
plt.plot(1.14906,0.964, marker = 'o', color = 'blue')
plt.plot( [1.5,1.14906],[0,0.964])

plt.plot(-0.2602,-1.476, marker = 'o', color = 'blue')
plt.plot(-1.5, 0, marker = 'o', color = 'blue')
plt.plot([-0.2602,-1.5], [-1.476, 0])

plt.plot(-1.5,0, marker = 'o', color = 'blue')
plt.plot(1.5, 0, marker = 'o', color = 'blue')
plt.plot([-1.5,1.5], [0, 0])

plt.gca().annotate( 'diameter', xy=(-0.5, -0.25), xycoords='data', fontsize=10)
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.gca().set_aspect('equal')
plt.show()
