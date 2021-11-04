
class Panel:

    list_assemblies= []

    def __str__(self):
        return "Nombre :" +str(self.name)+ " Id :" +str(self.id)

    def __init__(self, name="Panel", id=0):
        self.name = name
        self.id = id

    def to_dict(self):
        return {
            "Id": self.id,
            "Name": self.name,
            "Assemblies": [assemble.to_dict() for assemble in self.list_assemblies]
        }

    def add_list_assemblies(self,list_assemblies):
        self.list_assemblies = list_assemblies

    def print_assemblies(self):
        for i in self.list_assemblies:
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