import numpy as np
import matplotlib.pyplot as plt

L = 4.
dx = 0.05
dt = 0.05
size = int(L/dx)
T = 0.5

u = np.zeros(size)

u[:int(size/2+1)] = 1.
u0 = u

t = 0.

while t<T:
    u_final = u.copy()
    u_final = 0.5*(u[2:]+u[:-2])-0.25*dt*(u[2:]**2-u[:-2]**2)/dx
    u = u_final.copy()
    t += dt

plt.plot(u0)
plt.plot(u)
plt.show()
