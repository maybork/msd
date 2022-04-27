# type:ignore
import numpy as np
import matplotlib.pyplot as plt
import math
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
    xy = np.zeros((2, steps))
    xy[0, 0] = x0
    xy[1, 0] = y0

    for i in range(np.shape(xy)[1] - 1):
        x, y = xy[0, i], xy[1, i]
        dx = (a - b * y) * x * dt
        dy = (c * x - d) * y * dt
        xy[0, i + 1] = x + dx
        xy[1, i + 1] = y + dy

    return xy, t


# t, xy = calc_euler(20, 0.01, 2, 1, (1, 1, 1, 1))
# plt.plot(t, xy[1, :], "g", label="x(t)")
# plt.plot(t, xy[0, :], "r", label="y(t)")
# plt.legend(loc="best")
# plt.xlabel("t")
# plt.ylabel("population")
# plt.show()


fig, axs = plt.subplots(3)

abcd = (1.2, 0.6, 0.3, 0.8)
xy, t = calc_euler(25, 0.3, 2, 1, abcd)
axs[0].plot(t, xy[1, :])
axs[0].plot(t, xy[0, :])
xy, t = calc_euler(25, 0.1, 2, 1, abcd)
axs[1].plot(t, xy[1, :])
axs[1].plot(t, xy[0, :])
xy, t = calc_euler(25, 0.001, 2, 1, abcd)
axs[2].plot(t, xy[1, :])
axs[2].plot(t, xy[0, :])
plt.show()
