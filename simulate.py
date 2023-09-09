import pybullet as p
import time

physicsClient = p.connect(p.GUI)  # connect client to gui
# p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)  # disable sidebars to increase performance

for i in range(1000):
    p.stepSimulation()  # step through simulation
    time.sleep(1/60)
    # print(i)

p.disconnect()  # disconnect client
