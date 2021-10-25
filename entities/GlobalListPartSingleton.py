from copy import copy
from repository.load_data import LoadData


class GlobalListPartSingleton:

    class __GlobalListPart:
        """
        Private class
        """

        def __init__(self):
            self.globalList = []

        def __str__(self):
            return "Global List =" + self.globalList

    instante = None

    def __new__(cls):
        """
        Create object
        """
        if not GlobalListPartSingleton.instante:
            GlobalListPartSingleton.instante = GlobalListPartSingleton.__GlobalListPart()
        return GlobalListPartSingleton.instante

    def __getattr__(self, global_list):
        return getattr(self.instante, global_list)

    def __setattr__(self, global_list, value):
        return setattr(self.instante, global_list, value)






    """
    def __init__(self, path = None):
        self.load_data = LoadData()
        self._globalList = self.load_data.load_data_json(path)

    def update_list(self, list_parts):
        self._globalList = list.copy(list_parts)

    # getter method
    def get_global_list(self):
        self._globalList

    # setter method
    def set_global_list(self, x):
        self._globalList = x
    """