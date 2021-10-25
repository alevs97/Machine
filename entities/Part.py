"""
Entity of the part to cut in the machine
"""


class Part:
    """
    Entity of the piece. This piece will be extrated from the
    JSON file come from RoboFramer.
    """

    def __str__(self):
        return f'index: {self.index} name: {self.name}, woodType: {self.woodType}' \
               f' height: {self.height}, processed: {self.processed}, skip: {self.skip}, flag: {self.flag}'

    def __init__(self, name, woodType, height, printSections, processed, skip, index , flag):
        """
        Description:
        Constructor of the Part to be process, this part will be inicialize in by the JSON come from RoboFrame

        Args:
            name: Name of the piece
            woodType: Type of the piece
            height: Height of the piece
            printSections: PrintSections into the wood.
            processed: If the piecehave been preceded by the machine
            skip: If the user wants to avoid it (TESTING)
            index: number of the index (TESTING)
            flag: (TESTING)
        """
        self.name = name
        self.woodType = woodType
        self.height = height
        self.printSections = printSections
        self.processed = processed
        self.skip = skip
        self.index = index
        self.flag = flag

    def to_Dict(self):
        """
        Description:
        Method to express this entity in form of a Dictionary

        Returns:
        Dictionary -- return the atributes
        """
        return {
            'Name': self.name,
            'WoodType': self.woodType,
            'Height': self.height,
            'PrintSections': self.printSections,
            'Processed': self.processed,
            "Skip": self.skip,
            "Index": self.index,
            "Flag": self.flag
        }

    # getter method
    def get_index(self):
        return self.index

    # setter method
    def set_index(self, x):
        self.index = x

    # getter method
    def get_skip(self):
        return self.skip

    # setter method
    def set_skip(self, x):
        self.skip = x

    # getter method
    def get_name(self):
        return self.name

    # setter method
    def set_name(self, x):
        self.name = x