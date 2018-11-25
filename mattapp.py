import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
from tkinter import ttk
import tkinter as tk
import time
from PIL import Image, ImageTk
from random import *


LARGE_FONT = ("ms serif", 20)
NORM_FONT = ("ms serif", 12)
SMALL_FONT = ("ms serif", 8)

style.use("ggplot")

f = plt.figure()
a = f.add_subplot(1,1,1)


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

class MattApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)

        #tk.Tk.iconbitmap(self, default='@/home/mats/Documents/tutorials/mattestudio.png')
        tk.Tk.wm_title(self, "Matteverkstan")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (StartPage, Bases, Kodtabell):
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
        self.configure(background='white')
        label = ttk.Label(self, text="Matteverkstan", font=LARGE_FONT, background='white')
        label.pack(pady=10,padx=10)


        button2 = ttk.Button(self, text="Baser", command=lambda: controller.show_frame(Bases))
        button2.pack()
        button3 = ttk.Button(self, text="Quit", command=sys.exit)
        button3.pack()



class Kodtabell(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='white')

        label = ttk.Label(self, text="Kodtabell", font=LARGE_FONT, background='white')
        label.grid(row=0, column=5, columnspan=2, pady=10)

        button1 = ttk.Button(self, text="Tillbaka", command=lambda: controller.show_frame(Bases))
        button1.grid(row=0, column=0, columnspan=1, padx=3, sticky="w")

        label0 = ttk.Label(self, text="a = 0", font=NORM_FONT, background="white")
        label0.grid(row=1, column=0, columnspan=2, padx=3, pady=3)
        label1 = ttk.Label(self, text="b = 1", font=NORM_FONT, background="white")
        label1.grid(row=2, column=0, columnspan=2, padx=3, pady=3)
        label2 = ttk.Label(self, text="c = 2", font=NORM_FONT, background="white")
        label2.grid(row=3, column=0, columnspan=2, padx=3, pady=3)
        label3 = ttk.Label(self, text="d = 3", font=NORM_FONT, background="white")
        label3.grid(row=4, column=0, columnspan=2, padx=3, pady=3)
        label4 = ttk.Label(self, text="e = 4", font=NORM_FONT, background="white")
        label4.grid(row=5, column=0, columnspan=2, padx=3, pady=3)
        label5 = ttk.Label(self, text="f = 5", font=NORM_FONT, background="white")
        label5.grid(row=6, column=0, columnspan=2, padx=3, pady=3)
        label6 = ttk.Label(self, text="g = 6", font=NORM_FONT, background="white")
        label6.grid(row=7, column=0, columnspan=2, padx=3, pady=3)
        label7 = ttk.Label(self, text="h = 7", font=NORM_FONT, background="white")
        label7.grid(row=8, column=0, columnspan=2, padx=3, pady=3)
        label8 = ttk.Label(self, text="i = 8", font=NORM_FONT, background="white")
        label8.grid(row=9, column=0, columnspan=2, padx=3, pady=3)
        label9 = ttk.Label(self, text="j = 9", font=NORM_FONT, background="white")
        label9.grid(row=10, column=0, columnspan=2, padx=3, pady=3)
        label10 = ttk.Label(self, text="k = 10", font=NORM_FONT, background="white")
        label10.grid(row=11, column=0, columnspan=2, padx=3, pady=3)
        label11 = ttk.Label(self, text="l = 11", font=NORM_FONT, background="white")
        label11.grid(row=12, column=0, columnspan=2, padx=3, pady=3)
        label12 = ttk.Label(self, text="m = 12", font=NORM_FONT, background="white")
        label12.grid(row=13, column=0, columnspan=2, padx=3, pady=3)

        label13 = ttk.Label(self, text="n = 13", font=NORM_FONT, background="white")
        label13.grid(row=1, column=2, columnspan=2, padx=3, pady=3)
        label14 = ttk.Label(self, text="o = 14", font=NORM_FONT, background="white")
        label14.grid(row=2, column=2, columnspan=2, padx=3, pady=3)
        label20 = ttk.Label(self, text="p = 15", font=NORM_FONT, background="white")
        label20.grid(row=3, column=2, columnspan=2, padx=3, pady=3)
        label21 = ttk.Label(self, text="q = 16", font=NORM_FONT, background="white")
        label21.grid(row=4, column=2, columnspan=2, padx=3, pady=3)
        label22 = ttk.Label(self, text="r = 17", font=NORM_FONT, background="white")
        label22.grid(row=5, column=2, columnspan=2, padx=3, pady=3)
        label23 = ttk.Label(self, text="s = 18", font=NORM_FONT, background="white")
        label23.grid(row=6, column=2, columnspan=2, padx=3, pady=3)
        label24 = ttk.Label(self, text="t = 19", font=NORM_FONT, background="white")
        label24.grid(row=7, column=2, columnspan=2, padx=3, pady=3)
        label25 = ttk.Label(self, text="u = 20", font=NORM_FONT, background="white")
        label25.grid(row=8, column=2, columnspan=2, padx=3, pady=3)
        label26 = ttk.Label(self, text="v = 21", font=NORM_FONT, background="white")
        label26.grid(row=9, column=2, columnspan=2, padx=3, pady=3)
        label27 = ttk.Label(self, text="w = 22", font=NORM_FONT, background="white")
        label27.grid(row=10, column=2, columnspan=2, padx=3, pady=3)
        label28 = ttk.Label(self, text="x = 23", font=NORM_FONT, background="white")
        label28.grid(row=11, column=2, columnspan=2, padx=3, pady=3)
        label29 = ttk.Label(self, text="y = 24", font=NORM_FONT, background="white")
        label29.grid(row=12, column=2, columnspan=2, padx=3, pady=3)
        label210 = ttk.Label(self, text="z = 25", font=NORM_FONT, background="white")
        label210.grid(row=13, column=2, columnspan=2, padx=3, pady=3)

        label30 = ttk.Label(self, text="! = 26", font=NORM_FONT, background="white")
        label30.grid(row=1, column=4, columnspan=2, padx=3, pady=3)
        label31 = ttk.Label(self, text="# = 27", font=NORM_FONT, background="white")
        label31.grid(row=2, column=4, columnspan=2, padx=3, pady=3)
        label32 = ttk.Label(self, text="$ = 28", font=NORM_FONT, background="white")
        label32.grid(row=3, column=4, columnspan=2, padx=3, pady=3)
        label33 = ttk.Label(self, text="% = 29", font=NORM_FONT, background="white")
        label33.grid(row=4, column=4, columnspan=2, padx=3, pady=3)
        label34 = ttk.Label(self, text="& = 30", font=NORM_FONT, background="white")
        label34.grid(row=5, column=4, columnspan=2, padx=3, pady=3)
        label35 = ttk.Label(self, text="( = 32", font=NORM_FONT, background="white")
        label35.grid(row=6, column=4, columnspan=2, padx=3, pady=3)
        label36 = ttk.Label(self, text=") = 33", font=NORM_FONT, background="white")
        label36.grid(row=7, column=4, columnspan=2, padx=3, pady=3)
        label37 = ttk.Label(self, text="+ = 34", font=NORM_FONT, background="white")
        label37.grid(row=8, column=4, columnspan=2, padx=3, pady=3)
        label38 = ttk.Label(self, text="- = 35", font=NORM_FONT, background="white")
        label38.grid(row=9, column=4, columnspan=2, padx=3, pady=3)
        label39 = ttk.Label(self, text="/ = 36", font=NORM_FONT, background="white")
        label39.grid(row=10, column=4, columnspan=2, padx=3, pady=3)
        label310 = ttk.Label(self, text=": = 37", font=NORM_FONT, background="white")
        label310.grid(row=11, column=4, columnspan=2, padx=3, pady=3)
        label311 = ttk.Label(self, text="; = 38", font=NORM_FONT, background="white")
        label311.grid(row=12, column=4, columnspan=2, padx=3, pady=3)
        label312 = ttk.Label(self, text=". = 39", font=NORM_FONT, background="white")
        label312.grid(row=13, column=4, columnspan=2, padx=3, pady=3)

        label40 = ttk.Label(self, text="A = 40", font=NORM_FONT, background="white")
        label40.grid(row=1, column=6, columnspan=2, padx=3, pady=3)
        label41 = ttk.Label(self, text="B = 41", font=NORM_FONT, background="white")
        label41.grid(row=2, column=6, columnspan=2, padx=3, pady=3)
        label42 = ttk.Label(self, text="C = 42", font=NORM_FONT, background="white")
        label42.grid(row=3, column=6, columnspan=2, padx=3, pady=3)
        label43 = ttk.Label(self, text="D = 43", font=NORM_FONT, background="white")
        label43.grid(row=4, column=6, columnspan=2, padx=3, pady=3)
        label44 = ttk.Label(self, text="E = 44", font=NORM_FONT, background="white")
        label44.grid(row=5, column=6, columnspan=2, padx=3, pady=3)
        label45 = ttk.Label(self, text="F = 45", font=NORM_FONT, background="white")
        label45.grid(row=6, column=6, columnspan=2, padx=3, pady=3)
        label46 = ttk.Label(self, text="G = 46", font=NORM_FONT, background="white")
        label46.grid(row=7, column=6, columnspan=2, padx=3, pady=3)
        label47 = ttk.Label(self, text="H = 47", font=NORM_FONT, background="white")
        label47.grid(row=8, column=6, columnspan=2, padx=3, pady=3)
        label48 = ttk.Label(self, text="I = 48", font=NORM_FONT, background="white")
        label48.grid(row=9, column=6, columnspan=2, padx=3, pady=3)
        label49 = ttk.Label(self, text="J = 49", font=NORM_FONT, background="white")
        label49.grid(row=10, column=6, columnspan=2, padx=3, pady=3)
        label410 = ttk.Label(self, text="K = 50", font=NORM_FONT, background="white")
        label410.grid(row=11, column=6, columnspan=2, padx=3, pady=3)
        label411 = ttk.Label(self, text="L = 51", font=NORM_FONT, background="white")
        label411.grid(row=12, column=6, columnspan=2, padx=3, pady=3)
        label412 = ttk.Label(self, text="M = 52", font=NORM_FONT, background="white")
        label412.grid(row=13, column=6, columnspan=2, padx=3, pady=3)

        label513 = ttk.Label(self, text="N = 53", font=NORM_FONT, background="white")
        label513.grid(row=1, column=8, columnspan=2, padx=3, pady=3)
        label514 = ttk.Label(self, text="O = 54", font=NORM_FONT, background="white")
        label514.grid(row=2, column=8, columnspan=2, padx=3, pady=3)
        label520 = ttk.Label(self, text="P = 55", font=NORM_FONT, background="white")
        label520.grid(row=3, column=8, columnspan=2, padx=3, pady=3)
        label521 = ttk.Label(self, text="Q = 56", font=NORM_FONT, background="white")
        label521.grid(row=4, column=8, columnspan=2, padx=3, pady=3)
        label522 = ttk.Label(self, text="R = 57", font=NORM_FONT, background="white")
        label522.grid(row=5, column=8, columnspan=2, padx=3, pady=3)
        label523 = ttk.Label(self, text="S = 58", font=NORM_FONT, background="white")
        label523.grid(row=6, column=8, columnspan=2, padx=3, pady=3)
        label524 = ttk.Label(self, text="T = 59", font=NORM_FONT, background="white")
        label524.grid(row=7, column=8, columnspan=2, padx=3, pady=3)
        label525 = ttk.Label(self, text="U = 60", font=NORM_FONT, background="white")
        label525.grid(row=8, column=8, columnspan=2, padx=3, pady=3)
        label526 = ttk.Label(self, text="V = 61", font=NORM_FONT, background="white")
        label526.grid(row=9, column=8, columnspan=2, padx=3, pady=3)
        label527 = ttk.Label(self, text="W = 62", font=NORM_FONT, background="white")
        label527.grid(row=10, column=8, columnspan=2, padx=3, pady=3)
        label528 = ttk.Label(self, text="X = 63", font=NORM_FONT, background="white")
        label528.grid(row=11, column=8, columnspan=2, padx=3, pady=3)
        label529 = ttk.Label(self, text="Y = 64", font=NORM_FONT, background="white")
        label529.grid(row=12, column=8, columnspan=2, padx=3, pady=3)
        label5210 = ttk.Label(self, text="Z = 65", font=NORM_FONT, background="white")
        label5210.grid(row=13, column=8, columnspan=2, padx=3, pady=3)

        label60 = ttk.Label(self, text="0 = 67", font=NORM_FONT, background="white")
        label60.grid(row=1, column=10, columnspan=2, padx=3, pady=3)
        label61 = ttk.Label(self, text="1 = 68", font=NORM_FONT, background="white")
        label61.grid(row=2, column=10, columnspan=2, padx=3, pady=3)
        label62 = ttk.Label(self, text="2 = 69", font=NORM_FONT, background="white")
        label62.grid(row=3, column=10, columnspan=2, padx=3, pady=3)
        label63 = ttk.Label(self, text="3 = 70", font=NORM_FONT, background="white")
        label63.grid(row=4, column=10, columnspan=2, padx=3, pady=3)
        label64 = ttk.Label(self, text="4 = 71", font=NORM_FONT, background="white")
        label64.grid(row=5, column=10, columnspan=2, padx=3, pady=3)
        label65 = ttk.Label(self, text="5 = 72", font=NORM_FONT, background="white")
        label65.grid(row=6, column=10, columnspan=2, padx=3, pady=3)
        label66 = ttk.Label(self, text="6 = 73", font=NORM_FONT, background="white")
        label66.grid(row=7, column=10, columnspan=2, padx=3, pady=3)
        label67 = ttk.Label(self, text="7 = 74", font=NORM_FONT, background="white")
        label67.grid(row=8, column=10, columnspan=2, padx=3, pady=3)
        label68 = ttk.Label(self, text="8 = 75", font=NORM_FONT, background="white")
        label68.grid(row=9, column=10, columnspan=2, padx=3, pady=3)
        label69 = ttk.Label(self, text="9 = 76", font=NORM_FONT, background="white")
        label69.grid(row=10, column=10, columnspan=2, padx=3, pady=3)

        
