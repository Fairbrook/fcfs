from tkinter import ttk
import tkinter as tk
from screens.process import ProcessComponent
from data.process import Process
from data.queue import ProcessQueue

class Processes:
    def __init__(self, root, processes: ProcessQueue,on_back):
        self.frame = ttk.Frame(root, padding="5 5 5 5")
        self.runing = False
        self.started = False
        self.processes = processes
        self.task_id = None
        self.state = tk.StringVar(value=f"Estado: {self.get_state()}")
        self.processComponents = [ProcessComponent(self.frame, proc) for proc in self.processes.queue]
        for component in self.processComponents:
            component.pack()
        ttk.Button(self.frame, text="Regresar", command=on_back).pack(side=tk.BOTTOM, expand=True, anchor=tk.NW, fill=tk.X)
        tk.Label(self.frame, textvariable=self.state).pack(side=tk.BOTTOM, expand=True, anchor=tk.NW, fill=tk.X)
        ttk.Button(self.frame, text="Iniciar", command=lambda:self.start()).pack(side=tk.LEFT, expand=True, fill=tk.X)
        ttk.Button(self.frame, text="Pausar", command=lambda:self.pause()).pack(side=tk.LEFT, expand=True, fill=tk.X)
        ttk.Button(self.frame, text="Reiniciar", command=lambda:self.restart()).pack(side=tk.LEFT, expand=True, fill=tk.X)

    def start(self):
        self.runing = True
        self.started = True
        self.update()
        self.frame.after(1000, self.tick)

    def pause(self):
        self.cancel_task()
        self.runing = False
        self.update()

    def restart(self):
        self.cancel_task()
        self.started = False
        self.processes.restart()
        self.update()
        if(self.runing):
            self.start()
            return

    def get_state(self):
        if(not self.started):
            return "En Espera"
        if(self.runing):
            if(self.processes.finished):
                return "Terminado"
            return "En Ejecución"
        return "Pausado"


    def cancel_task(self):
        if(self.task_id is not None):
            self.frame.after_cancel(self.task_id)


    def update(self):
        self.state.set(f'Estado: {self.get_state()}')
        for index, proc in enumerate(self.processComponents):
            proc.update(self.processes.queue[index])

    def tick(self):
        if(not self.runing):
            return
        self.processes.tick()
        self.update()
        if(not self.processes.finished):
            self.task_id = self.frame.after(1000, self.tick)

    def pack(self):
        self.frame.pack(fill=tk.BOTH)

    def unmount(self):
        self.cancel_task()
        self.frame.destroy()
        

