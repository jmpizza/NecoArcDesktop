import random as rd
from screeninfo import get_monitors
from PIL import Image
import win32gui
import win32con
import win32api
import pygame

class Neco:

    def __init__(self):
        self.running = True
        self.monitors = get_monitors()
        pygame.init()
        self.screen = pygame.display.set_mode((self.monitors[0].width, self.monitors[0].height), pygame.NOFRAME | pygame.SRCALPHA)
        self.clock = pygame.time.Clock()

        self.green = (0, 255, 0)

        a = pygame.display.get_wm_info()['window']
        win32gui.SetWindowLong(a, win32con.GWL_EXSTYLE,
                            win32gui.GetWindowLong(a, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        win32gui.SetLayeredWindowAttributes(a, win32api.RGB(*self.green), 0, win32con.LWA_COLORKEY)
        win32gui.SetWindowPos(a, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)
        self.frame_index = 0


    def update(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        self.screen.fill(self.green)


    def walk(self, gif):
        for i in range(len(gif)):
            self.screen.fill(self.green)
            self.screen.blit(gif[i], (0, 0))
            pygame.display.flip()
            self.clock.tick(9)
        