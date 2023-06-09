class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = self.__b = self.__c = None
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def __check_number(cls, num):
        return cls.MIN_DIMENSION <= num <= cls.MAX_DIMENSION

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        if Dimensions.__check_number(a):
            self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        if Dimensions.__check_number(b):
            self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        if Dimensions.__check_number(c):
            self.__c = c

    def __eq__(self, other):
        if isinstance(other, Dimensions):
            return self.a == other.a and self.b == other.b and self.c == other.c
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Dimensions):
            return (
                    self.a < other.a
                    or (self.a == other.a and self.b < other.b)
                    or (self.a == other.a and self.b == other.b and self.c < other.c)
            )
        return NotImplemented

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, Dimensions):
            return (
                    self.a > other.a
                    or (self.a == other.a and self.b > other.b)
                    or (self.a == other.a and self.b == other.b and self.c > other.c)
            )
        return NotImplemented

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)