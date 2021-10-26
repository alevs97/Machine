from interface.App import App
from entities.GlobalListPartSingleton import GlobalListPartSingleton
from repository.load_data import LoadData
from procedures.services import Services
"""
Main class
"""

if __name__ == "__main__":

    # Instances
    data = LoadData()
    services = Services()
    global_list = GlobalListPartSingleton()

    """
    #Charging part in the singleton list
    list = data.load_data_json('data.json')

    for i in list:
        print(i.__str__())

    """

    #global_list.globalList = data.load_data_json('data.json')

    list=data.load_data_json('6_Walls.json')
    print("###############")
    for i in list:
        print(i.__str__())
        i.print_assemblies()
        for a in i.list_assemblies:
            a.print_parts()
            print(" ")




















    """

    # create the application
    myapp = App()

    #Title app
    myapp.master.title("My Do-Nothing Application")

    #Screen
    myapp.screen()
    #myapp.charge_data()
    myapp.grid()


    # start the program
    myapp.mainloop()
    """



