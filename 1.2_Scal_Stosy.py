class StosTablicowy:
    def __init__(self, capacity):
        self.table = [None] * capacity
        self.topElem = -1

    def push(self, x):
        if self.topElem + 1 == len(self.table):
            raise OverflowError("Stos jest pełny")
        self.topElem += 1
        self.table[self.topElem] = x

    def pop(self):
        if self.empty():
            raise IndexError("Próba zdjęcia elementu z pustego stosu")
        element = self.table[self.topElem]
        self.topElem -= 1
        return element

    def top(self):
        if self.empty():
            raise IndexError("Próba odczytu wierzchołka z pustego stosu")
        return self.table[self.topElem]

    def empty(self):
        return self.topElem == -1

def scal_stosy(stosA, stosB):
    stosC = StosTablicowy(7)
    while not stosA.empty() and not stosB.empty():
        if stosA.top() < stosB.top():
            stosC.push(stosA.pop())
        else:
            stosC.push(stosB.pop())
    while not stosA.empty():
        stosC.push(stosA.pop())
    while not stosB.empty():
        stosC.push(stosB.pop())
    return stosC

stosA = StosTablicowy(4)
stosA.push(4)
stosA.push(3)
stosA.push(2)
stosA.push(1)

stosB = StosTablicowy(3)
stosB.push(7)
stosB.push(6)
stosB.push(5)

stosC = scal_stosy(stosA, stosB)
print("StosC po scaleniu:")
while not stosC.empty():
    print(stosC.pop())