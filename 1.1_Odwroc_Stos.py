class StosListowy:
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.insert(0, x)

    def pop(self):
        if self.empty():
            raise IndexError("Próba zdjęcia elementu z pustego stosu")
        return self.s.pop(0)

    def top(self):
        if self.empty():
            raise IndexError("Próba odczytu wierzchołka z pustego stosu")
        return self.s[0]

    def empty(self):
        return len(self.s) == 0

def odwroc_stos(stos):
    pomocniczy_stos = StosListowy()
    while not stos.empty():
        pomocniczy_stos.push(stos.pop())
    return pomocniczy_stos

stos = StosListowy()
stos.push(1)
stos.push(2)
stos.push(3)
stos.push(4)
print("Stos przed odwróceniem:")
while not stos.empty():
    print(stos.top())
    stos.pop()

stos.push(1)
stos.push(2)
stos.push(3)
stos.push(4)
stos = odwroc_stos(stos)
print("Stos po odwróceniu:")
while not stos.empty():
    print(stos.top())
    stos.pop()