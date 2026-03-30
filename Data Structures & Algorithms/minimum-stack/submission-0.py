class MinStack:

    def __init__(self):
        self.x = []
        self.minim = []

    def push(self, val: int) -> None:
        self.x.append(val)
        if len(self.minim) == 0 or val <= self.minim[-1]:
            self.minim.append(val) 

    def pop(self) -> None:
        val = self.x[-1]
        self.x = self.x[:-1]
        if self.minim[-1] == val:
            self.minim= self.minim[:-1]
        return val

    def top(self) -> int:
        return self.x[-1]

    def getMin(self) -> int:
        return self.minim[-1]
        
