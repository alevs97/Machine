from entities.GlobalListPartSingleton import GlobalListPartSingleton
import copy

class Services:

    def __init__(self):

        self.globalList = GlobalListPartSingleton()

    def start_here(self, index):

        print("Piece to start here : " + index)

        list_parts = copy.deepcopy(self.globalList.globalList)

        filter_list = list(filter(lambda x: x.get_index() >= int(index), list_parts))

        self.globalList.globalList = copy.deepcopy(filter_list)


    def skip_here(self, index):

        list_parts = copy.deepcopy(self.globalList.globalList)
        print("Piece to skip : " + index)

        map_list = list(map(lambda x: x.set_skip(True) if x.get_index() == int(index) else x, list_parts))
        filter_list = list(filter(lambda x: False if x.get_skip() else True, list_parts))

        self.globalList.globalList = copy.deepcopy(filter_list)

        #self.globalList.update_list(filter_list)
