class Stack: 

    def __init__(self):
        self.stack = []
        
    def size(self):
        return len(self.stack)

    def push(self, data):
        self.stack.append(data)
        #return f"Your stack {self.stack}"
        
    def pop(self):
        if len(self.stack) == 0:
            return "It's an empty stack"
        else:
            return self.stack.pop()
        
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return '~'


if __name__ == "__main__":
    print("Init STACK")
    st = Stack()
    print("Stack contains: ", st.__dict__)
    print("PUSHING '1', '2' and '3'")
    st.push(1)
    st.push(2)
    st.push(3)
    print("Stack contains: ", st.__dict__)
    print("GETTING SIZE")
    print(st.size())
    print("POPPING 4 elements")
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print("Stack contains: ", st.__dict__)