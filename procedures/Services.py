from entities.GlobalListPanelsSingleton import GlobalListPanelsSingleton
import copy

class Services:

    def __init__(self):

        self.list_global = GlobalListPanelsSingleton()

    def process_unprocess_here(self, id_panel, id_assemble, id_part, index_frame, section):

        if index_frame == 0:

            list_panels = self.list_global.globalList
            panel = self.list_global.globalList[id_panel]

            def function_panel(x):
                if x.get_id() == panel.get_id():
                    x.set_processed(section)
                    for assemble in x.list_assemblies:
                        assemble.set_processed(section)
                        for part in assemble.list_parts:
                            part.set_processed(section)
                return x

            map_list = list(map(function_panel, list_panels))

            self.list_global.globalList = copy.deepcopy(map_list)

        elif index_frame == 1:

            list_assemblies = self.list_global.globalList[id_panel].list_assemblies
            assemble = self.list_global.globalList[id_panel].list_assemblies[id_assemble]

            def function_assemblie(x):
                if x.get_id() == assemble.get_id():
                    x.set_processed(section)
                    for part in x.list_parts:
                        part.set_processed(section)
                return x

            map_list = list(map(function_assemblie, list_assemblies))

            count_unprocessed = 0
            for i in list_assemblies:
                if i.get_processed() == True:
                    count_unprocessed = count_unprocessed + 1
                    print(count_unprocessed)
                if len(list_assemblies) == count_unprocessed:
                    self.list_global.globalList[id_panel].set_processed(True)
                else:
                    self.list_global.globalList[id_panel].set_processed(False)

            self.list_global.globalList[id_panel].list_assemblies = copy.deepcopy(map_list)

        elif index_frame == 2:

            list_parts = self.list_global.globalList[id_panel].list_assemblies[id_assemble].list_parts
            part = self.list_global.globalList[id_panel].list_assemblies[id_assemble].list_parts[id_part]

            def function_part(x):
                if x.get_id() == part.get_id():
                    x.set_processed(section)
                    if not section:
                        self.list_global.globalList[id_panel].list_assemblies[id_assemble].set_processed(False)
                        self.list_global.globalList[id_panel].set_processed(False)
                return x

            map_list = list(map(function_part, list_parts))

            self.list_global.globalList[id_panel].list_assemblies[id_assemble].list_parts = copy.deepcopy(map_list)



