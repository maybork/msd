# type:ignore
from odeint_lorenz import calc_odeint
import matplotlib.pyplot as plt


X0 = Y0 = Z0 = 1
SIGMA = 10
BETA = 8 / 3
RHO = 28
TESTED_STEPS = (0.02, 0.01, 0.00001)
INTERVAL = 25

fig, axs = plt.subplots(ncols=3)
ode, _ = calc_odeint(INTERVAL, 0.001, X0, Y0, Z0, (SIGMA, BETA, RHO))

axs[0].plot(ode[:, 0], ode[:, 1])  # x(y)
axs[0].set_title("x(y)")
axs[1].plot(ode[:, 1], ode[:, 2])  # y(z)
axs[1].set_title("y(z)")
axs[2].plot(ode[:, 0], ode[:, 2])  # x(z)
axs[2].set_title("x(z)")
plt.suptitle("Układ Lorenza wyliczony odeint")

# plt.tight_layout()
plt.show()

fig = plt.figure()
fig.add_subplot(projection="3d")
ax = fig.add_subplot(projection="3d")
ax.plot(ode[:, 0], ode[:, 1], ode[:, 2])
plt.suptitle("Układ Lorenza wyliczony odeint")
plt.show()
