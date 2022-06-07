#1
class Person:
    IS_HEALTHY = True
    WALK_SPEED = 3
    IQ = 120
    def __init__(self, eye_color, hair_color, height):
        self.eye = eye_color
        self.hair = hair_color
        self.height = height
    def when_sees_dog():
        Person.WALK_SPEED = 15
        return Person.WALK_SPEED
    def normal_walk():
        Person.WALK_SPEED = 3
        return Person.WALK_SPEED

    def show_persons_info(self):
        return f"""\tThe Persons health is good: {Person.IS_HEALTHY}
        The IQ is: {Person.IQ}
        Walking speed in normal conditions: {Person.normal_walk()}
        Walking when sees dog: {Person.when_sees_dog()}"""
        

class Student(Person):
    TIME_AT_SCHOOL = "6h"
    def __init__(self, eye_color, hair_color, height, has_homework):
        self.has_hw = has_homework
        super().__init__(eye_color = eye_color, hair_color = hair_color, height = height)
        self.activity = "studying"
    
    def activity_change(self):
        if self.has_hw:
            self.activity = "studying"
        else:
            self.activity = "playing"
    def student_info(self):
        self.activity_change()
        return f"""\tStudent's eye color is: {self.eye}
        Hair color: {self.hair}
        Height: {self.height}
        Current activity: {self.activity}"""

human = Student("black", "brown", "175", False)
print(human.show_persons_info())
print(human.student_info())

#2

class Country:
    COUNTRY_NAME = "Armenia"
    CONTINENT = "Asia"
    def info_country(self) -> str:
        return f"Country name is: {self.COUNTRY_NAME} \nThe continent is: {self.CONTINENT}"

class Brand:
    BRAND_NAME = "Samsung"
    START_DATE = "2021"

    def info_brand(self) -> str:
        return f"Brands name is: {self.BRAND_NAME} \nBusiness start date is: {self.START_DATE}"

class Season:
    SEASON_NAME = "Summer"
    AVG_TEMP = "30"

    def info_season(self) -> str:
        return f"Season name: {self.SEASON_NAME} \nAverage temperature: {self.AVG_TEMP}"

class Product(Country, Brand, Season):
    def __init__(self, name, product_type, price, quantity):
        self.product_name = name
        self.product_type = product_type
        self.price = price
        self.quantity = quantity

    def present(self):
        return f"""\t{self.product_name} was made in {self.COUNTRY_NAME} which is located in {self.CONTINENT}
        During {self.SEASON_NAME} with average temperatur {self.AVG_TEMP} degree
        Brand name is {self.BRAND_NAME} which was established in {self.START_DATE}
        Product type is {self.product_type} with current price {self.price} 
        Right now is available {self.quantity} samples of the product"""

    def discount(self, amount : int) -> None:
        self.price -= int(self.price * amount / 100)

    def increase_quant(self, amount):
        self.quantity += amount

    def decrease_quant(self, amount):
        self.quantity -= amount

product_ = Product("Xndzor", "Mirg", 500, 15)

print(product_.present())
print("-" * 65)
product_.discount(20)
product_.increase_quant(15)
print(product_.present())


class Hotel:
    HOTEL_NAME = "Hotel Bliss"
    HOTEL_ADDRESS = "Andhra Pradesh 517501"

    ROOMS_MID = dict.fromkeys(("room1", "room2", "room3"), "Free")
    MID_ROOM_PRICE = 500

    ROOMS_LUX = dict.fromkeys(("room1", "room2", "room3"), "Free")
    LUX_ROOM_PRICE = 1000

    def present_hotel(self):
        return f"""{self.HOTEL_NAME}
        We are located at {self.HOTEL_ADDRESS}
        Curret state of our mid rooms {self.ROOMS_MID}
        Curret state of our lux rooms {self.ROOMS_LUX}
        Mid rooms cost {self.MID_ROOM_PRICE}, Lux rooms cost {self.LUX_ROOM_PRICE}"""

    def book_room(self, room_name, is_lux):
        if self.available_room(room_name, is_lux):
            raise Exception("Room is not available")
        if is_lux:
            self.ROOMS_LUX[room_name] = "bussy"
        else:
            self.ROOMS_MID[room_name] = "bussy"
    def available_room(self, room_name, is_lux):
        if is_lux:
            return self.ROOMS_LUX[room_name] == "bussy"
        else:
            return self.ROOMS_MID[room_name] == "bussy"

    def discount(self, number, is_lux):
        if is_lux:
            self.LUX_ROOM_PRICE -= (self.LUX_ROOM_PRICE * number / 100)
        else:
            self.MID_ROOM_PRICE -= (self.MID_ROOM_PRICE * number / 100)

class Taxi:
    TAXI_NAME = "Yandex"
    CAR_TYPES = ["Auris (Toyota)", "Avensis (Toyota)", "E-Class (Mercedes)", "Insignia (Vauxhall)"]
    PRICE_FOR_TOUR = 750
    
    def present(self):
        return f"""{self.TAXI_NAME}
        We have various type of cars such as:
        {self.CAR_TYPES}
        Our price per tour is {self.PRICE_FOR_TOUR}"""

    def discount(self, number):
        self.PRICE_FOR_TOUR -= (self.PRICE_FOR_TOUR * number / 100)

class Tour(Taxi, Hotel):
    TOUR_NAME = "Around World"
    PRICE_LUX = Hotel.LUX_ROOM_PRICE + Taxi.PRICE_FOR_TOUR
    PRICE_MID = Hotel.MID_ROOM_PRICE + Taxi.PRICE_FOR_TOUR

    def present(self):
        return f"""\t Welcome to tour '{self.TOUR_NAME}'
        Our tour costs from {self.PRICE_MID}, till {self.PRICE_LUX} \n
        Information about our tour Taxi: {super().present()} \n
        Information about our tour Hotel: {super().present_hotel()}"""

obj = Tour()
print(obj.present())