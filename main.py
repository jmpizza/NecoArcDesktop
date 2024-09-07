import random as rd
import os
from screeninfo import get_monitors
from NecoPet import Neco
from PIL import Image
import pygame

def build_gif(numOfFrames, path):
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

neco_walk_right = build_gif(11,"animations/walking_right")
neco_standing = build_gif(9, "animations/standing")
neco_angry = ''
neco_run = ''

if __name__ == "__main__":
    neco = Neco()
    while neco.running:
        neco.update()
        neco.standing(neco_standing, 2)
        neco.walk_right(neco_walk_right,5)
    pygame.quit()

