import random as rd
from screeninfo import get_monitors
from NecoPet import Neco
from PIL import Image
import win32gui
import win32con
import win32api
import pygame

def extract_frames(numOfFrames, path):
    gif = Image.open(path)
    frames = []
    monitors = get_monitors()
    for i in range(numOfFrames):
        pil_image = gif.convert('RGBA')


        original_width, original_height = pil_image.size
        aspect_ratio = original_width/original_height
        pet_height = int(monitors[0].height * 0.15)
        pet_width = int(pet_height * aspect_ratio)

        resized_image = pil_image.resize((pet_width, pet_height))

        frame = pygame.image.fromstring(resized_image.tobytes(), resized_image.size, 'RGBA')
        frames.append(frame)
        gif.seek(gif.tell() + 1)
    return frames

neco_walk = extract_frames(9,"gifs/Neco_Walk.gif")
neco_angry = ''
neco_run = ''

if __name__ == "__main__":
    neco = Neco()
    while neco.running:
        neco.update()
        neco.walk(neco_walk)
    pygame.quit()

