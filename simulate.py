import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

physicsClient = p.connect(p.GUI)  # connect client to gui
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)  # disable sidebars to increase performance

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")  # add floor
robotId = p.loadURDF("body.urdf")
pyrosim.Prepare_To_Simulate(robotId)

p.loadSDF("world.sdf")  # read in world from box.sdf

iters = 1000

backLegSensorValues = np.zeros(iters)
frontLegSensorValues = np.zeros(iters)

x = np.linspace(0, 2*np.pi, iters)

fl_amplitude = np.pi / 4
fl_frequency = 10
fl_phaseOffset = 0

fl_targetAngles = fl_amplitude * np.sin(fl_frequency * x + fl_phaseOffset)

bl_amplitude = np.pi / 4
bl_frequency = 11
bl_phaseOffset = np.pi / 4

bl_targetAngles = bl_amplitude * np.sin(bl_frequency * x + bl_phaseOffset)

# np.save("data/targetAngles.npy", targetAngles)

for i in range(iters):
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b"Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=bl_targetAngles[i],
        maxForce=50)

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b"Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=fl_targetAngles[i],
        maxForce=50)

    p.stepSimulation()  # step through simulation

    time.sleep(1/60)
    # print(backLegTouch)
    # print(i)

np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)

p.disconnect()  # disconnect client
