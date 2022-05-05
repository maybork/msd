# type: ignore
from euler_lorenz import calc_euler
from odeint_lorenz import calc_odeint
import matplotlib.pyplot as plt
import numpy as np

X0 = Y0 = Z0 = 1
SIGMA = 10
BETA = 8 / 3
RHO = 28
TESTED_STEPS = (0.02, 0.01, 0.005, 0.001, 0.0001)
INTERVAL = 25


fig, axs = plt.subplots(nrows=len(TESTED_STEPS), ncols=3, sharex=True)
print(f"{'step':>6} | {'x':>10} | {'y':>10} | {'z':>10} | {'(x+y+z)/3':>10}")
for i, stepsize in enumerate(TESTED_STEPS):
    eul, t = calc_euler(INTERVAL, stepsize, X0, Y0, Z0, (SIGMA, BETA, RHO))
    ode, _ = calc_odeint(INTERVAL, stepsize, X0, Y0, Z0, (SIGMA, BETA, RHO))
    avg_deviation_x = np.average(np.abs(eul[:, 0] - ode[:, 0]))
    avg_deviation_y = np.average(np.abs(eul[:, 1] - ode[:, 1]))
    avg_deviation_z = np.average(np.abs(eul[:, 1] - ode[:, 1]))

    print(
        f"{stepsize:6} | {avg_deviation_x:10.6f} | {avg_deviation_y:10.6f} | {avg_deviation_y:10.6f} | {(avg_deviation_x+avg_deviation_y + avg_deviation_z)/3:10.6f}"
    )

    axs[i, 0].plot(eul[:, 0], eul[:, 1])  # x(y)
    axs[i, 1].plot(eul[:, 1], eul[:, 2])  # y(z)
    axs[i, 2].plot(eul[:, 0], eul[:, 2])  # x(z)

axs[0, 0].set_title("x(y)")
axs[0, 1].set_title("y(z)")
axs[0, 2].set_title("x(z)")
plt.suptitle(
    "Wyniki uzyskane przez metodę Eulera z dt = "
    + ",".join([str(step) for step in TESTED_STEPS])
)
plt.show()
