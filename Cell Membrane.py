import numpy as np
import matplotlib.pyplot as plt

# Constants
Cm = 1.0    # Membrane capacitance (in Farads)
R_Na = 1.0  # Sodium channel resistance (in Ohms)
R_K = 2.0   # Potassium channel resistance (in Ohms)
R_other = 2.5  # Resistance for other ions (in Ohms)
V_Na = 55.0  # Sodium Nernst potential (in mV)
V_K = -75.0  # Potassium Nernst potential (in mV)
V_rest = -70.0  # Resting membrane potential (in mV)

deltax = 1.0
duration = 50.0  # Duration of the simulation (milli sec)
dt = 0.1  # Time step (milli sec)
num_steps = int(duration / dt)

# For storing results
time = np.linspace(0, duration, num_steps)
V_membrane = np.zeros(num_steps)

# Initial conditions
V_membrane[0] = V_rest

stim_start = 10  # Start of stimulation (in ms)
stim_end = 20    # End of stimulation (in ms)
stim_amplitude = 20.0  # Stimulation amplitude (in mV)

for i in range(1, num_steps):
    if stim_start <= time[i] <= stim_end:
        I_stim = stim_amplitude
    else:
        I_stim = 0.0

    # Update the membrane potential using the Euler method
    dV = (I_stim - (V_membrane[i - 1] - V_Na) / R_Na - (V_membrane[i - 1] - V_K) / R_K) / Cm * dt
    V_membrane[i] = V_membrane[i - 1] + dV

plt.figure()
plt.plot(time, V_membrane)
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Potential (mV)")
plt.title("Cell Membrane Potential Simulation")
plt.grid()
plt.show()

