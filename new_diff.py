import numpy as np
import matplotlib.pyplot as plt

L = 300.
dx = .1
dt = 0.015
a = -3.
T = 0.45
x = np.linspace(0, L, int(L/dx+1.))
ux0 = np.zeros(int(L/dx+1.))
ux0[int(50./dx+1.):int(110./dx+1.)] = np.sin(np.pi*(x[int(50./dx+1.):int(110./dx+1.)]-50.)/60.)

u = ux0

t = dt

while t <= T:
    u_final = u.copy()
    u_final[1:-1] = u[1:-1]-0.5*a*dt/dx*(u[2:]-u[:-2])
    u = u_final.copy()
    t+=dt

plt.plot(x,ux0)
plt.plot(x,u_final)
plt.show()
