from tkinter import *
from tkinter import ttk
import tkinter as tk
from interface_deprecated.ScrollableFrame import ScrollableFrame
from procedures.services import Services
from entities.GlobalListPartSingleton import GlobalListPartSingleton


class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.scroll = ScrollableFrame(self)
        self.global_list = GlobalListPartSingleton()
        self.services = Services()

        self.root = self

    def charge_data(self):
        for element in self.global_list.globalList:

            custom_frame = ttk.Frame(self.scroll.scrollable_frame, padding=10)

            ttk.Label(custom_frame, text=element.get_name()).grid(column=0, row=0)
            ttk.Frame(custom_frame, width=10).grid(column=1, row=0)
            ttk.Button(custom_frame, text="Skip", command= lambda : self.skip_here_app(element.get_index()))\
                .grid(column=2, row=0)
            ttk.Frame(custom_frame, width=10).grid(column=3, row=0)
            ttk.Button(custom_frame, text="Start Here " + str(element.get_index()),
                       command=lambda : self.start_here_app(element.get_index())).grid(column=4, row=0)

            custom_frame.pack()

        self.scroll.pack()

    def start_here_app(self,index):
        self.services.skip_here(index)
        #self.
        print(f'start_here_app print')

        self.charge_data()



    def skip_here_app(self,index):
        self.services.start_here(index)
        print(f'skip_here_app print')
        for i in self.global_list.globalList:
            print(i.__str__())
        self.charge_data()
















    """
    def display_list(self,list):
        scrollbar = Scrollbar(self)
        scrollbar.pack(side = RIGHT, fill = Y)

        myParts = Listbox(self,yscrollcommand = scrollbar.set)
        for line in range(1,100):

            singlePart = self.custom_part(parentWidget = myParts, element=line)
            myParts.insert(END,"singlePart" + str(line))
        myParts.pack(side=LEFT,fill = BOTH)

        scrollbar.config(command = myParts.yview)
        #scrollbar = Label(self,text="Hello").grid(column=0,row=0)

    
    def custom_part(self, parentWidget, element):
        custom_frame = Frame(parentWidget)
        custom_frame.grid()
        Label(custom_frame,text="Number" + str(element)).pack()
        Button(custom_frame,text="Button").pack()

        return custom_frame
    """