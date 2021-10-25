
class Panel:

    list_parts = []

    def __str__(self):
        return "Nombre :" +str(self.nombre)+ " Id :" +str(self.id)

    def __init__(self, nombre="Panel", id=0):
        self.nombre = nombre
        self.id = id

    def add_list_parts(self,list_parts):
        self.list_parts = list_parts