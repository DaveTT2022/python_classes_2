# #1
# class Person:
#     IS_HEALTHY = True
#     WALK_SPEED = 3
#     IQ = 120
#     def __init__(self, eye_color, hair_color, height):
#         self.eye = eye_color
#         self.hair = hair_color
#         self.height = height
#     def when_sees_dog():
#         Person.WALK_SPEED = 15
#         return Person.WALK_SPEED
#     def normal_walk():
#         Person.WALK_SPEED = 3
#         return Person.WALK_SPEED

#     def show_persons_info(self):
#         return f"""\tThe Persons health is good: {Person.IS_HEALTHY}
#         The IQ is: {Person.IQ}
#         Walking speed in normal conditions: {Person.normal_walk()}
#         Walking when sees dog: {Person.when_sees_dog()}"""
        

# class Student(Person):
#     TIME_AT_SCHOOL = "6h"
#     def __init__(self, eye_color, hair_color, height, has_homework):
#         self.has_hw = has_homework
#         super().__init__(eye_color = eye_color, hair_color = hair_color, height = height)
#         self.activity = "studying"
    
#     def activity_change(self):
#         if self.has_hw:
#             self.activity = "studying"
#         else:
#             self.activity = "playing"
#     def student_info(self):
#         self.activity_change()
#         return f"""\tStudent's eye color is: {self.eye}
#         Hair color: {self.hair}
#         Height: {self.height}
#         Current activity: {self.activity}"""

# human = Student("black", "brown", "175", False)
# print(human.show_persons_info())
# print(human.student_info())

# #2

# class Country:

#     def __init__(self, country_name, continent, *args, **kwargs) -> None:
#         self.country_name = country_name
#         self.continent = continent

#     def info_country(self) -> str:
#         return f"Country name is: {self.country_name} \nThe continent is: {self.continent}"

# class Season(Country):

#     def __init__(self, season_name, avg_temp, *args, **kwargs) -> None:
#         self.season_name = season_name
#         self.avg_temp = avg_temp
#         super().__init__(*args, **kwargs)

#     def info_season(self) -> str:
#         return f"Season name: {self.season_name} \nAverage temperature: {self.avg_temp}"

# class Brand(Season):

#     def __init__(self, brand_name, start_date, *args, **kwargs) -> None:
#         self.brand_name = brand_name
#         self.start_date = start_date
#         super().__init__(*args, **kwargs)

#     def info_brand(self) -> str:
#         return f"Brands name is: {self.brand_name} \nBusiness start date is: {self.start_date}"

# class Product(Brand, Season, Country):
#     def __init__(self, name, product_type, price, quantity, *args, **kwargs):
#         self.product_name = name
#         self.product_type = product_type
#         self.price = price
#         self.quantity = quantity
#         super(Product, self).__init__(*args, **kwargs)

#     def present(self):
#         return f"""\t{self.product_name} was made in {self.country_name} which is located in {self.continent}
#         During {self.season_name} with average temperatur {self.avg_temp} degree
#         Brand name is {self.brand_name} which was established in {self.start_date}
#         Product type is {self.product_type} with current price {self.price} 
#         Right now is available {self.quantity} samples of the product"""

#     def discount(self, amount : int) -> None:
#         self.price -= int(self.price * amount / 100)

#     def increase_quant(self, amount):
#         self.quantity += amount

#     def decrease_quant(self, amount):
#         self.quantity -= amount

# product_ = Product("Xndzor", "Mirg", 500, 15, brand_name = "Apple",  start_date = 2021, season_name = "Summer", avg_temp = 38, country_name = "America", continent = "North America", quality = "decent")

# print(product_.present())
# print("-" * 65)
# product_.discount(20)
# product_.increase_quant(15)
# print(product_.present())

#3

from ast import arg


class Hotel:

    def __init__(self, lux_number, mid_number, lux_price, mid_price, hotel_name, hotel_address, *args, **kwargs):
        self.hotel_name = hotel_name
        self.hotel_address = hotel_address
        self.mid_price = mid_price
        self.lux_price = lux_price
        self.lux_rooms = Hotel.rooms_maker(lux_number)
        self.mid_rooms = Hotel.rooms_maker(mid_number)

    def rooms_maker(room_number):
        return dict.fromkeys((f"room{x}" for x in range(room_number)), "Free")

    def present_hotel(self):
        return f"""{self.hotel_name}
        We are located at {self.hotel_address}
        Current state of our mid rooms {self.mid_rooms}
        Current state of our lux rooms {self.lux_price}
        Mid rooms cost {self.mid_price}, Lux rooms cost {self.lux_price}"""

    def book_room(self, room_name, is_lux):
        if self.available_room(room_name, is_lux):
            raise Exception("Room is not available")
        if is_lux:
            self.lux_rooms[room_name] = "bussy"
        else:
            self.mid_rooms[room_name] = "bussy"

    def available_room(self, room_name, is_lux):
        if is_lux:
            return self.lux_rooms[room_name] == "bussy"
        else:
            return self.mid_rooms[room_name] == "bussy"

    def discount(self, number, is_lux):
        if is_lux:
            self.lux_price -= (self.lux_price * number / 100)
        else:
            self.mid_price -= (self.mid_rooms * number / 100)

class Taxi(Hotel):
    
    def __init__(self, taxi_name, car_types, price_for_tour, *args, **kwargs):
        self.car_types = car_types
        self.taxi_name = taxi_name
        self.price_for_tour = price_for_tour
        super().__init__(*args, **kwargs)

    def present(self):
        return f"""{self.taxi_name}
        We have various type of cars such as:
        {self.car_types}
        Our price per tour is {self.price_for_tour}"""

    def discount(self, number):
        self.price_for_tour -= (self.price_for_tour * number / 100)

class Tour(Taxi, Hotel):

    def __init__(self, tour_name, *args, **kwargs):
        self.tour_name = tour_name
        super().__init__(*args, **kwargs)

        self.PRICE_LUX = self.lux_price + self.price_for_tour
        self.PRICE_MID = self.mid_price + self.price_for_tour

    def present(self):
        return f"""\tWelcome to tour '{self.tour_name}'
        Our tour costs from {self.PRICE_LUX}, till {self.lux_price} \n
        Information about our tour Taxi: {super().present()} \n
        Information about our tour Hotel: {super().present_hotel()}"""

obj = Tour("Around world", "Yandex", ["BMW", "Toyota", "Honda"], 400, lux_number = 5, mid_number = 7, lux_price = 400, mid_price = 200, hotel_name = "Nairi", hotel_address = "Myasnikyan Sreet 7/1")
print(obj.present())