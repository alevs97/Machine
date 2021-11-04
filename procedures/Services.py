from entities.GlobalListPanelsSingleton import GlobalListPanelsSingleton
import copy

class Services:

    def __init__(self):

        self.list_global = GlobalListPanelsSingleton()

    def skip_here(self, id_panel, id_assemblie, id_part,index_frame):



        if index_frame == 0:
            list_panels = self.list_global.globalList
            panel = self.list_global.globalList[id_panel]

            filter_list = list(filter(lambda x: x.get_id() != panel.get_id(), list_panels))
            self.list_global.globalList = copy.deepcopy(filter_list)

        elif index_frame == 1:
            list_assemblies = self.list_global.globalList[id_panel].list_assemblies
            assemblie = self.list_global.globalList[id_panel].list_assemblies[id_assemblie]

            filter_list = list(filter(lambda x: x.get_id() != assemblie.get_id(), list_assemblies))
            self.list_global.globalList[id_panel].list_assemblies = copy.deepcopy(filter_list)

        elif index_frame == 2:
            list_parts = self.list_global.globalList[id_panel].list_assemblies[id_assemblie].list_parts
            part = self.list_global.globalList[id_panel].list_assemblies[id_assemblie].list_parts[id_part]

            filter_list = list(filter(lambda x: x.get_id() != part.get_id(), list_parts))
            self.list_global.globalList[id_panel].list_assemblies[id_assemblie].list_parts = copy.deepcopy(filter_list)



    def filter_by_part(self, id_panel, id_assemblie, id_part):
        # Fitler by part
        list_parts = self.list_global.globalList[id_panel].list_assemblies[id_assemblie].list_parts
        part = list_parts[id_part]
        filter_list_parts = list(filter(lambda x: x.get_id() >= part.get_id(), list_parts))
        for i in filter_list_parts:
            print(i)
        return filter_list_parts

    def filter_by_assemblie(self, id_panel, id_assemblie):
        #Fitler by assemblies
        list_assemblies = self.list_global.globalList[id_panel].list_assemblies
        assemblie = list_assemblies[id_assemblie]
        filter_list_assemblies = list(filter(lambda x: x.get_id() >= assemblie.get_id(), list_assemblies))
        for i in filter_list_assemblies:
            print(i)
        return filter_list_assemblies

    def filter_by_panel(self, id_panel):
        # Filter by panels
        list_panels = self.list_global.globalList
        panel = list_panels[id_panel]
        filter_list_panels = list(filter(lambda x: x.get_id() >= panel.get_id(),list_panels))
        for i in filter_list_panels:
            print(i)
        return filter_list_panels


    def start_here(self, id_panel, id_assemblie, id_part, index_frame):



        if index_frame == 2:

            filter_list_parts = self.filter_by_part(id_panel, id_assemblie, id_part)
            filter_list_assemblies = self.filter_by_assemblie(id_panel, id_assemblie)
            filter_list_panels = self.filter_by_panel(id_panel)

            self.list_global.globalList[id_panel].list_assemblies[id_assemblie].list_parts = copy.deepcopy(filter_list_parts)
            self.list_global.globalList[id_panel].list_assemblies = copy.deepcopy(filter_list_assemblies)
            self.list_global.globalList = copy.deepcopy(filter_list_panels)

        elif index_frame == 1:

            filter_list_assemblies = self.filter_by_assemblie(id_panel, id_assemblie)
            filter_list_panels = self.filter_by_panel(id_panel)

            self.list_global.globalList[id_panel].list_assemblies = copy.deepcopy(filter_list_assemblies)
            self.list_global.globalList = copy.deepcopy(filter_list_panels)

        elif index_frame == 0:

            filter_list_panels = self.filter_by_panel(id_panel)

            self.list_global.globalList = copy.deepcopy(filter_list_panels)


