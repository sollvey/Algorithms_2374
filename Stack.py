class Stack: 

    def __init__(self):
        self.stack = []
        
    def size(self):
        return f"Length of stack = {len(self.stack)}"

    def push(self, data):
        self.stack.append(data)
        return f"Your stack {self.stack}"
        
    def pop(self):
        if len(self.stack) == 0:
            return "It's an empty stack"
        else:
            removed = self.stack.pop()
            return f"{removed} was deleted from stack"
