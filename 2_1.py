# #1

# import random

# class dictMaker:
#     def __init__(self, string : str):
#         self.dict_ = {}
#         for x in string:
#             self.dict_[x] = random.randint(0,5)

#     def no_copies(self):
#         value = tuple(self.dict_.values())
#         key = tuple(self.dict_.keys())

#         for nums in range(1,len(key)):

#             if self.dict_[key[nums]] in value[:nums]:
#                 self.dict_.pop(key[nums])
    
#     def high_values(self):
#         list_values = list(self.dict_.values())
#         max_values = sorted(list_values)[-3:]
#         return max_values

# text = input("Send your string: ")

# obj = dictMaker(text)
# print(obj.dict_)
# obj.no_copies()
# print(obj.dict_)
# print(obj.high_values())

# #2

# import math

# class circle:
#     def __init__(self, radius : int):
#         self.radius = radius

#     def perimeter(self):
#         return 2 * self.radius * math.pi

#     def area(self):
#         return math.pi * (self.radius ** 2)

# num = int(input("Send radius: "))
# obj = circle(num)
# print(f"Perimeter: {round(obj.perimeter(), 2)}")
# print(f"Area: {round(obj.area(), 2)}")