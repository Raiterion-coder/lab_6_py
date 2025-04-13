class A:
    def __str__(self):
        return 'A._str_method'

    def hello(self):
        print('Hello')


class B:
    def __str__(self):
        return 'B._str_method'

    def good_evening(self):
        print('Good evening')


class C(A, B):
    pass


class D(B, A):
    pass


print("Пример 1")
c = C()
c.hello()
c.good_evening()

d = D()
d.hello()
d.good_evening()

print(c)
print(d)

print("Пример 2")


def new_method(arg):
    return "new method"


def new_method2(arg):
    return "new method 2"


A.__str__ = new_method
B.__str__ = new_method2

c = C()
c.hello()
c.good_evening()

d = D()
d.hello()
d.good_evening()

print(isinstance(c, A), isinstance(c, B))
print(isinstance(d, A), isinstance(d, B))
print(c)
print(d)
