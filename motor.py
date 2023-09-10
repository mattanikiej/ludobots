import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

        self.amplitude = c.bl_amplitude
        self.frequency = c.bl_frequency
        self.phaseOffset = c.bl_phaseOffset

        self.values = np.linspace(0, 2*np.pi, 1000)

    def Set_Value(self, desiredAngle, robotId):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=50)

