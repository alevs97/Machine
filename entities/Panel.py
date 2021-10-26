
class Panel:

    list_assemblies= []

    def __str__(self):
        return "Nombre :" +str(self.nombre)+ " Id :" +str(self.id)

    def __init__(self, nombre="Panel", id=0):
        self.nombre = nombre
        self.id = id

    def add_list_assemblies(self,list_assemblies):
        self.list_assemblies = list_assemblies

    def print_assemblies(self):
        for i in self.list_assemblies:
            print(i)
