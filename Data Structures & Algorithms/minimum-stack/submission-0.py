class MinStack:

    def __init__(self):
        self.val_stack = []
        self.mins_stack = []

    def push(self, val: int) -> None:
        self.val_stack.append(val)  

        if not self.mins_stack or val <= self.mins_stack[-1]:
            self.mins_stack.append(val)
        else:
            self.mins_stack.append(self.mins_stack[-1])

    def pop(self) -> None:
        if not self.val_stack:
            return
        
        self.val_stack.pop()
        self.mins_stack.pop()


    def top(self) -> int:
        return self.val_stack[-1]

    def getMin(self) -> int:
        return self.mins_stack[-1]
