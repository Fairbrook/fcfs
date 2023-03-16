from data.process import Process

class ProcessQueue:
    def __init__(self):
        self.queue: List[Process] = list()
        self.finished = False
        self.active_index = 0

    def add(self, proc: Process):
        self.queue.append(proc)

    def get_active(self):
        return self.queue[self.active_index]

    def next_proc(self):
        if(self.active_index >= len(self.queue)-1):
            self.finished = True
            return
        self.active_index += 1

    def tick(self):
        if(len(self.queue) == 0 or self.finished):
            return
        if(self.get_active().state == Process.WAITING):
            self.get_active().state = Process.RUNING
        for proc in self.queue:
            proc.tick()
        if(self.get_active().state == Process.FINISH):
            self.next_proc()

    def restart(self):
        self.active_index = 0
        self.finished = False
        for proc in self.queue:
            proc.restart()
