import tkinter as tk
import random
from tkinter import ttk
from screens.welcome import Welcome
from screens.processes import Processes
from data.queue import ProcessQueue
from data.process import Process
from data.nouns import get_random

class UI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("FCFS")
        self.window.attributes("-type", "dialog")
        self.processes_screen = None
        self.proc_num = tk.StringVar(value="5")
        self.show_welcome()

    def show_processes(self):
        self.list = ProcessQueue()
        for i in range(int(self.proc_num.get())):
            self.list.add(Process(get_random(), random.randint(2, 10)))
        self.welcome_screen.unmount()
        self.processes_screen = Processes(self.window, self.list, lambda:self.show_welcome()) 
        self.processes_screen.pack()

    def show_welcome(self):
        if (self.processes_screen is not None):
            self.processes_screen.unmount()
        self.welcome_screen = Welcome(self.window, lambda:self.show_processes(), self.proc_num)


    def mainloop(self):
        self.window.mainloop()

