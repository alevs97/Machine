import json


from entities.Part import Part
from entities.Panel import Panel
"""
File related with the data in the project
"""


class LoadData:

    _listParts = []
    _listPanels = []
    _aux = 0


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
                self.process_data_json_iterator(data)
                print("asdfasdfa")
                return self._listParts


        return "Error"


    def process_data_json_iterator(self,data):
        iterator_dict = iter(data.items())
        while True:
            try:
                element = next(iterator_dict)
            except StopIteration:
                break

            #print(type(iterator_dict))

            #if (isinstance(element[1],dict)):
            if (element[0] == 'Parts'):

                self._aux = self._aux + 1
                print("Parte " + str(self._aux))
            else:
                for element_list in element[1]:
                    self.process_data_json_iterator(element_list)


            if isinstance(element[1],list):
                for element_list in element[1]:
                    self.process_data_json_iterator(element_list)
                    #print("lista")





    """
    def process_data_json(self, data):

        if isinstance(data, dict):
            for k, v in data.items():
                if (k == 'Name') and (v.find("Wall") != -1):
                    continue
                    print(v)

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

    """
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

    """
