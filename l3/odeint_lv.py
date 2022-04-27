from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint
from nsteps import nsteps


def lotka_volterra(xy, t, a, b, c, d):
    prey, pred = xy
    dydt = [(a - b * pred) * prey, (c * prey - d) * pred]
    return dydt


def calc_odeint(interval, dt, x0, y0, params):
    a, b, c, d = params
    steps = nsteps(interval, dt)
    t = np.linspace(0, interval, steps)
    xy0 = [x0, y0]
    xy = odeint(lotka_volterra, xy0, t, args=(a, b, c, d))
    return xy, t


def main():
    xy0 = [2, 1]
    a = 1.2
    b = 0.6
    c = 0.3
    d = 0.8
    t = np.linspace(0, 20, 201)

    sol, t = calc_odeint(25, 0.01, 2, 1, (a, b, c, d))
    print(sol.shape)
    plt.plot(t, sol[:, 0], "g", label="x(t)")
    plt.plot(t, sol[:, 1], "r", label="y(t)")
    plt.legend(loc="best")
    plt.xlabel("t")
    plt.ylabel("population")
    plt.show()


if __name__ == "__main__":
    raise SystemExit(main())
