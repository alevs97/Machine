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
                return self._listPanels, self._job_description


        return "Error"

    def process_data_json_iterator_2(self, data):
        if isinstance(data, dict):
            iterator_data = iter(data.items())

            while True:
                try:
                    element_dict = next(iterator_data)
                except StopIteration:
                    break

                if (element_dict[0] == 'JobDescription'):
                    self._job_description = element_dict[1]

                if (element_dict[0] == 'Name') and (element_dict[1].find("Wall") != -1):

                    element_assemblies = next(iterator_data)
                    self.add_to_list_panels(element_assemblies[1])


                else:
                    self.process_data_json_iterator_2(element_dict[1])


        elif isinstance(data, list):
            for element in data:
                self.process_data_json_iterator_2(element)


    def add_to_list_panels(self,list_panels, list_retrieve = None):

        for panel_dict in list_panels:
            self._id_panel = self._id_panel + 1

            if (list_retrieve is None) or (len(list_retrieve) != 0):
                list_retrieve = []

            panel = iter(panel_dict.items())
            while True:
                try:
                    element_dict =next(panel)
                except StopIteration:
                    break

                if(element_dict[0] == "Name") and (element_dict[1].find("Panel") != -1):
                    element = next(panel)


                    if element[0] == "Assemblies":
                        new_panel_1 = Panel(id=self._id_panel)

                        list_retrieve = copy.deepcopy(self.add_to_list_assemblies(element[1]))

                        element_1 = next(panel)

                        panel_assemblie_a = copy.deepcopy(self.add_panel_parts_assemblie(element_1[1]))
                        list_retrieve.append(panel_assemblie_a)
                        new_panel_1.add_list_assemblies(list_retrieve)
                        self._listPanels.append(new_panel_1)


                    if element[0] == "Parts":
                        new_panel_2 = Panel(id=self._id_panel)

                        panel_assemblie_b = copy.deepcopy(self.add_panel_parts_assemblie(element[1]))
                        list_retrieve.append(panel_assemblie_b)
                        new_panel_2.add_list_assemblies(list_retrieve)
                        self._listPanels.append(new_panel_2)


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

                list_parts = next(assemblie)
                list = self.add_to_list_parts(list_parts[1])
                new_assemblie.add_list_parts(list)
                list_retrieve.append(new_assemblie)
        return list_retrieve



    def add_to_list_parts(self, list_parts, list_retrieve = None):
        if (list_retrieve is None) or (len(list_retrieve) != 0):
            list_retrieve = list()
        for part in list_parts:

            printSection = part["PrintSections"] if "PrintSections" in part else None

            newPart = Part(name=part["Name"], woodType=part["WoodType"], height=part["Height"], printSections=printSection,
                           processed=part["Processed"],id=self._id_part + 1)
            self._id_part = self._id_part + 1
            list_retrieve.append(newPart)
        return list_retrieve
