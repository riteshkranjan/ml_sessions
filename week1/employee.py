
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __lt__(self, o):
        if self.id == o.id:
            return 0
        if self.id > o.id:
            return +1
        return -1


    def print_employee(self):
        print("id = {} and name = {}".format(self.id,self.name))

class Manager(Employee):

    def print_manager(self):
        print("i am manager")
    
    
