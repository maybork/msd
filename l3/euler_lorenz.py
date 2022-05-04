import numpy as np
import matplotlib.pyplot as plt
import math
from nsteps import nsteps


def calc_euler(
    interval: int,
    dt: float,
    x0: int,
    y0: int,
    z0: int,
    params: tuple[float, float, float],
):
    sigma, beta, rho = params
    steps = nsteps(interval, dt)
    t = np.linspace(0, interval, steps)
    xyz = np.zeros((steps, 3))
    xyz[0, 0] = x0
    xyz[0, 1] = y0
    xyz[0, 2] = z0

    for i in range(np.shape(xyz)[0] - 1):
        x, y, z = xyz[i, 0], xyz[i, 1], xyz[i, 2]
        dx = sigma * (y - x) * dt
        dy = (x * (rho - z) - y) * dt
        dz = ((x * y) - (beta * z)) * dt
        xyz[i + 1, 0] = x + dx
        xyz[i + 1, 1] = y + dy
        xyz[i + 1, 2] = z + dz
    return xyz, t
