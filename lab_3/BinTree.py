from Stack import Stack
from DynamicArray import DynamicArray

class BinaryTree:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    @staticmethod
    def pre_order_travers(node):
        answer = DynamicArray()
        def travers(node, answer):
            if node:
                travers(node.left, answer)
                answer.add(node.val)
                travers(node.right, answer)
        
        travers(node, answer)
        return answer

    @staticmethod
    def parsing_bracket_string(path: str = "tree.txt"):
        stack = Stack()
        curr_node = None
        with open(path, encoding="utf-8") as file:
            for sym in file.read():
                if sym != " ":
                    if sym == '(':
                        parent = stack.peek()
                        next_node = BinaryTree(val=None)
                        stack.push(next_node)
                        if isinstance(parent, BinaryTree):
                            if parent.left:
                                parent.right = next_node
                            else:
                                parent.left = next_node
                    elif sym == ')':
                        curr_node = stack.pop()
                    elif sym.isdigit():
                        if not stack.size():
                            print(f"error: stack empty")
                            return
                        stack.peek().val = int(sym)
                    else:
                        print(f"error: incorrect symbol {sym}")
                        return
            return curr_node