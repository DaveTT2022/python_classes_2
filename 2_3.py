import random

class game:
    def __init__(self):
        self.number = self.rand_num()
        while self.win() == None:
            self.guess = None
            while self.guess == None:
                self.guess = self.user_response() 
                self.guess = None if self.guess is None else self.dubl_check(self.guess, True)
            self.result_ = self.check_bull_cow()
            print(self.result_)
            print(self.win())

    def rand_num(self):
        randNum = self.dubl_check(str(random.randint(1000, 9999)), False)
        if randNum == None:
            self.rand_num()
        else:
            return randNum

    def user_response(self):
        try:
            guess = input("Send your 4 digit number: ")
            int(guess)
            if len(guess) != 4:
                raise TypeError("Your input isnt 4 digit number")
        except TypeError as e:
            print(e)
            return None
        except ValueError:
            print("Your input isnt digit, please try again")
            return None
        else:
            return guess

    def dubl_check(self, number, is_guess):
        for i in range(3):
            if number[i] in number[i + 1:]:
                if is_guess:
                    print("Your number has duplicates, please try again")
                return None
        return number

    def check_bull_cow(self):
        cows, bulls = 0, 0
        for num in range(4):
            if self.guess[num] == self.number[num]:
                cows += 1
            elif self.guess[num] in self.number:
                bulls += 1
        return {"Cows" : cows, "Bulls" : bulls}

    def win(self):
        try:
            if self.result_["Cows"] == 4:
                return "Congratulations you have guessed the number"
            return None
        except:
            return None
obj = game()

#2

class Triangle:
    def __init__(self, *triangle_sides):
        self.triangle_list = sorted(triangle_sides[:3])
        self.valid_triangle()

    def valid_triangle(self):
        if not (self.triangle_list[0] + self.triangle_list[1] > self.triangle_list[2]):
            raise Exception("invalid triangle")

    def perimeter(self):
        sum_ = 0
        for x in self.triangle_list:
            sum_ += x
        return sum_
    def area(self):
        perim = self.perimeter() / 2
        area = perim
        for x in self.triangle_list:
            area *= (perim - x)
        return round(area ** 0.5, 2)

    def is_similar(self, obj_):
        ratio = []
        for num in range(3):
            ratio.append(self.triangle_list[num] / obj_.triangle_list[num])
        if sorted(ratio)[0] == sorted(ratio)[2]:
            return "Is similar"
        return "Not similar"
            

obj = Triangle(3,4,5)
obj_2 = Triangle(6,10,8)
print(obj.area())
print(obj_2.is_similar(obj))