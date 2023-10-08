class DynamicArray:

    def __init__(self):
        self.array = [0]
        self.length = 0
        self.asize = 1

    def increase_size(self):
        new_array = [0] * (2 * self.asize)
        i = 0
        while i < self.asize:
            new_array[i] = self.array[i]
            i += 1
        self.array = new_array
        self.asize *= 2

    def set(self, value, index):
        if 0 <= index <= (self.length - 1):
            self.array[index] = value
        else:
            return "Index out of array"

    def add(self, value):
        if self.length == self.asize:
            self.increase_size()

        self.array[self.length] = value
        self.length += 1

    def remove(self, index):
        if self.length > 0:
            if 0 <= index <= (self.length - 1):
                i = index
                removed = self.array[index]
                while i < (self.length - 1):
                    self.array[i] = self.array[i + 1]
                    i += 1
                self.array[self.length - 1] = 0
                self.length -= 1
                return removed
            else:
                return "Index out of array"
        else:
            return "Array is empty"

    def size(self):
        return self.length

    def get(self, index):
        if 0 <= index <= (self.length - 1):
            return self.array[index]
        else:
            return "Index out of array"