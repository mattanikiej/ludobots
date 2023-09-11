from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import time


class SIMULATION:
    def __init__(self, directOrGui, solutionID):
        self.directOrGui = directOrGui
        self.physicsClient = p.connect(p.DIRECT) if directOrGui == "DIRECT" else p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def __del__(self):
        p.disconnect()

    def Run(self):
        for i in range(c.iters):

            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            p.stepSimulation()  # step through simulation
            if self.directOrGui == "GUI":
                time.sleep(1/100)

    def Get_Fitness(self):
        self.robot.Get_Fitness()


