class Kopiec:
    def __init__(self, comparator=lambda x, y: x.total_points > y.total_points):
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
            raise IndexError("Index po za granicą")
        oldValue = self.heap[index]
        self.heap[index] = value
        if self.comparator(value, oldValue):
            self.heapifyUp(index)
        else:
            self.heapifyDown(index)



class KopiecStudenta(Kopiec):
    def __init__(self):
        super().__init__(comparator=lambda x, y: x.total_points > y.total_points)

class Student:
    def __init__(self, student_id, lab_scores):
        self.student_id = student_id
        self.lab_scores = lab_scores
        self.total_points = sum(lab_scores)

class KolejkaPriorytetowa:
    def __init__(self):
        self.heap = KopiecStudenta()

    def insert(self, student):
        self.heap.insert(student)

    def remove(self):
        return self.heap.remove()

    def display(self):
        for student in self.heap.heap:
            print(f"Nr indeksu studenta: {student.student_id}, Łączna ilość punktów: {student.total_points}")


pq = KolejkaPriorytetowa()
pq.insert(Student(123456, [3, 3, 3, 3, 3, 3, 3]))
pq.insert(Student(111111, [1, 1, 1, 1, 1, 1, 1]))
pq.insert(Student(654321, [2, 2, 2, 2, 2, 2, 2]))


usuniety_student = pq.remove()
print(f"Usunięto Studenta o ID: {usuniety_student.student_id}, Łączna liczba punktów: {usuniety_student.total_points}")

print("\nStan kolejki po usunięciu:")
pq.display()
