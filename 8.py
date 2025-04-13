class Queue:
    def __init__(self, *args):
        self.items = list(args)

    def append(self, *values):
        self.items.extend(values)

    def copy(self):
        return Queue(*self.items)

    def pop(self):
        return self.items.pop(0) if self.items else None

    def extend(self, queue):
        self.items.extend(queue.items)

    def next(self):
        return Queue(*self.items[1:]) if len(self.items) > 1 else Queue()

    def __add__(self, other):
        return Queue(*(self.items + other.items))

    def __iadd__(self, other):
        self.items.extend(other.items)
        return self

    def __eq__(self, other):
        return self.items == other.items

    def __rshift__(self, n):
        return Queue(*self.items[n:]) if n < len(self.items) else Queue()

    def __str__(self):
        return f"[{' -> '.join(map(str, self.items))}]" if self.items else "[]"

    def __next__(self):
        return self.next()


print("Пример 1")

q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)

qx = q1.copy()
print(qx.pop())
print(qx)

q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))

q3 = q2.next()
print(q1, q2, q3, sep='\n')

print(q1 + q3)

q3.extend(Queue(1, 2))
print(q3)

q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)

q5 = next(q4)
print(q4)
print(q5)
