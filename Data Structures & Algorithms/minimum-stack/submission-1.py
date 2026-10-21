class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_stack.append(val)
        else:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        if len(self.stack) > 0:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()
        else:
            return None
        

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
        

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.min_stack[-1]
        else:
            return None
        
