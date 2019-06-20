import sys
import math


class Heap:
    def __init__(self, length):
        self.heap = [math.inf] * length
        self.length = 0

    def get_min_children(self, index):
        if self.heap[index*2 + 1] <= self.heap[index*2 + 2]:
            return [self.heap[index*2 + 1], index*2 + 1]
        else:
            return [self.heap[index*2 + 2], index*2 + 2]

    def get_parent(self, index):
        if index <= 2:
            return 0
        return (index-1) // 2

    def insert(self, value):
        self.heap[self.length] = value

        current = self.length
        parent = self.get_parent(current)

        while self.heap[current] < self.heap[parent]:
            self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
            current = parent
            parent = self.get_parent(parent)

        self.length += 1

    def pop(self):
        if self.heap[0] is math.inf:
            return print(0)

        print(self.heap[0])

        if self.length == 0:
            self.heap[0] = math.inf
        else:
            self.heap[0] = self.heap[self.length-1]
            self.heap[self.length - 1] = math.inf
            swap_index = 0
            min_child = self.get_min_children(swap_index)

            while min_child[0] < self.heap[swap_index]:
                self.heap[swap_index], self.heap[min_child[1]] = self.heap[min_child[1]], self.heap[swap_index]
                swap_index = min_child[1]
                min_child = self.get_min_children(swap_index)

        self.length -= 1


def main():
    h = Heap(100002)

    for value in sys.stdin.readlines()[1:]:
        value = int(value.rstrip('\n'))

        if value == 0:
            try:
                h.pop()
            except IndexError:
                pass
        else:
            h.insert(value)


if __name__ == '__main__':
    main()
