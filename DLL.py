class Node:
    
    def __init__(self, data, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next


class DoublyLinkedList:
    
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    def insert_item(self, index, data):
        new_node = Node(data)
        if self.length == 0 or index == 0:
            self.prepend(data)
        elif index < 0 or index > (self.length - 1):
            print("Index doesn't exist")
        elif (self.length - 1) == index:
            self.append(data)
        else:
            current = self.head
            count = 0
            while count < index:
                current = current.next
                count += 1
            new_node.previous = current
            new_node.next = current.next
            if current.next is not None:
                current.next.previous = new_node
            current.next = new_node
            self.length += 1

    def append(self, data):
        new_node = Node(data)
        new_node.previous = self.tail
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        self.tail.next = None
        if self.length == 0:
            self.head = self.tail
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.previous = new_node
        self.head = new_node
        self.head.previous = None
        if self.length == 0:
            self.tail = self.head
        self.length += 1

    def size(self):
        return self.length
    
    def get(self, index):
        if index > (self.length - 1) or index < 0:
            print("Index out of linked list")
        elif index <= self.length // 2:
            current = self.head
            count = 0
            while count < index:
                current = current.next
                count += 1
            return current.data
        else:
            current = self.tail
            count = self.length - 1
            while count > index:
                current = current.previous
                count -= 1        
            return current.data
    
    def remove(self, index):
        if index > (self.length - 1) or index < 0:
            print("Index out of linked list")
        elif index == 0:
            current = self.head
            if self.length == 1:
                self.head = self.tail = None
                self.length = 0
            else:
                self.head = self.head.next
                self.head.previous = None
                self.length -= 1
            return f'{current.data} was removed'
        elif index == (self.length - 1):
            current = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
            self.length -= 1
            return f'{current.data} was removed'
        else:
            current = self.head
            count = 0
            while count < index:
                current = current.next
                count += 1
            current.previous.next = current.next
            current.next.previous = current.previous
            self.length -= 1
            return f'{current.data} was removed'


print("Init DLL")
dll = DoublyLinkedList()
print("List contains: ", dll.__dict__)
print("APPENDING '2'")
dll.append(2)
print("List contains: ", dll.__dict__)
print("Head contains:", dll.head.data)
print("Tail contains: ", dll.tail.data)
print("PREPENDING '1'")
dll.prepend(1)
print("List contains: ", dll.__dict__)
print("Head contains:", dll.head.data)
print("Tail contains: ", dll.tail.data)
print("INSERTING '3' and '4'")
print(dll.insert_item(-1, 3))
dll.insert_item(1, 3)
dll.insert_item(2, 4)
print("List contains: ", dll.__dict__)
print("Head contains:", dll.head.data)
print("Tail contains: ", dll.tail.data)
print("GETTING ALL elements")
print(dll.get(0))
print(dll.get(1))
print(dll.get(2))
print(dll.get(3))
print("REMOVING elements with indexes 1 and 2")
print(dll.remove(1))
print(dll.remove(2))
print("List contains: ", dll.__dict__)
print("Head contains:", dll.head.data)
print("Tail contains: ", dll.tail.data)