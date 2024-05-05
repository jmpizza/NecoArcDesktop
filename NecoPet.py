import tkinter as tk
import pyautogui as pyt

class Neco:

    def __init__(self, path, screenHeight):
        self.root = tk.Tk()
        self.root.title('Neco')
        self.root.geometry(f'+500+{screenHeight-215}')
        self.root.config(highlightbackground='white')
        self.root.overrideredirect(True)
        self.root.wm_attributes('-transparentcolor', 'white', '-topmost', 1)
        self.frames = [tk.PhotoImage(file=path, format=f"gif -index {i}").subsample(3,3) for i in range(10)]
        self.label = tk.Label(self.root, image=self.frames[0],bd=0, bg='white')
        self.label.pack()
        self.index = 0
    
    def walkRight(self, times=10):
        if times > 0:
            self.label.config(image=self.frames[self.index % len(self.frames)])
            self.root.update()
            self.root.geometry(f'+{self.root.winfo_x()+10}+{self.root.winfo_y()}')
            self.index += 1
            if self.index >= 10: 
                self.index = 0
                times -= 1
            self.root.after(100, self.walkRight, times)  

    def walkLeft(self, times=10):
        if times > 0:
            self.label.config(image=self.frames[self.index % len(self.frames)])
            self.root.update()
            self.root.geometry(f'+{self.root.winfo_x()-10}+{self.root.winfo_y()}')
            self.index += 1
            if self.index >= 10:
                self.index = 0
                times -= 1
            self.root.after(100, self.walkRight, times)

    def startMovement(self):
        self.root.after(0,self.walkLeft)
    
    def run(self):
        self.startMovement()
        self.root.mainloop()