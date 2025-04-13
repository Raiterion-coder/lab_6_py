class SparseArray:
    def __init__(self):
        self._data = {}  # Словарь для хранения ненулевых значений

    def __setitem__(self, index, value):
        if value != 0:
            self._data[index] = value
        elif index in self._data:
            del self._data[index]

    def __getitem__(self, index):
        return self._data.get(index, 0)

    def __str__(self):
        return str(self._data)


print("Пример 1")
arr = SparseArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print(f'arr({i}) = {arr[i]}')

print("Пример 2")
arr = SparseArray()
arr[10] = 123
for i in range(8, 13):
    print(f'arr({i}) = {arr[i]}')

print("Пример 3")


def print_elem(array, ind):
    print('arr[{}] = {}'.format(ind, array[ind]))


arr = SparseArray()
index = 100000000
arr[index] = 123

print_elem(arr, index - 1)
print_elem(arr, index)
print_elem(arr, index + 1)
