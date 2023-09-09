import pyrosim.pyrosim as pyrosim

x = 0
y = 0
z = 0.5

pyrosim.Start_SDF("box.sdf")  # tell pyrosim file where world will be stored
for i in range(5):
    for j in range(5):
        length = 1
        width = 1
        height = 1
        for k in range(5):

            pyrosim.Send_Cube(name="Box", pos=[x+i, y+j, z+k], size=[length, width, height])  # store box in pyrosim

            length *= .9
            width *= .9
            height *= .9

pyrosim.End()
