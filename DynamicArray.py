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

    def __getitem__(self, key):
        if isinstance(key, slice):
            new_da = DynamicArray()
            [new_da.add(num) for num in self.array[key]]
            return new_da
        else:
            return self.array[key]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __len__(self):
        return self.size()

    def __iter__(self):
        return iter(self.array[:self.size()])


if __name__ == "__main__":
    print("Init DYNAMIC ARRAY")
    da = DynamicArray()
    print("Array contains: ", da.__dict__)
    print("ADDING '1' and '2'")
    da.add(1)
    da.add(2)
    print("Array contains: ", da.__dict__)
    print("SETTING '3' INSTEAD OF '2'")
    da.set(3, 3)
    da.set(3, 1)
    print("Array contains: ", da.__dict__)
    print("GETTING ALL elements")
    print(da.get(0))
    print(da.get(1))
    print(da.get(2))
    print("GETTING SIZE")
    print(da.size())
    print("REMOVING elements with indexes 1 and 2")
    print(da.remove(1))
    print(da.remove(2))
    print("Array contains: ", da.__dict__)