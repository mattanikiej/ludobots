import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")  # tell pyrosim file where world will be stored
pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[1, 1, 1])  # store box in pyrosim

pyrosim.End()
