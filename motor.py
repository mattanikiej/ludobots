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

        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        if self.jointName == b"Torso_FrontLeg":
            self.frequency /= 2

        self.values = self.amplitude * np.sin(self.frequency * self.values + self.phaseOffset)

    def Set_Value(self, t, robotId):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.values[t],
            maxForce=50)

    def Save_Values(self):
        np.save("data/"+self.jointName+"MotorValues.npy", self.values)