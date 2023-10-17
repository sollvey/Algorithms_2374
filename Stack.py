from DynamicArray import DynamicArray


class Stack: 

    def __init__(self):
        self.stack = DynamicArray()
        
    def size(self):
        return self.stack.size()

    def push(self, data):
        self.stack.add(data)
        #return f"Your stack {self.stack}"
        
    def pop(self):
        if self.stack.size() == 0:
            return "It's an empty stack"
        else:
            return self.stack.remove(self.size() - 1)
        
    def peek(self):
        if self.stack:
            return self.stack.get(self.size() - 1)
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
    st.peek()
    print("Stack contains: ", st.__dict__)
    print("GETTING SIZE")
    print(st.size())
    print("POPPING 4 elements")
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print("Stack contains: ", st.__dict__)