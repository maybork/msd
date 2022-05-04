# type:ignore
import numpy as np
from nsteps import nsteps


def calc_euler(
    interval: int,
    dt: float,
    x0: int,
    y0: int,
    params: tuple[float, float, float, float],
):

    a, b, c, d = params
    steps = nsteps(interval, dt)
    t = np.linspace(0, interval, steps)
    xy = np.zeros((steps, 2))
    xy[0, 0] = x0
    xy[0, 1] = y0

    for i in range(np.shape(xy)[0] - 1):
        x, y = xy[i, 0], xy[i, 1]
        dx = (a - b * y) * x * dt
        dy = (c * x - d) * y * dt
        xy[i + 1, 0] = x + dx
        xy[i + 1, 1] = y + dy
    return xy, t
