import random as rd
from screeninfo import get_monitors
from NecoPet import Neco

if __name__ == "__main__":
    neco = Neco()
    while neco.running:
        neco.action(neco.standing)
        neco.action(neco.walk_right, rd.randint(1, 5))

