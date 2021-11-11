import json
import copy

from entities.Part import Part
from entities.Panel import Panel
from entities.Assemblie import Assemblie
"""
File related with the data in the project
"""


class LoadData:

    _id_panel = 0
    _id_assemblie = 0
    _id_part = 0

    _listPanels = []
    _job_description = ""


    def load_data_json(self,path = None):
        """
        Description:
        Function to load and process the data come from JSON file of robot framer
        Parameters:
        path -- the path of json file(default None)
        Return:
        list<part> -- of entities of Part
        """
        if(path != None):
            with open(path) as file:
                data = json.load(file)
                self.process_data_json_iterator_2(data)
                return self._listPanels


        return "Error"

    def process_data_json_iterator_2(self, data):
        if isinstance(data, dict):
            iterator_data = iter(data.items())

            while True:
                try:
                    element_dict = next(iterator_data)
                except StopIteration:
                    break

                if element_dict[0] == "Panels":
                    self.add_to_list_panels(element_dict[1])
                else:
                    self.process_data_json_iterator_2(element_dict[1])

        elif isinstance(data, list):
            for element in data:
                self.process_data_json_iterator_2(element)


    def add_to_list_panels(self, list_panels, list_retrieve = None):

        for panel_dict in list_panels:

            if (list_retrieve is None) or (len(list_retrieve) != 0):
                list_retrieve = []

            self._id_panel = self._id_panel + 1
            iter_panel = iter(panel_dict.items())
            while True:
                try:
                    element = next(iter_panel)
                except StopIteration:
                    break

                if element[0] == "Name":

                    new_panel = Panel(name=element[1],id = self._id_panel)
                    element = next(iter_panel)

                    if element[0] == "Processed":
                        new_panel.set_processed(element[1])
                        element = next(iter_panel)

                    if element[0] == "Assemblies":

                        list_retrieve = copy.deepcopy(self.add_to_list_assemblies(element[1]))

                        try:
                            element_1 = next(iter_panel)
                        except StopIteration:
                            new_panel.add_list_assemblies(list_retrieve)

                            self._listPanels.append(new_panel)
                            break


                        panel_assemblie_a = copy.deepcopy(self.add_panel_parts_assemblie(element_1[1]))
                        list_retrieve.append(panel_assemblie_a)
                        new_panel.add_list_assemblies(list_retrieve)
                        self._listPanels.append(new_panel)

                    if element[0] == "Parts":


                        panel_assemblie_b = copy.deepcopy(self.add_panel_parts_assemblie(element[1]))
                        list_retrieve.append(panel_assemblie_b)
                        new_panel.add_list_assemblies(list_retrieve)
                        self._listPanels.append(new_panel)



    def add_panel_parts_assemblie(self, list_parts):
        assemblie_panel = Assemblie("Panel Assemble",self._id_assemblie + 1)
        self._id_assemblie = self._id_assemblie + 1
        list = self.add_to_list_parts(list_parts)
        assemblie_panel.add_list_parts(list)
        return assemblie_panel


    def add_to_list_assemblies(self,list_assemblies, list_retrieve = None ):

        if (list_retrieve is None) or (len(list_retrieve) != 0):
            list_retrieve = []

        for assemblie_dict in list_assemblies:
            assemblie = iter(assemblie_dict.items())


            while True:
                try:
                    element_dict =next(assemblie)
                except StopIteration:
                    break


                new_assemblie = Assemblie(element_dict[1],self._id_assemblie+1)
                self._id_assemblie = self._id_assemblie + 1

                element = next(assemblie)

                if element[0] == "Processed":
                    new_assemblie.set_processed(element[1])
                    element = next(assemblie)

                list = self.add_to_list_parts(element[1])
                new_assemblie.add_list_parts(list)
                list_retrieve.append(new_assemblie)

        return list_retrieve



    def add_to_list_parts(self, list_parts, list_retrieve = None):
        if (list_retrieve is None) or (len(list_retrieve) != 0):
            list_retrieve = list()
        for part in list_parts:

            printSection = part["PrintSections"] if "PrintSections" in part else None

            newPart = Part(name=part["Name"], woodType=part["WoodType"], height=part["Height"], printSections=printSection,
                           processed=part["Processed"], id=self._id_part + 1)
            self._id_part = self._id_part + 1
            list_retrieve.append(newPart)
        return list_retrieve
