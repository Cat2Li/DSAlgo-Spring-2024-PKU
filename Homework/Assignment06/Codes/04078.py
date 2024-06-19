from typing import List


class Heap(object):

    def __init__(self):
        self.heap: List[int] = []

    def heappush(self, value: int):
        self.heap.append(value)
        self.__siftup(len(self.heap) - 1)

    def heappop(self) -> int:
        if len(self.heap) == 0:
            raise IndexError("pop from empty heap")

        if len(self.heap) == 1:
            return self.heap.pop()

        self.__swap(0, len(self.heap) - 1)
        root = self.heap.pop()
        self.__siftdown(0)

        return root

    def __swap(self, a: int, b: int):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def __siftup(self, index: int):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] <= self.heap[index]:
                break
            self.__swap(parent, index)

            index = parent

    def __siftdown(self, index: int):
        while index * 2 + 1 < len(self.heap):
            left = index * 2 + 1
            right = index * 2 + 2

            child = left
            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                child = right

            if self.heap[index] <= self.heap[child]:
                break
            self.__swap(index, child)

            index = child


n = int(input())
heap = Heap()
for _ in range(n):
    string = input()
    if string[0] == "1":
        _, value = map(int, string.split())
        heap.heappush(value)
    else:
        print(heap.heappop())
