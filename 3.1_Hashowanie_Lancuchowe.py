class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class HashTable:
    def __init__(self, M):
        self.M = M
        self.array = [None] * M

    def hash(self, key):
        return key % self.M

    def insert(self, key):
        index = self.hash(key)
        new_node = Node(key)
        if self.array[index] is None:
            self.array[index] = new_node
        else:
            new_node.next = self.array[index]
            self.array[index] = new_node

    def __str__(self):
        elements = []
        for i in range(self.M):
            curr = self.array[i]
            while curr:
                elements.append(curr.key)
                curr = curr.next
        return str(elements)


hash_table = HashTable(5)
hash_table.insert(1)
hash_table.insert(6)
hash_table.insert(11)
print(hash_table)