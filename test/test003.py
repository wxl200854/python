class Foo():
    @staticmethod
    def tmp(x, y, z):
        print(x, y, z)

print(type(Foo.tmp))
Foo.tmp(1, 2, 3)

f1 = Foo()
f1.tmp(3, 3, 3)