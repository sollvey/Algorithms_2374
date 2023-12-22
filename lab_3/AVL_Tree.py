from Stack import Stack
from DynamicArray import DynamicArray


class AVLTree:

    def __init__(self, val=0, left=None, right=None, height=0):
        self.val = val
        self.left = left
        self.right = right
        self.height = height

    def get_height(self, node):
        if node:
            return node.height
        else:
            return 0

    def balance(self, node):
        if node:
            return abs(self.get_height(node.left) - self.get_height(node.right))
        else:
            return 0

    def left_rotate(self, node):
        curr = node.right
        prev = curr.left
        curr.left = node 
        node.right = prev
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        curr.height = 1 + max(self.get_height(curr.left), self.get_height(curr.right)) 
        return curr

    def right_rotate(self, node):
        curr = node.left
        prev = curr.right
        curr.right = node
        node.left = prev
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        curr.height = 1 + max(self.get_height(curr.left), self.get_height(curr.right)) 
        return curr

    def left_right_rotate(self, node):
        node.left = self.left_rotate(node.left)
        return self.right_rotate(node)

    def right_left_rotate(self, node):
        node.right = self.right_rotate(node.right)
        return self.left_rotate(node)

    def insert(self, key, node):
        if node is None:
            return AVLTree(val=key)
        elif key < node.val:
            node.left = self.insert(key, node.left)
            if self.balance(node) == 2:
                if key < node.left.val:
                    node = self.left_rotate(node)
                else:
                    node = self.left_right_rotate(node)
        elif key >= node.val:
            node.right = self.insert(key, node.right)
            if self.balance(node) == 2:
                if key < node.right.val:
                    node = self.right_rotate(node)
                else:
                    node = self.right_left_rotate(node)
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return node

    def remove(self, key, node):
        if node is None:
            print("Error")
            return
        elif key < node.val:
            node.left = self.remove(key, node.left)
            if self.balance(node) == 2:
                if self.get_height(node.right.right) >= self.get_height(node.right.left):
                    node = self.right_rotate(node)
                else:
                    node = self.right_left_rotate(node)
            node.height =  1 + max(self.get_height(node.left), self.get_height(node.right))
        elif key >= node.val:
            node.right = self.remove(key, node.right)
            if self.balance(node) == 2:
                if self.get_height(node.left.left) >= self.get_height(node.left.right):
                    node = self.left_rotate(node)
                else:
                    node = self.left_right_rotate(node)
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return node

    def search(self, node, key):
        if node is None or node.val == key:
            return node
        if node.val < key:
            return self.search(node.right, key)
        else:
            return self.search(node.left, key)

    def width_travers(self, node):
        steps = DynamicArray()
        if node is None:
            return 
        steps.add(node)
        print("[ ", end="")
        while len(steps) > 0:
            print(steps[0].val, end=" ")
            curr = steps.remove(0)
            if curr.left:
                steps.add(curr.left)
            if curr.right:
                steps.add(curr.right)
        print("]")

    # Итеративный способ во всех трёх обходах
    def pre_order_travers(self, node):
        ans = DynamicArray()
        stack = Stack()
        curr = node
        while curr or stack.size():
            if curr:
                ans.add(curr.val)
                if curr.right:
                    stack.push(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return ans   

    def in_order_travers(self, node):
        ans = DynamicArray()
        stack = Stack()
        curr = node
        while curr or stack.size():
            if curr:
                stack.push(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                ans.add(curr.val)
                curr = curr.right
        return ans 
    
    def post_order_travers(self, node):
        ans = DynamicArray()
        stack = Stack()
        curr = node
        while curr or stack.size():
            if curr:
                ans.add(curr.val)
                if curr.left:
                    stack.push(curr.left)
                curr = curr.right
            else:
                curr = stack.pop()
        return ans.array[:len(ans)][::-1]

    def binary2avl(self, binary_tree):
        def form_avl(nodes):
            if nodes:
                middle = len(nodes) // 2
                next_root = AVLTree(nodes[middle])
                next_root.left = form_avl(nodes[:middle])
                next_root.right = form_avl(nodes[middle+1:])
                return next_root
        return form_avl(sorted(filter(None, self.in_order_travers(binary_tree))))