from entities.GlobalListPanelsSingleton import GlobalListPanelsSingleton
import copy

class Services:

    def __init__(self):

        self.list_global = GlobalListPanelsSingleton()

    def skip_here(self, id_panel, id_assemble, id_part, index_frame):

        if index_frame == 0:
            list_panels = self.list_global.globalList
            panel = self.list_global.globalList[id_panel]

            def function_panel(x):
                if x.get_id() == panel.get_id():
                    x.set_processed(True)
                    for assemble in x.list_assemblies:
                        assemble.set_processed(True)
                        for part in assemble.list_parts:
                            part.set_processed(True)
                return x

            map_list = list(map(function_panel, list_panels))

            self.list_global.globalList = copy.deepcopy(map_list)

        elif index_frame == 1:
            list_assemblies = self.list_global.globalList[id_panel].list_assemblies
            assemble = self.list_global.globalList[id_panel].list_assemblies[id_assemble]

            def function_assemblie(x):
                if x.get_id() == assemble.get_id():
                    x.set_processed(True)
                    for part in x.list_parts:
                        part.set_processed(True)
                return x

            map_list = list(map(function_assemblie, list_assemblies))

            self.list_global.globalList[id_panel].list_assemblies = copy.deepcopy(map_list)

        elif index_frame == 2:

            list_parts = self.list_global.globalList[id_panel].list_assemblies[id_assemble].list_parts
            part = self.list_global.globalList[id_panel].list_assemblies[id_assemble].list_parts[id_part]

            def function_part(x):
                if x.get_id() == part.get_id():
                    x.set_processed(True)
                return x

            map_list = list(map(function_part, list_parts))

            self.list_global.globalList[id_panel].list_assemblies[id_assemble].list_parts = copy.deepcopy(map_list)


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

        if index_frame == 0:

            list_panels = self.list_global.globalList
            panel = self.list_global.globalList[id_panel]

            def function(x):
                if x.get_id() <= panel.get_id():
                    x.set_processed(True)
                    for assemble in x.list_assemblies:
                        assemble.set_processed(True)
                        for part in assemble.list_parts:
                            part.set_processed(True)
                return x

            map_list = list(map(function, list_panels))

            self.list_global.globalList = copy.deepcopy(map_list)

        elif index_frame == 1:

            list_panels = self.list_global.globalList
            panel = self.list_global.globalList[id_panel]
            assemblie = list_panels[id_panel].list_assemblies[id_assemblie]

            def function(x):
                def function_1():
                    for assemble in x.list_assemblies:
                        if assemble.get_id() < assemblie.get_id():
                            assemble.set_processed(True)
                            for part in assemble.list_parts:
                                part.set_processed(True)
                if x.get_id() < panel.get_id():
                    x.set_processed(True)
                    function_1()
                elif x.get_id() == panel.get_id():
                    x.set_processed(False)
                    function_1()
                return x

            map_list = list(map(function, list_panels))

            self.list_global.globalList = copy.deepcopy(map_list)

        elif index_frame == 2:
            list_panels = self.list_global.globalList
            panel = self.list_global.globalList[id_panel]
            assemblie = panel.list_assemblies[id_assemblie]
            parts = assemblie.list_parts[id_part]

            def function(x):

                def function_parts(assemble):
                    for part in assemble.list_parts:
                        if part.get_id() < parts.get_id():
                            part.set_processed(True)

                def function_assemblies():
                    for assemble in x.list_assemblies:

                        if assemble.get_id() < assemblie.get_id():
                            assemble.set_processed(True)
                            function_parts(assemble)

                        elif assemble.get_id() == assemblie.get_id():
                            function_parts(assemble)

                if x.get_id() < panel.get_id():
                    x.set_processed(True)
                    function_assemblies()

                elif x.get_id() == panel.get_id():
                    x.set_processed(False)
                    function_assemblies()
                return x

            map_list = list(map(function, list_panels))

            self.list_global.globalList = copy.deepcopy(map_list)


