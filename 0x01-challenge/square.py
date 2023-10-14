#!/usr/bin/python3

class Square:
    def __init__(self, side=0):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

    def __str__(self):
        return str(self.side)

if __name__ == "__main":
    s = Square(side=12)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())
