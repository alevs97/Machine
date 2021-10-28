import time
from interface.App_new import App_new
from entities.GlobalListPanelsSingleton import GlobalListPanelsSingleton
from repository.load_data import LoadData
from tkinter import *
from tkinter import ttk
import tkinter as tk

# from procedures.services import Services
"""
Main class
"""

if __name__ == "__main__":

    # Instances
    data = LoadData()
    global_list = GlobalListPanelsSingleton()

    """
    #Charging part in the singleton list
    list = data.load_data_json('data.json')

    for i in list:
        print(i.__str__())

    """

    global_list.globalList = data.load_data_json('data.json')

    # list=data.load_data_json('6_Walls.json')
    print("###############")
    for i in global_list.globalList:
        print(i.__str__())
        i.print_assemblies()
        for a in i.list_assemblies:
            a.print_parts()
            print(" ")



    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(str(width) + "x" + str(height))


    my_app = App_new(root)
    my_app.pack(fill="both", expand=1)
    my_app.config(bg="lightblue")
    time.sleep(1)

    my_app.master.title("My Do-Nothing Application")
    my_app.main_frame()
    my_app.mainloop()

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
