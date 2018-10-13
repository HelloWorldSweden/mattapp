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


# i for intervall
def animate(i):

    bins = 11
    dice_rolled= Dice.stat
    a.clear()
    a.hist(dice_rolled, bins, rwidth=0.8, color="skyblue")




class Dice(tk.Tk):
    stat = []
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)


        self.wm_title("Dices")

        self.i=0
        # StringVar() updates result label automatically
        self.text = tk.StringVar()

        # set initial value of text
        self.text.set("")

        # create the result label
        #result = ttk.Label(self, textvariable=self.text)
        #result.grid(row=3, column=0, columnspan=3)

        self.dice_list = self.create_dice()
        self.dice_list2 = self.create_dice2()

        # start with an empty canvas
        self.dice_list[0].grid(row=1, column=0, columnspan=3, padx=5, pady=3)
        self.dice_list2[0].grid(row=1, column=1, columnspan=3, padx=5, pady=3)
        button = ttk.Button(self, text="Roll", command=combine_funcs(self.click, self.click2))
        button.grid(row=2, column=0, columnspan=2, padx=5, pady=3)
        button1 = ttk.Button(self, text="Fast roll", command=combine_funcs(self.click_fast1, self.click_fast2))
        button1.grid(row=2, column=2, columnspan=2, padx=5, pady=3)
        button2 = ttk.Button(self, text="Quit", command=self.destroy)
        button2.grid(row=3,column=0, columnspan=2, padx=5, pady=3)



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
            dots.get(arg)(x, y, r) # Gets the diccolumspan=2,tionary keys while passing in x, y, and r values

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
        self.i += 1
        print(self.i)
        self.dice1 = 0
        t = 50 # start with a time delay of 100 ms and increase it as the dice rolls
        stop = randint(13, 18) # chooses random number between 13 - 17
        for x in range(stop):
            dice_index = x % 6 + 1 # gets the randomly selected dice head by modulo
            self.dice_list[dice_index].grid(row=1, column=0, columnspan=3, padx=5, pady=3)
            self.update()
            if x == stop - 1:
                # set text to the selected result
                self.text.set(str(x % 6 + 1))
                self.dice1 = (x%6+1)
                break
            self.after(t, self.dice_list[dice_index].grid_forget()) # forgets the grid and restarts
            t += 15
        print(self.dice1)


    def click2(self):
        self.dice2 = 0
        t = 50 # start with a time delay of 100 ms and increase it as the dice rolls
        stop = randint(13, 18) # chooses random number between 13 - 17
        for x in range(stop):
            dice_index = x % 6 + 1 # gets the randomly selected dice head by modulo
            self.dice_list2[dice_index].grid(row=1, column=1, columnspan=3, padx=5, pady=3)
            self.update()
            if x == stop - 1:
                # set text to the selected result
                self.text.set(str(x % 6 + 1))
                self.dice2 = (x%6+1)
                break
            self.after(t, self.dice_list2[dice_index].grid_forget()) # forgets the grid and restarts
            t += 15

        print(self.dice2)
        Dice.stat.append(self.dice1 + self.dice2)
        print(self.stat)
        if(self.i == 1):
            self.popup_problem1()
            print(self.i)
        if(self.i==3):
            self.popup_problem2()
            print(self.i)
        if(self.i==5):
            self.popup_problem3()
            print(self.i)
        if(self.i==7):
            self.popup_problem4()
            print(self.i)
        if(self.i==9):
            self.popup_problem5()
            print(self.i)
        if(self.i==11):
            self.popup_problem6()
            print(self.i)


    def click_fast1(self):
        self.dice1 = 0
        x = randint(13, 18) # chooses random number between 13 - 17

        self.dice1 = (x%6+1)

        print(self.dice1)


    def click_fast2(self):
        self.dice2 = 0
        x = randint(13, 18) # chooses random number between 13 - 17

        self.dice2 = (x%6+1)

        print(self.dice2)
        Dice.stat.append(self.dice1 + self.dice2)
        print(self.stat)

    def popup_problem1(self):
        popup = tk.Tk()

        def get_value():
            ans = e1.get()
            corr_ans = ans.replace(" ", "")
            print(corr_ans)
            if (corr_ans=="1/36"):
                result1 = ttk.Label(popup, text="Rätt!", font=LARGE_FONT)
                result1.grid(row=3, column=0, columnspan=2)

            else:
                result1 = ttk.Label(popup, text="Det var tyvärr fel. Prova igen!")
                result1.grid(row=3, column=0, columnspan=2)


        popup.wm_title("Problem")
        label1 = ttk.Label(popup, text="Hur stor är sannolikheten att kasta två ettor nästa gång du kastar?", font=NORM_FONT)
        label1.grid(row=0, columnspan=2, padx=3, pady=3, sticky="w")
        label2=ttk.Label(popup, text="Svara exakt", font=SMALL_FONT)
        label2.grid(row=1, columnspan=2, padx=3, pady=3, sticky="w")
        label3 = ttk.Label(popup, text="Svar: ", font=NORM_FONT)
        label3.grid(row=2, column=0, sticky="w", padx=3, pady=3)

        e1 = ttk.Entry(popup)
        e1.grid(row=2, column=0, sticky="e")

        button1 = ttk.Button(popup, text="Svara", command=get_value)
        button1.grid(row=2, column=1, padx=3, pady=3, sticky="e")
        button2 = ttk.Button(popup, text="Quit", command=popup.destroy)
        button2.grid(row=3, column=1, padx=3, pady=3, sticky="e")
        popup.mainloop()

    def popup_problem2(self):
        popup = tk.Tk()
        def get_value():
            ans = e1.get()
            corr_ans = ans.replace(" ", "")
            print(corr_ans)
            if (corr_ans=="1/6"):
                result3 = ttk.Label(popup, text="Rätt!", font=LARGE_FONT)
                result3.grid(row=3, column=0, columnspan=2)

            else:
                result4 = ttk.Label(popup, text="Det var tyvärr fel. Prova igen!")
                result4.grid(row=3, column=0, columnspan=2)

                #result2.destroy()

        popup.wm_title("Problem")
        label1 = ttk.Label(popup, text="""Hur stor är sannolikheten att få en sammanlagd summa av 7
nästa gång du kastar?""", font=NORM_FONT)
        label1.grid(row=0, columnspan=2, padx=3, pady=3, sticky="w")
        label2=ttk.Label(popup, text="Svara exakt", font=SMALL_FONT)
        label2.grid(row=1, columnspan=2, padx=3, pady=3, sticky="w")
        label3 = ttk.Label(popup, text="Svar: ", font=NORM_FONT)
        label3.grid(row=2, column=0, sticky="w", padx=3, pady=3)

        e1 = ttk.Entry(popup)
        e1.grid(row=2, column=0, sticky="e")

        button1 = ttk.Button(popup, text="Svara", command=get_value)
        button1.grid(row=2, column=1, padx=3, pady=3, sticky="e")
        button2 = ttk.Button(popup, text="Quit", command=popup.destroy)
        button2.grid(row=3, column=1, padx=3, pady=3, sticky="e")
        popup.mainloop()

    def popup_problem3(self):
        popup = tk.Tk()

        def get_value():
            ans = e1.get()
            corr_ans = ans.replace(" ", "")
            print(corr_ans)
            if (corr_ans=="15/36"):
                result5 = ttk.Label(popup, text="Rätt!", font=LARGE_FONT)
                result5.grid(row=3, column=0, columnspan=2)

            else:
                result6 = ttk.Label(popup, text="Det var tyvärr fel. Prova igen!")
                result6.grid(row=3, column=0, columnspan=2)

                #result2.destroy()

        popup.wm_title("Problem")
        label1 = ttk.Label(popup, text="""Hur stor är sannolikheten att summan är större än 7
nästa gång du kastar?""", font=NORM_FONT)
        label1.grid(row=0, columnspan=2, padx=3, pady=3, sticky="w")
        label2=ttk.Label(popup, text="Svara exakt", font=SMALL_FONT)
        label2.grid(row=1, columnspan=2, padx=3, pady=3, sticky="w")
        label3 = ttk.Label(popup, text="Svar: ", font=NORM_FONT)
        label3.grid(row=2, column=0, sticky="w", padx=3, pady=3)

        e1 = ttk.Entry(popup)
        e1.grid(row=2, column=0, sticky="e")

        button1 = ttk.Button(popup, text="Svara", command=get_value)
        button1.grid(row=2, column=1, padx=3, pady=3, sticky="e")
        button2 = ttk.Button(popup, text="Quit", command=popup.destroy)
        button2.grid(row=3, column=1, padx=3, pady=3, sticky="e")
        popup.mainloop()


    def popup_problem4(self):
        popup = tk.Tk()

        def get_value():
            ans = e1.get()
            corr_ans = ans.replace(" ", "")
            print(corr_ans)
            if (corr_ans=="0.03"):
                result7 = ttk.Label(popup, text="Rätt!", font=LARGE_FONT)
                result7.grid(row=3, column=0, columnspan=2)

            else:
                result8 = ttk.Label(popup, text="Det var tyvärr fel. Prova igen!")
                result8.grid(row=3, column=0, columnspan=2)


        popup.wm_title("Problem")
        label1 = ttk.Label(popup, text="Hur stor är sannolikheten i procent att kasta två ettor nästa gång du kastar?", font=NORM_FONT)
        label1.grid(row=0, columnspan=2, padx=3, pady=3, sticky="w")
        label2=ttk.Label(popup, text="Avrunda till två decimaler", font=SMALL_FONT)
        label2.grid(row=1, columnspan=2, padx=3, pady=3, sticky="w")
        label3 = ttk.Label(popup, text="Svar: ", font=NORM_FONT)
        label3.grid(row=2, column=0, sticky="w", padx=3, pady=3)

        e1 = ttk.Entry(popup)
        e1.grid(row=2, column=0, sticky="e")

        button1 = ttk.Button(popup, text="Svara", command=get_value)
        button1.grid(row=2, column=1, padx=3, pady=3, sticky="e")
        button2 = ttk.Button(popup, text="Quit", command=popup.destroy)
        button2.grid(row=3, column=1, padx=3, pady=3, sticky="e")
        popup.mainloop()

    def popup_problem5(self):
        popup = tk.Tk()
        def get_value():
            ans = e1.get()
            corr_ans = ans.replace(" ", "")
            print(corr_ans)
            if (corr_ans=="0.17"):
                result9 = ttk.Label(popup, text="Rätt!", font=LARGE_FONT)
                result9.grid(row=3, column=0, columnspan=2)

            else:
                result10 = ttk.Label(popup, text="Det var tyvärr fel. Prova igen!")
                result10.grid(row=3, column=0, columnspan=2)

                #result2.destroy()

        popup.wm_title("Problem")
        label1 = ttk.Label(popup, text="""Hur stor är sannolikheten i procent att få en sammanlagd summa av 7
nästa gång du kastar?""", font=NORM_FONT)
        label1.grid(row=0, columnspan=2, padx=3, pady=3, sticky="w")
        label2=ttk.Label(popup, text="Avrunda till två decimaler", font=SMALL_FONT)
        label2.grid(row=1, columnspan=2, padx=3, pady=3, sticky="w")
        label3 = ttk.Label(popup, text="Svar: ", font=NORM_FONT)
        label3.grid(row=2, column=0, sticky="w", padx=3, pady=3)

        e1 = ttk.Entry(popup)
        e1.grid(row=2, column=0, sticky="e")

        button1 = ttk.Button(popup, text="Svara", command=get_value)
        button1.grid(row=2, column=1, padx=3, pady=3, sticky="e")
        button2 = ttk.Button(popup, text="Quit", command=popup.destroy)
        button2.grid(row=3, column=1, padx=3, pady=3, sticky="e")
        popup.mainloop()

    def popup_problem6(self):
        popup = tk.Tk()

        def get_value():
            ans = e1.get()
            corr_ans = ans.replace(" ", "")
            print(corr_ans)
            if (corr_ans=="0.42"):
                result11 = ttk.Label(popup, text="Rätt!", font=LARGE_FONT)
                result11.grid(row=3, column=0, columnspan=2)

            else:
                result12 = ttk.Label(popup, text="Det var tyvärr fel. Prova igen!")
                result12.grid(row=3, column=0, columnspan=2)

                #result2.destroy()

        popup.wm_title("Problem")
        label1 = ttk.Label(popup, text="""Hur stor är sannolikheten i procent att summan är större än 7
nästa gång du kastar?""", font=NORM_FONT)
        label1.grid(row=0, columnspan=2, padx=3, pady=3, sticky="w")
        label2=ttk.Label(popup, text="Svara exakt", font=SMALL_FONT)
        label2.grid(row=1, columnspan=2, padx=3, pady=3, sticky="w")
        label3 = ttk.Label(popup, text="Svar: ", font=NORM_FONT)
        label3.grid(row=2, column=0, sticky="w", padx=3, pady=3)

        e1 = ttk.Entry(popup)
        e1.grid(row=2, column=0, sticky="e")

        button1 = ttk.Button(popup, text="Svara", command=get_value)
        button1.grid(row=2, column=1, padx=3, pady=3, sticky="e")
        button2 = ttk.Button(popup, text="Quit", command=popup.destroy)
        button2.grid(row=3, column=1, padx=3, pady=3, sticky="e")
        popup.mainloop()


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

        for F in (StartPage, Graph, Bases):
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

        button1 = ttk.Button(self, text="Diagram", command=lambda: controller.show_frame(Graph))
        button1.pack()
        button2 = ttk.Button(self, text="Bases", command=lambda: controller.show_frame(Bases))
        button2.pack()
        button3 = ttk.Button(self, text="Quit", command=sys.exit)
        button3.pack()



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

