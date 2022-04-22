from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint


def lotka_volterra(xy, t, a, b, c, d):
    prey, pred = xy
    dydt = [(a - b * pred) * prey, (c * prey - d) * pred]
    return dydt


def main():
    xy0 = [2, 1]
    a = 1.2
    b = 0.6
    c = 0.3
    d = 0.8
    t = np.linspace(0, 20, 201)

    solution = odeint(lotka_volterra, xy0, t, args=(a, b, c, d))

    plt.plot(t, solution[:, 0], "g", label="x(t)")
    plt.plot(t, solution[:, 1], "r", label="y(t)")
    plt.legend(loc="best")
    plt.xlabel("t")
    plt.ylabel("population")
    plt.show()


if __name__ == "__main__":
    raise SystemExit(main())
