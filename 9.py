class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)


print("Пример 1")
triangle = Triangle(3, 4, 5)
print(triangle.perimeter())
eq_triangle = EquilateralTriangle(5)
print(eq_triangle.perimeter())
