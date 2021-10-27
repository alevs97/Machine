from entities.GlobalListPanelsSingleton import GlobalListPanelsSingleton
import copy

class Services:

    def __init__(self):

        self.list_global = GlobalListPanelsSingleton()

    def skip_here(self, id_panel, id_assemblie, id_part):
        list_parts = self.list_global.globalList[id_panel].list_assemblies[id_assemblie].list_parts
        part = self.list_global.globalList[id_panel].list_assemblies[id_assemblie].list_parts[id_part]

        print(id_panel)
        print(id_assemblie)
        print(id_part)
        filter_list = list(filter(lambda x: x.get_id() != part.get_id(), list_parts))
        for i in filter_list:
            print(i)
        self.list_global.globalList[id_panel].list_assemblies[id_assemblie].list_parts = copy.deepcopy(filter_list)

    def start_here(self, id_panel, id_assemblie, id_part):
        list_panels = self.list_global.globalList

    """
    def skip_here(self, index):

        list_parts = copy.deepcopy(self.globalList.globalList)
        print("Piece to skip : " + index)

        map_list = list(map(lambda x: x.set_skip(True) if x.get_index() == int(index) else x, list_parts))
        filter_list = list(filter(lambda x: False if x.get_skip() else True, list_parts))

        self.globalList.globalList = copy.deepcopy(filter_list)

        self.globalList.update_list(filter_list)
    """
