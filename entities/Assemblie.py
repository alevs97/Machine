
class Assemblie:
    list_parts = []

    def __str__(self):
        return "Nombre: "+ str(self.nombre) +", id: " +str(self.id)

    def __init__(self, nombre, id=0):
        self.nombre = nombre
        self.id = id

    def add_list_parts(self, list_parts):
        self.list_parts = list_parts

    def print_parts(self):
        for i in self.list_parts:
            print(i)


