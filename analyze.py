import numpy as np
import matplotlib.pyplot as plt

# backLegSensorValues = np.load("data/backLegSensorValues.npy")
# frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
#
# plt.plot(backLegSensorValues, linewidth=1.5, label="back leg")
# plt.plot(frontLegSensorValues, label="front leg")

sin = np.load("data/targetAngles.npy")

plt.plot(range(1000), sin)

plt.legend()
plt.show()
