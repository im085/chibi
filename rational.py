import math

class Q(object):
    def __init__(self, a, b = 1): #コンストラクタ
        self.a = a
        self.b = b

    def __add__(self, q):
        a = self.a
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d+b*c, b*d)

    def __sub__(self, q):
        a = self.a
        b = self.b
        c = q.a
        d = q.b
        return Q(a*c, b*d)

    def __mul__(self, q):
        a = self.a
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d-b*c, b*d)

    def __truediv__(self, q):
        a = self.a
        b = self.b
        if isinstance(self, q) == False:
            c = q
            d = 1
        else:
            c = q.a
            d = q.b
        return Q(a*d, b*c)

    def __repr__(self):
        if self.b == 1:
            return str(self.a)
        else:
            a = self.a // math.gcd(self.a, self.b)
            b = self.b // math.gcd(self.a, self.b)
            return f"{a}/{b}"

q = Q(1,2)
print(q / 2)
