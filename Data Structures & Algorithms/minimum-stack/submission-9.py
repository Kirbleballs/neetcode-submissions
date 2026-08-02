class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val-self.min)
            if val < self.min:
                self.min = val
            
                

    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack[-1]
        if pop < 0:
            self.min -= pop
        self.stack = self.stack[:-1]


    def top(self) -> int:
        if self.stack[-1] <= -1:
            return(self.min)
        else:
            return(self.stack[-1] + self.min)


    def getMin(self) -> int:
        return(self.min)        



