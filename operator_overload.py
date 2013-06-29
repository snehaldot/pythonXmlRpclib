class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + self.b, other.b + other.b)


V1 = Vector(2,10)
V2 = Vector(3,5)
V3 = V1 + V2
print V3
