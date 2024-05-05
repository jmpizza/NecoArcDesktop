import random as rd
import tkinter as tk
import pyautogui as pyt
from NecoPet import Neco

neco_walk = "gifs/Neco_Walk.gif"
neco_angry = ''
neco_run = ''
screenWidth, screenHeight = pyt.size()

if __name__ == "__main__":
    neco = Neco(neco_walk, screenHeight)
    neco.run()