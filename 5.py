class ReversedList:
    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, index):
        if index < 0 or index >= len(self.lst):
            raise IndexError("Index out of range")
        return self.lst[-(index + 1)]


print("Пример 1")
rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])

print("Пример 2")
rl = ReversedList([])
print(len(rl))

print("Пример 3")
rl = ReversedList([10])
print(len(rl))
print(rl[0])
