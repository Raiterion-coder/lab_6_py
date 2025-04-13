class Polynomial:
    def __init__(self, coefficients):
        self.coeffs = coefficients

    def __call__(self, x):
        itog = 0
        for power, coeff in enumerate(self.coeffs):
            itog += coeff * (x ** power)
        return itog

    def __add__(self, other):
        max_len = max(len(self.coeffs), len(other.coeffs))
        new_coeffs = []
        for i in range(max_len):
            coeff1 = self.coeffs[i] if i < len(self.coeffs) else 0
            coeff2 = other.coeffs[i] if i < len(other.coeffs) else 0
            new_coeffs.append(coeff1 + coeff2)
        return Polynomial(new_coeffs)


print("Пример 1")
poly = Polynomial([10, -1])
print(poly(0))
print(poly(1))
print(poly(2))

print("Пример 2")
poly1 = Polynomial([0, 0, 1])
print(poly1(-2))
print(poly1(-1))
print(poly1(0))
print(poly1(1))
print(poly1(2))
print()

poly2 = Polynomial([0, 0, 2])
print(poly2(-2))
print(poly2(-1))
print(poly2(0))
print(poly2(1))
print(poly2(2))
print()

poly3 = poly1 + poly2
print(poly3(-2))
print(poly3(-1))
print(poly3(0))
print(poly3(1))
print(poly3(2))
print()

print("Пример 3")
poly1 = Polynomial([0, 1])
poly2 = Polynomial([10])
poly3 = poly1 + poly2
poly4 = poly2 + poly1

print(poly3(-2), poly4(-2))
print(poly3(-1), poly4(-1))
print(poly3(0), poly4(0))
print(poly3(1), poly4(1))
print(poly3(2), poly4(2))