class Bases(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='white')

        label = ttk.Label(self, text="Talbaser", font=LARGE_FONT, background="white")
        label.grid(row=0, column=2, columnspan=2, pady=10)
        self.rand_ans = 18
        def run_binary():
            self.rand_ans = randint(0, 50)
            label0.config(text=str(self.rand_ans))
        #Binary Converter - www.101computing.net/binary-converter-using-python/

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
            print("Your binary number is: " + binary)
            return binary
        def clear_text():
            self.e2.delete(0, 'end')

        def get_value():

            ans = self.e2.get()
            fixed_ans = ans.replace(" ", "")
            correct_ans = denary_convert(self.rand_ans)
            string_correct_ans = str(correct_ans)
            print(fixed_ans)

            if (fixed_ans==correct_ans):
                #result = ttk.Label(self, text="Rätt!", font=LARGE_FONT, background="white")
                #result.pack(anchor="center")
                label4.config(text="Rätt!")
            else:
                #result = ttk.Label(self, text="Det var tyvärr fel. Prova igen!")
                #result.pack()
                label4.config(text="Det var tyvärr fel. Prova igen!")


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

        button0 = ttk.Button(self, text="Nytt tal", command=combine_funcs(clear_text,run_binary))
        button0.grid(row=4, column=3,columnspan=1, padx=3, sticky="w")
        button1 = ttk.Button(self, text="Svara", command=get_value)
        button1.grid(row=5, column=3,columnspan=1, padx=3, sticky="w")
        label4 = ttk.Label(self, text="", font=NORM_FONT, background="white")
        label4.grid(row=7, column=0, columnspan=4, sticky="w", padx=3)
        #button2 = ttk.Button(self, text="Quit", command=self.destroy)
        #button2.grid(row=9, column=0,columnspan=1, padx=3, sticky="w")


app = MattApp()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()
