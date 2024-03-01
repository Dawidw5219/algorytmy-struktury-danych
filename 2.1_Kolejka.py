class KolejkaTablicowa:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.first = 0
        self.last = -1
        self.size = 0
        self.capacity = capacity

    def initQueue(self):
        self.__init__(self.capacity)

    def enQueue(self, x):
        if self.size == self.capacity:
            print("Kolejka jest pełna, nie można dodać elementu.")
            return False
        self.last = (self.last + 1) % self.capacity
        self.queue[self.last] = x
        self.size += 1
        return True

    def deQueue(self):
        if self.size == 0:
            print("Kolejka jest pusta, nie można usunąć elementu.")
            return None
        removed_element = self.queue[self.first]
        self.queue[self.first] = None
        self.first = (self.first + 1) % self.capacity
        self.size -= 1
        return removed_element

    def empty(self):
        return self.size == 0

    def front(self):
        if self.size == 0:
            print("Kolejka jest pusta.")
            return None
        return self.queue[self.first]

kolejka = KolejkaTablicowa(5)

kolejka.enQueue(1.5)
kolejka.enQueue(2.3)
kolejka.enQueue(3.7)

print(f"Usunięty element: {kolejka.deQueue()}")
print("Czy kolejka jest pusta?", "Tak" if kolejka.empty() else "Nie")
print(f"Pierwszy element w kolejce: {kolejka.front()}")

kolejka.enQueue(4.4)
kolejka.enQueue(5.5)

added = kolejka.enQueue(6.6)
if not added:
    print("Nie udało się dodać elementu, kolejka jest pełna.")

print("Stan kolejki:", kolejka.queue)