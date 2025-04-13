class Summator:

    def sum(self, N):
        return sum(self.transform(n) for n in range(1, N + 1))


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3


class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b


# Примеры
square_summator = SquareSummator()
print(square_summator.sum(10))

cube_summator = CubeSummator()
print(cube_summator.sum(10))

power_summator = PowerSummator(4)
print(power_summator.sum(10))
