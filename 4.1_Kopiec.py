class Kopiec:
    def __init__(self, comparator=lambda x, y: x > y):
        self.heap = []
        self.comparator = comparator

    def getParentIndex(self, i):
        return (i - 1) // 2

    def getLeftChildIndex(self, i):
        return 2 * i + 1

    def getRightChildIndex(self, i):
        return 2 * i + 2

    def hasParent(self, i):
        return self.getParentIndex(i) >= 0

    def hasLeftChild(self, i):
        return self.getLeftChildIndex(i) < len(self.heap)

    def hasRightChild(self, i):
        return self.getRightChildIndex(i) < len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapifyUp(self, index):
        while self.hasParent(index) and self.comparator(self.heap[index], self.heap[self.getParentIndex(index)]):
            self.swap(index, self.getParentIndex(index))
            index = self.getParentIndex(index)

    def heapifyDown(self, index):
        while self.hasLeftChild(index):
            largerChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.comparator(self.heap[self.getRightChildIndex(index)], self.heap[largerChildIndex]):
                largerChildIndex = self.getRightChildIndex(index)

            if self.comparator(self.heap[largerChildIndex], self.heap[index]):
                self.swap(index, largerChildIndex)
                index = largerChildIndex
            else:
                break

    def insert(self, key):
        self.heap.append(key)
        self.heapifyUp(len(self.heap) - 1)

    def remove(self):
        if not self.heap:
            return "Kopiec jest pusty"
        if len(self.heap) == 1:
            return self.heap.pop()
        self.swap(0, len(self.heap) - 1)
        item = self.heap.pop()
        self.heapifyDown(0)
        return item

    def peek(self):
        if not self.heap:
            return "Kopiec jest pusty"
        return self.heap[0]

    def change(self, index, value):
        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of bounds")
        oldValue = self.heap[index]
        self.heap[index] = value
        if self.comparator(value, oldValue):
            self.heapifyUp(index)
        else:
            self.heapifyDown(index)


    def insert(self, key):
        self.heap.append(key)
        self.heapifyUp(len(self.heap) - 1)

    def remove(self):
        if not self.heap:
            return "Kopiec jest pusty"
        if len(self.heap) == 1:
            return self.heap.pop()
        self.swap(0, len(self.heap) - 1)
        item = self.heap.pop()
        self.heapifyDown(0)
        return item

    def peek(self):
        if not self.heap:
            return "Kopiec jest pusty"
        return self.heap[0]

    def change(self, index, value):
        if index < 0 or index >= len(self.heap):
            raise IndexError("Indeks poza zakresem")
        old_value = self.heap[index]
        self.heap[index] = value
        if self.comparator(value, old_value):
            self.heapifyUp(index)
        else:
            self.heapifyDown(index)

kopiec = Kopiec()
kopiec.insert(10)
kopiec.insert(15)
kopiec.insert(20)
kopiec.insert(17)

print("Kopiec przed zminą")
print(kopiec.heap)
kopiec.change(2, 22)

print("Kopiec po zmianie")
print(kopiec.heap)
