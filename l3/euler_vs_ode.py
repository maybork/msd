import euler_lv
import odeint_lv
from nsteps import nsteps
import matplotlib.pyplot as plt
import numpy as np

PARAMS = (1.2, 0.6, 0.3, 0.8)
X0 = 2
Y0 = 1
TESTED_STEPS = (0.3, 0.01, 0.001)
INTERVAL = 25

for stepsize in TESTED_STEPS:
    num_of_steps = nsteps(INTERVAL, stepsize)
    eul, t = euler_lv.calc_euler(INTERVAL, stepsize, X0, Y0, PARAMS)
    ode, t = odeint_lv.calc_odeint(INTERVAL, stepsize, X0, Y0, PARAMS)
    # print(t.shape, eul[:, 0].shape)
    avg_deviation_x = np.average((eul[:, 0] - ode[:, 0]) ** 2)
    avg_deviation_y = np.average((eul[:, 1] - ode[:, 1]) ** 2)
    print(f"average deviation for step {stepsize}: {avg_deviation_x} {avg_deviation_y}")
    plt.plot(t, eul[:, 0], "g", label="x(t)")
    plt.plot(t, ode[:, 0], "r", label="y(t)")
    plt.show()
