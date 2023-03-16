class Process:
    FINISH="finish"
    WAITING="waiting"
    RUNING="runing"

    def __init__(self, name: str, seconds: int):
        self.name = name
        self.seconds = seconds
        self.elapsed = 0
        self.state = Process.WAITING
        self.progress = 0
        self.remaining = seconds

    def tick(self):
        if(self.state == Process.RUNING):
            self.elapsed +=1
            self.remaining -=1
            self.progress = (self.elapsed / self.seconds) * 100
            if(self.progress >= 100):
                self.progress = 99.9
            if (self.remaining == 0):
                self.state = Process.FINISH

    def restart(self):
        self.state = Process.WAITING
        self.elapsed = 0
        self.remaining = self.seconds
        self.progress = 0
