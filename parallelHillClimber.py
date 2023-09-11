from solution import SOLUTION
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        # self.parent = SOLUTION()
        # self.child = None

        os.system("del brain*.nndf")
        os.system("del fitness*.txt")

        self.parents = {}
        self.children = {}

        self.nextAvailableID = 0

        for parent in range(c.populationSize):
            self.parents[parent] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        # self.parent.Evaluate("GUI")
        #
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()
        #
        # self.Show_Best()

        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()



    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1


    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Select(self):
        for parent in self.parents:
            if self.children[parent].fitness < self.parents[parent].fitness:
                self.parents[parent] = copy.deepcopy(self.children[parent])

    def Evaluate(self, solutions):
        for solution in solutions:
            solutions[solution].Start_Simulation("DIRECT")

        for solution in solutions:
            solutions[solution].Wait_For_Simulation_To_End()

    def Print(self):
        for parent in self.parents:
            print(self.parents[parent].fitness, self.children[parent].fitness)

    def Show_Best(self):
        best = 0
        for parent in self.parents:
            if self.parents[parent].fitness < self.parents[best].fitness:
                best = parent

        self.parents[best].Start_Simulation("GUI")

