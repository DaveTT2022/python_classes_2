class Rectangle():
    created_rects = 0

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        cls.created_rects += 1
        return self

    
    def __init__(self, *args):
        self.list_sides = sorted(args)

    def __eq__(self, other):
        self.instance_check(other)
        return True if self.list_sides == other.list_sides else False

    def __gt__(self, other):
        self.instance_check(other)
        for x in range(4):
            if not self.list_sides[x] >= other.list_sides[x]:
                return False
        return True

    def perimeter(self):
        sum_ = 0
        for x in self.list_sides:
            sum_ += x
        return sum_

    def area(self):
        return self.list_sides[0] * self.list_sides[3]

    def instance_check(self, other):
        if isinstance(other, Rectangle):
           return None
        else:
            return TypeError("Comparing with wrong type")

    def is_alike(self, other):
        ratio = []
        for num in range(4):
            ratio.append(self.list_sides[num] / other.list_sides[num])
        if sorted(ratio)[0] == sorted(ratio)[2]:
            return "Is similar"
        return "Not similar"

    def __del__(self):
        self.created_rects -= 1
            

rect_1 = Rectangle(24,12,24,12)
print(Rectangle.created_rects)
rect_2 = Rectangle(12,12,11,11)
print(Rectangle.created_rects)
print(rect_2 > rect_1)
print(rect_1.is_alike(rect_2))