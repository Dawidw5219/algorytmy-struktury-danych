import math

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class DoubleHashTable:
    def __init__(self, M):
        self.M = M
        self.size = 0
        self.array = [None] * M

    def hash(self, key):
        a = (math.sqrt(5) - 1) / 2
        frac = math.floor(math.modf(a * hash(key))[0])
        return int(self.M * frac)

    def insert(self, key, value):
        index = self.hash(key)
        while self.array[index] is not None and self.array[index].key != key and self.array[index].key != -1:
            index += 1
            index = index % self.M
        if self.array[index] is None or self.array[index].key == -1:
            self.size += 1
        self.array[index] = Node(key, value)

    def search(self, key):
        index = self.hash(key)
        while self.array[index] is not None:
            if self.array[index].key == key:
                return self.array[index].value
            index += 1
            index = index % self.M
        return None

    def delete(self, key):
        index = self.hash(key)
        while self.array[index] is not None:
            if self.array[index].key == key:
                self.array[index].key = -1
                self.array[index].value = None
                self.size -= 1
                return
            index += 1
            index = index % self.M

    def __str__(self):
        elements = []
        for i in range(self.M):
            if self.array[i] is not None and self.array[i].key != -1:
                elements.append((self.array[i].key, self.array[i].value))
        return str(elements)


hash_table = DoubleHashTable(8)
hash_table.insert(10, "jablko")
hash_table.insert(22, "banan")
hash_table.insert(34, "tata")
hash_table.insert(46, "ciastko")
hash_table.insert(58, "piwo")

print("Zawartość tablicy haszującej:")
print(hash_table)

key_to_find = 34
print(f"\nWyszukiwanie dla klucza {key_to_find}:")
if hash_table.search(key_to_find):
    print(f"Znaleziono wartość dla klucza {key_to_find}: {hash_table.search(key_to_find)}")
else:
    print(f"Nie znaleziono wartości dla klucza {key_to_find}")

klucz_do_usuniecia = 22
print(f"\nUsuwanie klucza {klucz_do_usuniecia}:")
hash_table.delete(klucz_do_usuniecia)
print("Aktualna zawartość tablicy po usunięciu:")
print(hash_table)