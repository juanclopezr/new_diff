import numpy as np
import matplotlib.pyplot as plt

dx = .1
dt = .025
T = .5
x = np.linspace(0.,1.,500)
L = x[-1]


rho = np.zeros(x.shape)
p = np.zeros(x.shape)
u = np.zeros(x.shape)

ii = x<=0.5

rho[ii] = 1.
rho[np.logical_not(ii)] = 0.125
p[ii] = 1.
p[np.logical_not(ii)] = .1

def mac(prev, F):
	u_f = prev.copy()
	ust = prev.copy()
	ust[1:-1] = u-dt(F(prev)[2:]-F(prev)[1:-1])/dx
	u_f[1:-1] = 0.5*(prev[1:-1]+ust[1:-1]-dt*(F(ust)[1:-1]-F(ust)[:-2])/dx)
	return u_f
	
