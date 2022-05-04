# type:ignore

import euler_lv
import odeint_lv

import matplotlib.pyplot as plt
import numpy as np

PARAMS = (1.2, 0.6, 0.3, 0.8)
X0 = 2
Y0 = 1
TESTED_STEPS = (0.3, 0.1, 0.01, 0.001, 0.0001)
INTERVAL = 25

print(f"{'step':>6} | {'x':>9} | {'y':>9} | {'(x+y)/2':>9}")
fig, axs = plt.subplots(nrows=len(TESTED_STEPS), sharex=True, squeeze=True)
for i, stepsize in enumerate(TESTED_STEPS):
    eul, t = euler_lv.calc_euler(INTERVAL, stepsize, X0, Y0, PARAMS)
    ode, t = odeint_lv.calc_odeint(INTERVAL, stepsize, X0, Y0, PARAMS)
    # print(t.shape, eul[:, 0].shape)
    avg_deviation_x = np.average(np.abs(eul[:, 0] - ode[:, 0]))
    avg_deviation_y = np.average(np.abs(eul[:, 1] - ode[:, 1]))
    print(
        f"{stepsize:6} | {avg_deviation_x:9.6f} | {avg_deviation_y:9.6f} | {(avg_deviation_x+avg_deviation_y)/2:9.6f}"
    )
    axs[i].plot(t, eul[:, 0], "g")
    axs[i].plot(t, ode[:, 0], "r")
    axs[i].set_title(f"dt = {stepsize}")

plt.suptitle("Porównanie między metodą eulera i scipy.odeint (porównywane wartości x)")
plt.show()
