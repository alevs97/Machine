import json
from entities.GlobalListPanelsSingleton import GlobalListPanelsSingleton


class SafeData:

    def __init__(self):
        self.list_global = GlobalListPanelsSingleton()

    def _panels_to_dict(self, panels):
        return {
            "Panels": panels
        }

    def write_file(self):
        with open("prueba.json","w") as writeFile:
            json.dump(self._panels_to_dict([panel.to_dict() for panel in self.list_global.globalList]),writeFile)