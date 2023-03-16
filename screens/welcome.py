import tkinter as tk
from tkinter import ttk

class Welcome:
    def __init__(self, root, on_random, proc_num):
        self.frame = ttk.Frame(root, padding="5 5 5 5")
        self.frame.columnconfigure((2,), weight=2)
        self.frame.columnconfigure((0, 1), weight=1)
        tk.Label(self.frame, text="First Come First Served", font=("Arial", 20), justify="center").grid(column=0, row=1, columnspan=3, sticky=tk.EW, pady=5)
        tk.Label(self.frame, text="Procesos: ").grid(row=2, column=0, sticky=tk.EW)
        ttk.Spinbox(self.frame, from_=1, to=20, increment=1, textvariable=proc_num, state="readonly", width=10).grid(row=2, column=1, sticky=tk.EW)
        ttk.Button(self.frame, text="Generar Aleatorios", command=on_random).grid(row=2, column=2, sticky=tk.EW)
        self.frame.pack(fill=tk.BOTH, expand=True)

    def unmount(self):
        self.frame.destroy()
