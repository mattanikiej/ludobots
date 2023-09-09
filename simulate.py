import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)  # connect client to gui
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)  # disable sidebars to increase performance

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")  # add floor
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")  # read in world from box.sdf

for i in range(1000):
    p.stepSimulation()  # step through simulation
    time.sleep(1/60)
    # print(i)

p.disconnect()  # disconnect client
