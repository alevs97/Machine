
class Assemblie:
    list_parts = []

    def __str__(self):
        return "Nombre: "+ str(self.name) +", id: " +str(self.id)

    def __init__(self, name, id=0):
        self.name = name
        self.id = id

    def to_dict(self):
        return {
            "Id": self.id,
            "Name": self.name,
            "Assemblies": [part.to_dict() for part in self.list_parts]
        }

    def add_list_parts(self, list_parts):
        self.list_parts = list_parts

    def print_parts(self):
        for i in self.list_parts:
            print(i)

    # getter method
    def get_id(self):
        return self.id

    # setter method
    def set_id(self, x):
        self.id = x

    # getter method
    def get_name(self):
        return self.name

    # setter method
    def set_name(self, x):
        self.name = x


