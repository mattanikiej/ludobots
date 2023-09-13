from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import time
import constants as c


class ROBOT:
    def __init__(self, solutionID):
        self.sensors = {}
        self.motors = {}

        while not os.path.exists("brain"+str(solutionID)+".nndf"):
            time.sleep(0.01)

        self.nn = NEURAL_NETWORK("brain"+str(solutionID)+".nndf")

        self.robotId = p.loadURDF("body.urdf")
        self.solutionID = solutionID

        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        os.remove("brain" + str(solutionID) + ".nndf")

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Sense(self, t):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Value(t)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle, self.robotId)

    def Think(self):
        self.nn.Update()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        f = open("tmp"+self.solutionID+".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()

        os.rename("tmp"+self.solutionID+".txt", "fitness"+self.solutionID+".txt")

