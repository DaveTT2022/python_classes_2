import os 

class Files:
    def __init__(self, *args):
        for i in args:
            if not i.endswith(".txt"):
                self.folder_creator(i)
            else:
                self.file_creator(i)
        self.ask_remove(self.delete_files("Dir1"))

    def folder_creator(self, path_):
        if not os.path.exists(path_):
            os.makedirs(path_)
    
    def file_creator(self, file):
        with open(file, 'w'):
            pass
    def delete_files(self, files):
        os.chdir(os.path.join(os.getcwd(), files))
        all_list = os.listdir()
        for x in all_list:
            if len(os.listdir(os.path.join(x))) != 0:
                for y in os.listdir(os.path.join(x)):
                    all_list.append(os.path.join(x, y))
        return all_list
    
    def ask_remove(self, array_list):
        for x in array_list[::-1]:
            question_ = input(f"do you want to remove {x} file? y/n \n")
            if question_ == "yes" and os.path.exists(x):
                path_ = os.getcwd()
                self.remove_big_folder(x, path_)


    def remove_big_folder(self, fold, old_path):
        path__ = os.path.join(old_path, fold)
        os.chdir(path__)
        while os.path.exists(path__):
            for elem in os.listdir():
                try:
                    os.rmdir(elem)
                    if os.getcwd() != path__:
                        os.chdir("..")
                except:
                    try:
                        os.chdir(os.path.join(os.getcwd(), elem))
                    except:
                        pass
            try:
                abc = os.getcwd()
                os.chdir("..")
                os.rmdir(path__)
            except:
                os.chdir(abc)
        os.chdir(old_path)
        

obj = Files("Dir1/dir2/dir5", "Dir1/dir3/dir6/dir9/dir10", "abcd.txt", "Dir1")