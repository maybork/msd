from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint
from nsteps import nsteps


def lorenz(xyz, t, sigma, beta, rho):
    x, y, z = xyz
    delta = [sigma * (y - x), (x * (rho - z) - y), ((x * y) - (beta * z))]
    return delta


def calc_odeint(interval, dt, x0, y0, z0, params):
    sigma, beta, rho = params
    steps = nsteps(interval, dt)
    t = np.linspace(0, interval, steps)
    xyz0 = [x0, y0, z0]
    xyz = odeint(lorenz, xyz0, t, args=(sigma, beta, rho))
    return xyz, t
