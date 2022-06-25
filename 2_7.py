import json
import requests
import threading

class RequestImage:

    @staticmethod
    def validate_request(url_):
        while True:
            try:
                request = requests.get(url_)
            except ConnectionError:
                print("connection error, trying again")
                continue
            break
        if request.status_code == 404:
            return None
        
        return request 
    
    @staticmethod
    def send_image(url_):
        req = RequestImage.validate_request(url_)
        return None if not req else req.content

class MakeImage:
    def __init__(self, dir):
        self.dir = dir
        self.data = self.read_file()

    def read_file(self):
        data = ""
        with open(self.dir) as json_file:
            data = json.load(json_file)
        return data

    def create_imgs(self):
        self.read_file()
        for elems in self.data:
            self.create_img(elems["img_name"], elems["img_url"])
            

    def create_img(self, name, content):
        with open(name, 'wb') as image:
                image.write(RequestImage.send_image(content))

    def thread_create(self):
        self.read_file()
        thread_list = []
        for elems in self.data:
            thd = threading.Thread(target=self.create_img, args=(elems["img_name"], elems["img_url"]))
            thd.start()
            thread_list.append(thd)

        for thread in thread_list:
            thread.join()
        
make_image = MakeImage("img_links.json")
make_image.thread_create()