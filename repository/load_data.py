import json

from entities.Part import Part
from entities.Panel import Panel
"""
File related with the data in the project
"""


class LoadData:

    _listParts = []
    _listPanels = []

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
                self.process_data_json(data)
                return self._listParts


        return "Error"

    """

    def process_data_json(self, data):
        come_list_panels = False
        come_parts_wall = False
        if isinstance(data, dict):
            for k, v in data.items():
                if (k == 'Name') and (v.find("Wall") != -1):
                    come_list_panels = True
                    continue

                if (k == 'Assemblies') and (come_list_panels):
                    self.save_panels_in_list(v)
                    come_parts_wall = True
                    come_list_panels = False
                    continue

                else:
                    self.process_data_json(v)
        elif isinstance(data, list):
            for element in data:
                self.process_data_json(element)


    def save_parts_wall_in_panel(self):
        pass

    def save_panels_in_list(self, panels):
        for panel in panels:
            index = len(self._listPanels) + 1
            newPanel = Panel(id = index)
            self._listPanels.append(newPanel)

    """



   #def save_part_in_


    def process_data_json(self, data):
        if isinstance(data, dict):
            for k, v in data.items():
                if k == 'Parts':
                    self.save_part_in_list(v)
                else:
                    self.process_data_json(v)
        elif isinstance(data, list):
            for element in data:
                self.process_data_json(element)


    def save_part_in_list(self, parts):
        for part in parts:
            index = len(self._listParts)
            printSection = part["PrintSections"] if "PrintSections" in part else None
            newPart = Part(part["Name"],part["WoodType"],part["Height"],printSection,
                           part["Processed"],part["Skip"],index + 1 ,part["Flag"])
            self._listParts.append(newPart)

