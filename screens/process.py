from tkinter import ttk
import tkinter as tk
from data.process import Process

class ProcessComponent:
    def __init__(self, root, proc: Process):
        self.frame = tk.Frame(root)
        self.elapsed = tk.StringVar()
        self.elapsed.set(self.get_status(proc))
        self.progress = tk.IntVar(value=proc.progress)
        self.progress.set(0.1)
        self.frame.columnconfigure((0,1,2,3,4,5), weight=1)
        self.frame.rowconfigure((1,2), weight=1)
        tk.Label(self.frame, text=proc.name, width=10, anchor=tk.E).grid(row=1, column=0, sticky=tk.W)
        tk.Label(self.frame, textvariable=self.elapsed).grid(row=1, column=1, sticky=tk.W)
        tk.Label(self.frame, text=f'Total: {proc.seconds}s', width=20, anchor=tk.E).grid(row=1, column=5, sticky=tk.E)
        ttk.Progressbar(self.frame, variable=self.progress).grid(row=2, column=1, columnspan=5, padx=5, sticky=tk.NSEW)

    def get_status(self, proc:Process):
        if(proc.state == Process.WAITING):
            return "En Espera"
        if(proc.state == Process.FINISH):
            return "Terminado"
        return f"Up: {proc.elapsed}s"

    def update(self, proc: Process):
        self.elapsed.set(self.get_status(proc))
        self.progress.set(proc.progress)

    def pack(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def unmount(self):
        self.frame.destroy()
