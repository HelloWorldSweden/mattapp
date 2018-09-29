import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from tkinter import ttk
import tkinter as tk

from random import *


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

style.use("ggplot")

f = plt.figure()
a = f.add_subplot(1,1,1)

class Dice(tk.Tk):
    stat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)

        self.wm_title("Dices")


        # StringVar() updates result label automatically
        self.text = tk.StringVar()

        # set initial value of text
        self.text.set("")

        # create the result label
        result = ttk.Label(self, textvariable=self.text)
        result.grid(row=3, column=0, columnspan=3)

        self.dice_list = self.create_dice()
        self.dice_list2 = self.create_dice2()

        # start with an empty canvas
        self.dice_list[0].grid(row=1, column=0, columnspan=3)
        self.dice_list2[0].grid(row=1, column=1, columnspan=3)
        button = ttk.Button(self, text="Roll", command=combine_funcs(self.click, self.click2))
        button.grid(row=2, column=0, padx=3, pady=3)
        button1 = ttk.Button(self, text="Quit", command=self.destroy)
        button1.grid(row=2, column=1, pady=3)
        #Dice.stat = []


    def create_dice(self):

        dice = list()
        dice.append(self.draw_dice('dot0'))  # empty
        dice.append(self.draw_dice('dot4'))  # center dot --> 1
        dice.append(self.draw_dice('dot3', 'dot5'))  # dice head 2
        dice.append(self.draw_dice('dot2', 'dot4', 'dot6'))  # dice head 3
        dice.append(self.draw_dice('dot1', 'dot2', 'dot6', 'dot9'))  # dice head 4
        dice.append(self.draw_dice('dot1', 'dot2', 'dot4', 'dot6', 'dot9'))  # dice head 5
        dice.append(self.draw_dice('dot1', 'dot2', 'dot3', 'dot5', 'dot6', 'dot9'))  # dice head 6
        return dice

    def create_dice2(self):

        dice = list()
        dice.append(self.draw_dice2('dot0'))  # empty
        dice.append(self.draw_dice2('dot4'))  # center dot --> 1
        dice.append(self.draw_dice2('dot3', 'dot5'))  # dice head 2
        dice.append(self.draw_dice2('dot2', 'dot4', 'dot6'))  # dice head 3
        dice.append(self.draw_dice2('dot1', 'dot2', 'dot6', 'dot9'))  # dice head 4
        dice.append(self.draw_dice2('dot1', 'dot2', 'dot4', 'dot6', 'dot9'))  # dice head 5
        dice.append(self.draw_dice2('dot1', 'dot2', 'dot3', 'dot5', 'dot6', 'dot9'))  # dice head 6
        return dice

    def draw_dice(self, *args):

        w, h = 23, 23 # sets width and height
        x, y, r = 2, 2, 5 # sets x, y, and radius
        c = tk.Canvas(self, width=w, height=h, bg='white') # creates canvas c

        #Dictionary containing lambda functions to draw dots on canvas c
        dots = {
            'dot0': lambda x, y, r: c,
            'dot1': lambda x, y, r: c.create_oval(x, y, x + r, y + r, fill='black'),
            'dot2': lambda x, y, r: c.create_oval(x + 16, y, (x + 16) + r, y + r, fill='black'),
            'dot3': lambda x, y, r: c.create_oval(x, y + 8, x + r, (y + 8) + r, fill='black'),
            'dot4': lambda x, y, r: c.create_oval(x + 8, (y + 8), (x + 8) + r, (y + 8) + r, fill='black'),
            'dot5': lambda x, y, r: c.create_oval(x + 16, (y + 8), (x + 16) + r, (y + 8) + r, fill='black'),
            'dot6': lambda x, y, r: c.create_oval(x, y + 16, x + r, (y + 16) + r, fill='black'),
            'dot9': lambda x, y, r: c.create_oval(x + 16, y + 16, (x + 16) + r, (y + 16) + r, fill='black')
        }

        for arg in args:
            dots.get(arg)(x, y, r) # Gets the dictionary keys while passing in x, y, and r values

        return c

    def draw_dice2(self, *args):

        w, h = 23, 23 # sets width and height
        x, y, r = 2, 2, 5 # sets x, y, and radius
        c = tk.Canvas(self, width=w, height=h, bg='white') # creates canvas c

        #Dictionary containing lambda functions to draw dots on canvas c
        dots = {
            'dot0': lambda x, y, r: c,
            'dot1': lambda x, y, r: c.create_oval(x, y, x + r, y + r, fill='black'),
            'dot2': lambda x, y, r: c.create_oval(x + 16, y, (x + 16) + r, y + r, fill='black'),
            'dot3': lambda x, y, r: c.create_oval(x, y + 8, x + r, (y + 8) + r, fill='black'),
            'dot4': lambda x, y, r: c.create_oval(x + 8, (y + 8), (x + 8) + r, (y + 8) + r, fill='black'),
            'dot5': lambda x, y, r: c.create_oval(x + 16, (y + 8), (x + 16) + r, (y + 8) + r, fill='black'),
            'dot6': lambda x, y, r: c.create_oval(x, y + 16, x + r, (y + 16) + r, fill='black'),
            'dot9': lambda x, y, r: c.create_oval(x + 16, y + 16, (x + 16) + r, (y + 16) + r, fill='black')
        }

        for arg in args:
           dots.get(arg)(x, y, r) # Gets the dictionary keys while passing in x, y, and r values

        return c


    def click(self):
        self.dice1 = 0
        t = 100 # start with a time delay of 100 ms and increase it as the dice rolls
        stop = randint(13, 18) # chooses random number between 13 - 17
        for x in range(stop):
            dice_index = x % 6 + 1 # gets the randomly selected dice head by modulo
            self.dice_list[dice_index].grid(row=1, column=0, columnspan=3)
            self.update()
            if x == stop - 1:
                # set text to the selected result
                self.text.set(str(x % 6 + 1))
                self.dice1 = (x%6+1)
                break
            self.after(t, self.dice_list[dice_index].grid_forget()) # forgets the grid and restarts
            t += 25
        print(self.dice1)


    def click2(self):
        self.dice2 = 0
        t = 100 # start with a time delay of 100 ms and increase it as the dice rolls
        stop = randint(13, 18) # chooses random number between 13 - 17
        for x in range(stop):
            dice_index = x % 6 + 1 # gets the randomly selected dice head by modulo
            self.dice_list2[dice_index].grid(row=1, column=1, columnspan=3)
            self.update()
            if x == stop - 1:
                # set text to the selected result
                self.text.set(str(x % 6 + 1))
                self.dice2 = (x%6+1)
                break
            self.after(t, self.dice_list2[dice_index].grid_forget()) # forgets the grid and restarts
            t += 25

        print(self.dice2)
        Dice.stat.append(self.dice1 + self.dice2)
        print(self.stat)
# i for intervall
def animate(i):

    bins = 12
    dice_rolled= Dice.stat
    a.clear()
    a.hist(dice_rolled, bins)



class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)

        #tk.Tk.iconbitmap(self, default='@/home/mats/Documents/tutorials/mattestudio.png')
        tk.Tk.wm_title(self, "Matteverkstan")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (StartPage, Graph):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()





class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Matteverkstan", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Diagram", command=lambda: controller.show_frame(Graph))
        button1.pack()

        button2 = ttk.Button(self, text="Quit", command=quit)
        button2.pack()



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to home", command=lambda: controller.show_frame(StartPage))
        button1.pack()



class Graph(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Throw dices", command=Dice)
        button2.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)







app = SeaofBTCapp()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()