class Bases(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='white')
        self.i = 0
        self.j = 0
        label = ttk.Label(self, text="Talbaser", font=LARGE_FONT, background="white")
        label.grid(row=0, column=1, columnspan=2, pady=10)
        self.rand_ans = 18
        def change_new():
            button1.configure(text="Nytt tal", command=combine_funcs(clear_text, run_binary, change_ans))

        def change_ans():
            button1.configure(text="Svara", command=combine_funcs(get_value, change_new))

        def run_binary():
            self.rand_ans = randint(0, 32)
            label0.config(text=str(self.rand_ans))
            self.j += 1


        #Binary to denary conversion
        def binary_converter(bi):
            binary = bi
            denary = 0
            for digit in binary:
                #A left shift in binary means x2
                denary = denary*2 + int(digit)
                print("Your denary number is: " + str(denary))



        def denary_convert(dec):
             #Denary to binary conversion
            denary = dec
            binary=""
            while denary>0:
                  #A left shift in binary means /2
                  binary = str(denary%2) + binary
                  denary = denary//2
            return binary



        def clear_text():
            self.e2.delete(0, 'end')

        def get_value():

            ans = self.e2.get()
            fixed_ans = ans.replace(" ", "")
            correct_ans = denary_convert(self.rand_ans)
            string_correct_ans = str(correct_ans)

            if (fixed_ans==correct_ans):
                label4.config(text="Rätt!")
                if(self.i == self.j):
                    self.i += 1
                    label5.config(text=str(self.i))

            else:
                label4.config(text="Det var tyvärr fel. Prova igen!")
                self.i = 0
                label5.config(text=str(self.i))



        button1 = ttk.Button(self, text="Hem", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0, column=0, columnspan=1, padx=3, sticky="w")

        label1 = ttk.Label(self, text="Konvertera decimaltalet till ett binärtal", font=NORM_FONT, background="white")
        label1.grid(row=3, column=0, columnspan=3, padx=3, pady=3)

        label0 = ttk.Label(self, text=str(self.rand_ans), font=LARGE_FONT, background="white")
        label0.grid(row=4, column=0, padx=3, pady=3, sticky="w")

        label3 = ttk.Label(self, text="Svar: ", font=NORM_FONT, background="white")
        label3.grid(row=5, column=0, sticky="w", padx=3)

        self.e2 = ttk.Entry(self)
        self.e2.grid(row=5, column=1, columnspan=2,padx=3, pady=3, sticky="w")

        button0 = ttk.Button(self, text="Kodtabell", command=lambda: controller.show_frame(Kodtabell))
        button0.grid(row=4, column=3,columnspan=1, padx=3, sticky="w")

        button1 = ttk.Button(self, text="Svara", command=combine_funcs(get_value, change_new))
        button1.grid(row=5, column=3,columnspan=1, padx=3, sticky="w")

        label5 = ttk.Label(self, text="Antal rätt i rad: " + str(self.i), font=NORM_FONT, background="white")
        label5.grid(row=7, column=0, columnspan=1, sticky="w", padx=3)

        label4 = ttk.Label(self, text="", font=NORM_FONT, background="white")
        label4.grid(row=7, column=1, columnspan=4, sticky="w", padx=3)


app = MattApp()
#ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()
