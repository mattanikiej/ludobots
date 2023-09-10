import os
from hillclimber import HILL_CLIMBER


# for _ in range(5):
#     os.system("Python generate.py")
#     os.system("Python simulate.py")

hc = HILL_CLIMBER()
hc.Evolve()
