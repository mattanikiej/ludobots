from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time
import constants as c


class SIMULATION:
    def __init__(self):

        self.physicsClient = p.connect(p.GUI)  # connect client to gui
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT()

    def __del__(self):
        p.disconnect()

    def Run(self):
        for i in range(c.iters):

            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            p.stepSimulation()  # step through simulation

            time.sleep(1 / 60)


