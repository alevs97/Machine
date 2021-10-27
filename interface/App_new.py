
from tkinter import *
from tkinter import ttk
import tkinter as tk
import copy

from entities.GlobalListPanelsSingleton import GlobalListPanelsSingleton
from procedures.services import Services
class App_new(tk.Frame):

    list_global = GlobalListPanelsSingleton()

    back_frame = None

    my_list_panels = None
    my_list_assemblies = None
    my_list_parts = None

    id_panel = 0
    id_assemblie = 0
    id_part = 0

    control_back = 0

    display_button = False

    services = Services()

    def __int__(self,master=None):
        super().__init__(master)





    def main_frame(self):
        ttk.Label(self,text="Hola mundo").pack()
        ttk.Button(self,text="Back",command=self.control_button_back).pack()
        self.render_scroll_frame_panels()


    def services_parts(self):
        if self.display_button == False:
            ttk.Button(self, text="Skip Part", command=self.service_skip).pack()
            ttk.Button(self, text="Start Here", command=self.control_button_back).pack()
        self.display_button = True

    def service_skip(self):
        self.services.skip_here(self.id_panel,self.id_assemblie,self.id_part)
        self.clear_frame()
        self.render_scroll_frame_parts()

    def control_button_back(self):
        if self.control_back == 1:
            self.go_back_frame()
            self.control_back = self.control_back - 1
        elif self.control_back == 2:
            self.go_back_assemblie()
            self.control_back = self.control_back - 1
            self.display_button = False
            self.clear_buttons()
        else:
            print("Variable vacia ")


    def go_back_assemblie(self):
        self.clear_frame()
        self.render_scroll_frame_assemblies()

    def go_back_frame(self):
        self.clear_frame()
        self.render_scroll_frame_panels()

    def render_scroll_frame_parts(self):
        # LIST OF PIECES
        frame_list = ttk.Frame(self, padding=10)

        ttk.Label(frame_list, text="List of Panels to process ").pack()
        scrollbar = ttk.Scrollbar(frame_list)
        scrollbar.pack(side=LEFT, fill=Y)

        self.my_list_parts = Listbox(frame_list, yscrollcommand=scrollbar.set)

        for line in self.list_global.globalList[self.id_panel].list_assemblies[self.id_assemblie].list_parts:
            self.my_list_parts.insert(END, str(line.get_id()) + " - " + line.get_name())

        self.my_list_parts.pack(side=RIGHT, fill=BOTH)
        self.my_list_parts.bind('<Button-1>', self.event_parts)
        scrollbar.config(command=self.my_list_parts.yview)
        frame_list.pack()

    def render_scroll_frame_assemblies(self):
        # LIST OF PIECES
        frame_list = ttk.Frame(self, padding=10)

        ttk.Label(frame_list, text="List of Panels to process ").pack()
        scrollbar = ttk.Scrollbar(frame_list)
        scrollbar.pack(side=LEFT, fill=Y)

        self.my_list_assemblies = Listbox(frame_list, yscrollcommand=scrollbar.set)

        for line in self.list_global.globalList[self.id_panel].list_assemblies:
            self.my_list_assemblies.insert(END, str(line.get_id()) + " - " + line.get_name())

        self.my_list_assemblies.pack(side=RIGHT, fill=BOTH)
        self.my_list_assemblies.bind('<Button-1>', self.event_assemblies)
        scrollbar.config(command=self.my_list_assemblies.yview)
        frame_list.pack()


    def render_scroll_frame_panels(self):
        # LIST OF PIECES
        frame_list = ttk.Frame(self, padding=10)

        ttk.Label(frame_list, text="List of Assemblies to process ").pack()
        scrollbar = ttk.Scrollbar(frame_list)
        scrollbar.pack(side=LEFT, fill=Y)

        self.my_list_panels = Listbox(frame_list, yscrollcommand=scrollbar.set)

        for line in self.list_global.globalList:
            self.my_list_panels.insert(END, str(line.get_id()) + " - " + line.get_name())

        self.my_list_panels.pack(side=RIGHT, fill=BOTH)
        self.my_list_panels.bind('<Button-1>', self.event_panels)
        scrollbar.config(command=self.my_list_panels.yview)

        frame_list.pack()


    def event_panels(self,event):
        cs = self.my_list_panels.curselection()
        for i in cs:

            self.control_back = self.control_back + 1
            self.id_panel = i
            print(self.list_global.globalList[i])
            self.clear_frame()
            self.render_scroll_frame_assemblies()

    def event_parts(self,event):
        cs = self.my_list_parts.curselection()
        for i in cs:

            self.services_parts()
            self.id_part = i
            print(self.list_global.globalList[self.id_panel].list_assemblies[self.id_assemblie].list_parts[i])



    def event_assemblies(self,event):
        cs = self.my_list_assemblies.curselection()
        for i in cs:

            self.control_back = self.control_back + 1
            self.id_assemblie =i
            print(self.list_global.globalList[self.id_panel].list_assemblies[i])
            self.clear_frame()
            self.render_scroll_frame_parts()



    def clear_frame(self):
        list = self.pack_slaves()
        for l in list:
            if isinstance(l, ttk.Frame):
                l.destroy()

    def clear_buttons(self):
        list = self.pack_slaves()
        i = 0
        for l in list:
            if isinstance(l, ttk.Button) and i<2:
                i = i + 1
                l.destroy()

