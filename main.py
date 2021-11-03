import time
from tkinter.tix import Tk

from interface.App_new import AppNew
from entities.GlobalListPanelsSingleton import GlobalListPanelsSingleton
from repository.load_data import LoadData
from tkinter import *
from tkinter import ttk
import tkinter as tk

from interface.App_new import AppNew

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

    global_list.globalList, global_list.job_description = data.load_data_json('data.json')

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


    """
    
    # App Refactor
    appRefactor = AppRefactor()
    appRefactor.pack(fill="both", expand=1)
    appRefactor.main_frame()
    appRefactor.config(bg="lightblue")
    appRefactor.master.title("Hola App")


    appRefactor.mainloop()

    """

    
    my_app = AppNew(root)
    my_app.pack(fill="both", expand=1)
    #my_app.config(bg="lightblue")
    time.sleep(1)

    my_app.master.title("My Do-Nothing Application")
    my_app.main_frame()
    my_app.mainloop()



