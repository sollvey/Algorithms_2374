from random import randint
from functools import reduce
from DynamicArray import DynamicArray


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array


def merge(left, right):
    consecutives = {"left": 0, "right": 0}
    n = m = 0
    answer = DynamicArray()
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            answer.add(left[n])
            n += 1
            consecutives["right"] = 0
            consecutives["left"] += 1
        else:
            answer.add(right[m])
            m += 1
            consecutives["left"] = 0
            consecutives["right"] += 1

        if consecutives["left"] == 7:
            r_index = binary_search_rightmost(left[n:len(left)], right[m:len(right)][0])
            [answer.add(num) for num in left[n:r_index+n]]
            consecutives["left"] = 0
            n += r_index
        elif consecutives["right"] == 7:
            r_index = binary_search_rightmost(right[m:len(right)], left[n:len(left)][0])
            [answer.add(num) for num in right[m:r_index+m]]
            consecutives["right"] = 0
            m += r_index

    [answer.add(num) for num in left[n:len(left)]]
    [answer.add(num) for num in right[m:len(right)]]
    return answer

            
def get_minrun(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r

    
def binary_search_rightmost(array, key):
    left, right = 0, len(array)
    while left < right:
        middle = (left + right) // 2
        if array[middle] > key:
            right = middle
        else:
            left = middle + 1
    return right


def get_runs(array, minrun):
    runs, left = DynamicArray(), 0
    while True:
        if left + minrun < len(array):
            runs.add(insertion_sort(array[left:left + minrun]))
        else:
            runs.add(insertion_sort(array[left:len(array)]))
            break
        left += minrun
    return runs


def timsort(array):
    N = len(array)
    if N < 64:
        return insertion_sort(array)
    minrun = get_minrun(N)
    runs = get_runs(array, minrun)
    return reduce(lambda left, right: merge(left, right), runs)
    

if __name__ == "__main__":
    unsorted_array = DynamicArray()
    [unsorted_array.add(randint(-100, 100)) for _ in range(randint(50, 500))]
    sorted_array = timsort(unsorted_array)
    print("\nUNSORTED ARRAY:\n")
    for num in unsorted_array:
        print(num, end=" ")
    print("\n\nSORTED ARRAY:\n")
    for num in sorted_array:
        print(num, end=" ")
    print(f"\n\n{sorted(unsorted_array.array[:unsorted_array.length]) == sorted_array.array[:sorted_array.length]}")
