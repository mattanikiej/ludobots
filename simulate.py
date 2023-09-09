import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np

physicsClient = p.connect(p.GUI)  # connect client to gui
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)  # disable sidebars to increase performance

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")  # add floor
robotId = p.loadURDF("body.urdf")
pyrosim.Prepare_To_Simulate(robotId)

p.loadSDF("world.sdf")  # read in world from box.sdf

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

for i in range(1000):
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    p.stepSimulation()  # step through simulation
    time.sleep(1/60)
    # print(backLegTouch)
    # print(i)

np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)

p.disconnect()  # disconnect client
