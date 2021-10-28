
from tkinter import *
from tkinter import ttk
import tkinter as tk
import copy

from entities.GlobalListPanelsSingleton import GlobalListPanelsSingleton
from procedures.services import Services
class App_new(Frame):


    my_list_panels = None
    my_list_assemblies = None
    my_list_parts = None

    id_panel = 0
    id_assemblie = 0
    id_part = 0

    frame_list_box = None

    control_back = 0

    display_button = False

    list_global = GlobalListPanelsSingleton()
    services = Services()

    def __int__(self, container, *args, **kwargs):
        super().__init__(self, container, *args, **kwargs)


    def main_frame(self):

        # Frames in the frame
        self.frame_nort_west()
        self.frame_nort()
        self.frame_east()
        self.frame_center()


        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

    #----------------------------------------------------------------------------------
    # ---------------------------------Sub Frames interfaces---------------------------
    def frame_east(self):
        frame_east = ttk.Frame(self,padding=10)

        ttk.Label(frame_east,text="Testing Label").grid(pady=5,row=0, column=0)
        ttk.Button(frame_east, text="Skip", command=self.service_skip).grid(pady=5,row=1, column=0)
        ttk.Button(frame_east, text="Start Here", command=self.service_start_here).grid(pady=5,row=2, column=0)

        frame_east.rowconfigure(0, weight=1)
        frame_east.rowconfigure(1, weight=1)
        frame_east.rowconfigure(2, weight=1)

        frame_east.grid(pady=5,row=1, column=2)

    def frame_nort_west(self):
        ttk.Label(self, text="Hola mundo").grid(pady=5, row=0, column=0)

    def frame_nort(self):
        ttk.Button(self,text="Back",command=self.control_button_back).grid(pady=5, row=0, column=1)

    def frame_center(self):

        self.render_scroll_frame_panels()


    def service_skip(self):
        self.services.skip_here(self.id_panel,self.id_assemblie,self.id_part)

        self.clear_frame()
        self.render_scroll_frame_parts()
        self.display_button = False

    def service_start_here(self):
        self.services.start_here(self.id_panel,self.id_assemblie,self.id_part)

        self.clear_frame()
        self.render_scroll_frame_panels()
        self.control_back = 0
        self.display_button = False

    #----------------------------------------------------------------------------------
    # ---------------------------------Validation Back Button--------------------------

    def control_button_back(self):
        if self.control_back == 1:
            self.go_back_frame()
            self.control_back = self.control_back - 1
        elif self.control_back == 2:
            self.go_back_assemblie()
            self.control_back = self.control_back - 1
            self.display_button = False

        else:
            print("Variable vacia ")


    def go_back_assemblie(self):
        self.clear_frame()
        self.render_scroll_frame_assemblies()

    def go_back_frame(self):
        self.clear_frame()
        self.render_scroll_frame_panels()


    #----------------------------------------------------------------------------------
    # ---------------------------------Frames with ListBox-----------------------------

    def render_scroll_frame_parts(self):
        """
        Description:
            Frame with the Parts in the
        Returns:
            VOID
        """

        # Creating the main frame who could be render
        self.frame_list_box = ttk.Frame(self, padding=10)

        #Label of ahere are you
        # TODO: ADD Label where are you(Part/Asseblie/Panel )
        Label(self.frame_list_box, text="List of PARTS to process ",height=1).grid(pady=5, row=0, column=1)

        #Creating the listbox
        self.my_list_parts = Listbox(self.frame_list_box)
        for line in self.list_global.globalList[self.id_panel].list_assemblies[self.id_assemblie].list_parts:
            self.my_list_parts.insert(END, str(line.get_id()) + " - " + line.get_name() + " - "
                                      + line.get_wood_type() + "x" + str(line.height))

        #Put it in the grid
        self.my_list_parts.grid(pady=5, row=1, column=1)
        #Adding the event to navigate
        self.my_list_parts.bind('<Button-1>', self.event_parts)

        #Creating and binding with the listbox
        scrollbar = ttk.Scrollbar(self.frame_list_box,orient=VERTICAL,command=self.my_list_parts.yview)
        #Put it in the grid
        scrollbar.grid(pady=5, row=1, column=0, sticky="ns")

        #Communicate back to the scrollbar
        self.my_list_parts.config(yscrollcommand=scrollbar.set)

        # Dimesion columns
        self.frame_list_box.columnconfigure(0, weight=0)
        self.frame_list_box.columnconfigure(1, weight=1)

        # Dimesion Row
        self.frame_list_box.rowconfigure(0, weight=0)
        self.frame_list_box.rowconfigure(1, weight=1)

        # Put it in the main grid
        self.frame_list_box.grid(pady=5, row=1, column=1)

    def render_scroll_frame_assemblies(self):
        """
        Description:
            Frame with the Assemblies in the Panel

        Returns:
            VOID

        """
        # Creating the main frame who could be render
        self.frame_list_box = ttk.Frame(self, padding=10)

        #Label of where are you
        # TODO: ADD Label where are you(Panel)
        Label(self.frame_list_box, text="List of ASSEMBLIES to process ", height=1).grid(pady=5, row=0, column=1)

        #Creating the listbox
        self.my_list_assemblies = Listbox(self.frame_list_box)
        for line in self.list_global.globalList[self.id_panel].list_assemblies:
            self.my_list_assemblies.insert(END, str(line.get_id()) + " - " + line.get_name())

        #Punt it in the grid
        self.my_list_assemblies.grid(pady=5, row=1, column=1)
        #Adding the event to navigate
        self.my_list_assemblies.bind('<Button-1>', self.event_assemblies)

        #Creatig and binding with the listbox
        scrollbar = ttk.Scrollbar(self.frame_list_box, orient=VERTICAL,command=self.my_list_assemblies.yview)
        #Put it in the grid
        scrollbar.grid(pady=5, row=1, column=0, sticky="ns")

        # Communicate back to the scrollbar
        self.my_list_assemblies.config(yscrollcommand=scrollbar.set)

        # Dimesion columns
        self.frame_list_box.columnconfigure(0, weight=0)
        self.frame_list_box.columnconfigure(1, weight=1)

        # Dimesion Row
        self.frame_list_box.rowconfigure(0, weight=0)
        self.frame_list_box.rowconfigure(1, weight=1)

        #Put it in the main grid
        self.frame_list_box.grid(pady=5, row=1, column=1)


    def render_scroll_frame_panels(self):
        """
        Description:
            Frame with the Panels in the project

        Returns:
            VOID

        """
        #Creating the main frame who could be render.
        self.frame_list_box = ttk.Frame(self, padding=10)

        #Label of where are you
        # TODO: ADD Label where are you(Project)
        Label(self.frame_list_box, text="List of PANELS to process ", height=1).grid(pady=5, row=0, column=1)

        #Creating the listBox
        self.my_list_panels = Listbox(self.frame_list_box)
        for line in self.list_global.globalList:
            self.my_list_panels.insert(END, str(line.get_id()) + " - " + line.get_name())

        #Put it in the grid
        self.my_list_panels.grid(pady=5, row=1, column=1)
        #Adding the evnt to navigate
        self.my_list_panels.bind('<Button-1>', self.event_panels)

        #Creating and binding with the listbox
        scrollbar = ttk.Scrollbar(self.frame_list_box, orient=VERTICAL,command=self.my_list_panels.yview)
        #Put it in the grid
        scrollbar.grid(pady=5, row=1, column=0, sticky="ns")

        # Communicate back to the scrollbar
        self.my_list_panels.config(yscrollcommand=scrollbar.set)

        #Dimesion columns
        self.frame_list_box.columnconfigure(0,weight=0)
        self.frame_list_box.columnconfigure(1,weight=1)

        #Dimesion Row
        self.frame_list_box.rowconfigure(0, weight=0)
        self.frame_list_box.rowconfigure(1, weight=1)

        #Put it in the main grid
        self.frame_list_box.grid(pady=5, row=1, column=1)


    #----------------------------------------------------------------------------------
    # ---------------------------------Events-List-Box---------------------------------

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


    #----------------------------------------------------------------------------------
    # ---------------------------------Render-app--------------------------------------
    # -----------------------------Destroy widgets-------------------------------------
    def clear_frame(self):
        self.frame_list_box.destroy()



