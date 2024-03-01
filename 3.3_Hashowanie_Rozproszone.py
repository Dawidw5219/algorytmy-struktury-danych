import math

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class DistributedHashTable:
    def __init__(self, M, a, b):
        self.M = M
        self.a = a
        self.b = b
        self.size = 0
        self.array = [None] * M

    def hash(self, key):
        return (int((self.a * key) % self.b) % self.M)

    def insert(self, key, value):
        index = self.hash(key)
        while self.array[index] is not None and self.array[index].key != key:
            index = (index + 1) % self.M
        if self.array[index] is None:
            self.size += 1
        self.array[index] = Node(key, value)

    def __str__(self):
        elements = []
        for i in range(self.M):
            if self.array[i] is not None:
                elements.append((self.array[i].key, self.array[i].value))
        return str(elements)



M = 10
a = 11
b = 13

hash_table = DistributedHashTable(M, a, b)

hash_table.insert(10, "mleko")
hash_table.insert(11, "maslo")
hash_table.insert(26, "banan")
hash_table.insert(20, "pomarancz")
hash_table.insert(30, "truskawka")
hash_table.insert(40, "winogrono")

print("Zawartość tablicy haszującej:")
print(hash_table)
