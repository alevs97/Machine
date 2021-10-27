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

        # Fitler by part
        list_parts = self.list_global.globalList[id_panel].list_assemblies[id_assemblie].list_parts
        part = list_parts[id_part]
        filter_list_parts = list(filter(lambda x: x.get_id() >= part.get_id(), list_parts))
        for i in filter_list_parts:
            print(i)


        #Fitler by assemblies
        list_assemblies = self.list_global.globalList[id_panel].list_assemblies
        assemblie = list_assemblies[id_assemblie]
        filter_list_assemblies = list(filter(lambda x: x.get_id() >= assemblie.get_id(), list_assemblies))
        for i in filter_list_assemblies:
            print(i)


        # Filter by panels
        list_panels = self.list_global.globalList
        panel = list_panels[id_panel]
        filter_list_panels = list(filter(lambda x: x.get_id() >= panel.get_id(),list_panels))
        for i in filter_list_panels:
            print(i)

        self.list_global.globalList[id_panel].list_assemblies[id_assemblie].list_parts = copy.deepcopy(filter_list_parts)
        self.list_global.globalList[id_panel].list_assemblies = copy.deepcopy(filter_list_assemblies)
        self.list_global.globalList = copy.deepcopy(filter_list_panels)
