class NumberTransformer:
    def __init__(self, numbers):
        self.numbers = numbers

    def make_negative(self):
        self.numbers = [x if x < 0 else -x for x in self.numbers]

    def square(self):
        self.numbers = [x ** 2 for x in self.numbers]

    def strange_command(self):
        self.numbers = [x + 1 if x % 5 == 0 else x for x in self.numbers]

    def apply_rules(self, rules):
        for rule in rules:
            if rule == "make_negative":
                self.make_negative()
            elif rule == "square":
                self.square()
            elif rule == "strange_command":
                self.strange_command()
        return self.numbers

print("Пример 1")
numbers1 = [1, 0, -2, 30, -4]
rules1 = ["make_negative"]
transformer1 = NumberTransformer(numbers1)
print(transformer1.apply_rules(rules1))

print("Пример 2")
numbers2 = [1, 5, -2, 0, 30, -4]
rules2 = ["square", "strange_command"]
transformer2 = NumberTransformer(numbers2)
print(transformer2.apply_rules(rules2))
print("Пример 3")
numbers3 = [1, 5, -2, 0, 30, -4]
rules3 = ["square", "strange_command", "square"]
transformer3 = NumberTransformer(numbers3)
print(transformer3.apply_rules(rules3))
