import euler_lv
import odeint_lv
from nsteps import nsteps
tested_steps = (0.3,0.1,0.01,0.001)

for stepsize in tested_steps:
    num_of_steps = nsteps(25, stepsize)

    euler_lv.calc_euler(25,stepsize,) 