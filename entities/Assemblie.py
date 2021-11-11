
class Assemblie:
    list_parts = []

    def __str__(self):
        return "Nombre: "+ str(self.name) + ", id: " +str(self.id) + "processed: " +str(self.processed)

    def __init__(self, name, id=0, processed=False):
        self.name = name
        self.id = id
        self.processed = processed

    def to_dict(self):
        return {
            "Name": self.name,
            "Processed": self.processed,
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

    # getter method
    def get_processed(self):
        return self.processed

    # setter method
    def set_processed(self, x):
        self.processed = x


