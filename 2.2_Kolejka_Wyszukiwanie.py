class KolejkaListowa:
    def __init__(self):
        self.first = None
        self.last = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def initQueue(self):
        self.__init__()

    def enQueue(self, x):
        newNode = self.Node(x)
        if self.last is None:
            self.first = self.last = newNode
            return
        self.last.next = newNode
        self.last = newNode

    def deQueue(self):
        if self.first is None:
            raise ValueError("Kolejka jest pusta, nie można usunąć elementu.")
        removedValue = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return removedValue

    def empty(self):
        return self.first is None

    def front(self):
        if self.first is None:
            raise ValueError("Kolejka jest pusta, nie można odczytać pierwszego elementu.")
        return self.first.data
def znajdz_element(kolejka, x):
    current = kolejka.first
    while current is not None:
        if current.data == x:
            return True
        current = current.next
    return False

kolejka = KolejkaListowa()
kolejka.initQueue()
kolejka.enQueue("A1b2")
kolejka.enQueue("B3c4")
kolejka.enQueue("C5d6")
kolejka.enQueue("D7e8")

szukana_wartosc = "B3c4"
czy_znaleziono = znajdz_element(kolejka, szukana_wartosc)
print(f"Czy znaleziono element '{szukana_wartosc}'?:", "Tak" if czy_znaleziono else "Nie")


szukana_wartosc = "B3c44444"
czy_znaleziono = znajdz_element(kolejka, szukana_wartosc)
print(f"Czy znaleziono element '{szukana_wartosc}'?:", "Tak" if czy_znaleziono else "Nie")