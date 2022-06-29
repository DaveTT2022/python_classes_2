import json

class User:            

    def __init__(self, user, password, age, email, phone):
        self.user = user
        self.password = password
        self.age = age
        self.email = email
        self.phone = phone
        self.add_data()


    def to_json(self):
        data = {
            "user" : self.user,
            "password" : self.password,
            "age" : self.age,
            "email" : self.email,
            "phone" : self.phone
        }
        return {self.user : data}
    
    def add_data(self):
        overal_json.update(self.to_json())
        with open("data.json", "w") as file:
            json.dump(overal_json, file, indent = 4)

    @staticmethod
    def get_data() -> dict:
        with open("data.json") as file:
            text = json.loads(file.read())
            return text

overal_json = dict()

class PyRequest:
    def __init__(
            self, 
            headers = [], 
            body = {}, 
            authorization = None, 
            User = None
            ):
        self.User = User

    def local_login(self, username, password):
        self.data = User.get_data()
        try:
            if self.data[username]["password"] == password:
                self.user = username
            else:
                self.user = None
        except:
            print("No such user in directory")
            self.user = None
    
    def login_check(func: callable) -> callable:
        def decor(*args, **kwargs):
            if args[0].user is None:
                return "You didn't login"
            return func(*args, **kwargs)
        return decor
    
    @login_check
    def get_user_info(self, request):
        self.data = User.get_data()
        obj = self.data.get(self.user)
        return obj.get(request)


obj = PyRequest()
obj.local_login(input("Send your login: "), input("Send your password: "))
print(obj.get_user_info(input("What information you need? \n")))