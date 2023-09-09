import pyrosim.pyrosim as pyrosim

x = 0
y = 0
z = 0.5

length = 1
width = 1
height = 1


def Create_World():
    pyrosim.Start_SDF("world.sdf")  # tell pyrosim file where world will be stored

    pyrosim.Send_Cube(name="Box", pos=[x+1, y+3, z], size=[length, width, height])  # store box in pyrosim

    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1, 0, 1.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0.5, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[1.5, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])
    pyrosim.End()

Create_Robot()
Create_World()
