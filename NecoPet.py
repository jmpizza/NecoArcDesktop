import random as rd
from screeninfo import get_monitors
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

        self.black = (0, 0, 0)

        a = pygame.display.get_wm_info()['window']
        win32gui.SetWindowLong(a, win32con.GWL_EXSTYLE,
                            win32gui.GetWindowLong(a, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        win32gui.SetLayeredWindowAttributes(a, win32api.RGB(*self.black), 0, win32con.LWA_COLORKEY)
        win32gui.SetWindowPos(a, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)
        
        self.pet_xposition = 0
        self.pet_yposition = self.monitors[0].height-250


    def update(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        self.screen.fill(self.black)


    def walk(self, gif):
        for frame in range(len(gif)):
            self.screen.fill(self.black)
            self.screen.blit(gif[frame], (self.pet_xposition, self.pet_yposition))
            self.pet_xposition += 10
            pygame.display.flip()
            self.clock.tick(9)
            if self.pet_xposition > self.monitors[0].width:
                 self.pet_xposition = -200
        