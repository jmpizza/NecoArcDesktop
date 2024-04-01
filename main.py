import random as rd
import tkinter as tk
import pyautogui as pyt
from PIL import Image, ImageTk
import neco_moves

def neco_walk_right(label, frames, index, times):
    if index < 10:
        label.config(image=frames[index])
        label.after(100, neco_walk_right, label, frames, index+1, times)
        root.update()
        label.after(100, root.geometry, f'+{root.winfo_x()+10}+{root.winfo_y()}')
        
        print(root.winfo_geometry())
    elif times > 1:
        neco_walk_right(label, frames, 0, times-1)

def move_decision(type):
    if type == 1:
        movement = screenWidth-root.winfo_x
        

neco_walk = "Neco_Walk.gif"
neco_angry = ''
neco_run = ''
screenWidth, screenHeight = pyt.size()

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Neco')
    root.geometry(f'+-172+{screenHeight-215}')
    frames = [tk.PhotoImage(file=neco_walk, format=f"gif -index {i}").subsample(3,3) for i in range(10)]
    root.config(highlightbackground='white')
    root.overrideredirect(True)
    root.wm_attributes('-transparentcolor', 'white')
    label = tk.Label(root, image=frames[0],bd=0, bg='white')
    label.pack()
    neco_walk_right(label, frames, 0, 20)
    root.mainloop()