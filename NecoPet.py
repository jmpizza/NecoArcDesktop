import os
from screeninfo import get_monitors
import win32gui
import win32con
import win32api
import pygame
from PIL import Image

class Neco:

    def __init__(self):
        self.running = True
        self.click_action = False

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

        self.neco_walk_right = self.build_gif("animations/walking_right")
        self.neco_standing = self.build_gif("animations/standing")
        self.neco_run = self.build_gif("animations/running")
        self.neco_thinking = self.build_gif("animations/thinking")


    def build_gif(self, path):
        frames = []
        monitors = get_monitors()
        sorted(os.listdir(path), key=lambda x: int(x.split('.')[0]))
        for archive in sorted(os.listdir(path), key=lambda x: int(x.split('.')[0])):
            route = os.path.join(path, archive)
            frame = Image.open(route)
            pil_image = frame.convert('RGBA')

            original_width, original_height = pil_image.size
            aspect_ratio = original_width/original_height
            pet_height = int(monitors[0].height * 0.15)
            pet_width = int(pet_height * aspect_ratio)
            resized_frame = pil_image.resize((pet_width, pet_height))

            frames.append(pygame.image.fromstring(resized_frame.tobytes(), resized_frame.size, 'RGBA'))
            
        return frames
    
    def update(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN and not self.click_action:
                    self.click_action = True
                    self.thinking()
        self.click_action = False

    def action(self, function, times = 1):
        if function == self.walk_right and self.running:
            self.render(self.neco_walk_right[0])
        for _ in range(times):
            if not self.running:
                break
            self.update()
            function()
        if function == self.walk_right and self.running:
            self.render(self.neco_walk_right[0])

    def render(self, frame):
        self.screen.fill(self.black)
        self.screen.blit(frame, (self.pet_xposition, self.pet_yposition))
        pygame.display.flip()
        self.clock.tick(9)
        if not self.click_action:
            self.update()


    def walk_right(self, times = 1):
        for _ in range(times):
            for frame in self.neco_walk_right[1:-1]:
                if not self.running:
                    break
                self.render(frame)
                self.pet_xposition += 10
                if self.pet_xposition > self.monitors[0].width:
                    self.pet_xposition = -200
                    self.screen.fill(self.black)

    
    def standing(self):
        for frame in self.neco_standing:
            if not self.running:
                break
            self.render(frame)
    
    def thinking(self):
        for frame in self.neco_thinking:
            if not self.running:
                break
            self.render(frame)

        