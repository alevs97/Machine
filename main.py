import time
from tkinter.tix import Tk

from interface.NewInterface import NewInterface
from entities.GlobalListPanelsSingleton import GlobalListPanelsSingleton
from repository.load_data import LoadData
from repository.SafeData import SafeData
from procedures.Services import Services
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

    global_list.globalList= data.load_data_json('prueba.json')


    # list=data.load_data_json('6_Walls.json')
    print("###############")
    for i in global_list.globalList:
        print(i.__str__())
        i.print_assemblies()
        for a in i.list_assemblies:
            a.print_parts()
            print(" ")


    safe = SafeData()
    safe.write_file()

    #services =  Services()
    #services.skip_here(1,2,3,0)



    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(str(width) + "x" + str(height))

    interface = NewInterface(root)

    interface.main_frame()
    interface.pack(fill="both", expand=1)
    interface.mainloop()


    """
    
    # App Refactor
    appRefactor = AppRefactor()
    appRefactor.pack(fill="both", expand=1)
    appRefactor.main_frame()
    appRefactor.config(bg="lightblue")
    appRefactor.master.title("Hola App")


    appRefactor.mainloop()

    """





