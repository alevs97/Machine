
from tkinter import *
from tkinter import ttk
import tkinter as tk


from entities.GlobalListPanelsSingleton import GlobalListPanelsSingleton
from procedures.services import Services

class App_new(tk.Frame):

    item_selected = False

    my_list_panels = None
    my_list_assemblies = None
    my_list_parts = None

    id_panel = None
    id_assemblie = None
    id_part = None

    frame_list_box = None

    control_back = 0

    label_front_button = None
    label_back_button = None
    label_skip_button = None
    label_start_here_button = None

    def __init__(self, master= None):
        super().__init__(master)
        self.list_global = GlobalListPanelsSingleton()
        self.services = Services()

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

        # Widgets 1° Column
        ttk.Label(frame_east,text="Options to select").grid(pady=5,row=0, column=0)
        ttk.Button(frame_east, text="Skip", command=self.service_skip).grid(pady=5,row=1, column=0)
        ttk.Button(frame_east, text="Start Here", command=self.service_start_here).grid(pady=5,row=2, column=0)

        # Widgets 2° Column
        self.label_skip_button = ttk.Label(frame_east, text="",width=30)
        self.label_skip_button .grid(pady=5,row=1, column=1, columnspan=2,sticky="w")

        self.label_start_here_button = Label(frame_east, text="")
        self.label_start_here_button.grid(pady=5,row=2, column=1, columnspan=2,sticky="w")

        frame_east.rowconfigure(0, weight=1)
        frame_east.rowconfigure(1, weight=1)
        frame_east.rowconfigure(2, weight=1)

        frame_east.columnconfigure(0, weight=1)
        frame_east.columnconfigure(1, weight=1)
        frame_east.columnconfigure(2, weight=1)


        frame_east.grid(pady=5,row=1, column=2,sticky="nsew")

    def frame_nort_west(self):
        pass
        #ttk.Label(self, text="Hola mundo").grid(pady=5, row=0, column=0)

    def frame_nort(self):
        frame_nort = ttk.Frame(self)

        # Widgets in the row -> 1
        ttk.Button(frame_nort,text="Go to ",command=self.control_go_to).grid(pady=5, row=1, column=2, sticky="s")
        ttk.Label(frame_nort, text="Name of the project: ").grid(pady=5, row=1, column=1, sticky="s")
        ttk.Button(frame_nort,text="Back",command=self.control_button_back).grid(pady=5, row=1, column=0, sticky="s")

        # Widgets in the row -> 2
        frame_label_back = Frame(frame_nort, highlightbackground="black", highlightthickness=1, bd=0)
        frame_label_back.grid(row=2, column=0, sticky="nsew")

        self.label_back_button = Label(frame_label_back,text="")
        self.label_back_button.grid(pady=5,sticky="nsew")

        frame_label_back.columnconfigure(0, weight=1)
        frame_label_back.rowconfigure(0, weight=1)

        Label(frame_nort,text=str(self.list_global.job_description),borderwidth=2, relief="groove",padx=15,pady=10)\
            .grid(row=2, column=1,sticky="n")

        frame_label_go_to = Frame(frame_nort, highlightbackground="black", highlightthickness=1, bd= 0)
        frame_label_go_to.grid(row=2, column=2,sticky="nsew")

        self.label_front_button = Label(frame_label_go_to,text="" )
        self.label_front_button.grid(sticky="nsew")

        frame_label_go_to.columnconfigure(0, weight=1)
        frame_label_go_to.rowconfigure(0, weight=1)

        frame_nort.columnconfigure(0, weight=1)
        frame_nort.columnconfigure(1, weight=1)
        frame_nort.columnconfigure(2, weight=1)

        frame_nort.rowconfigure(0, weight=1)
        frame_nort.rowconfigure(1, weight=1)
        frame_nort.rowconfigure(2, weight=1)


        frame_nort.grid(pady=5,row=0, column=1,sticky="nsew")

    def frame_center(self):
        self.render_scroll_frame_panels()

    def service_skip(self):

        try:

            self.services.skip_here(self.id_panel,self.id_assemblie,self.id_part,self.control_back)

        except TypeError:

            print("Skip no specified")

        finally:

            self.clear_frame()
            self.clear_labels()

            if self.item_selected and self.control_back ==2:
                self.render_scroll_frame_parts()
            elif self.item_selected and self.control_back == 1:
                self.render_scroll_frame_assemblies()
            elif self.item_selected and self.control_back == 0:
                self.render_scroll_frame_panels()
            else:
                print("Skip invalido")


    def service_start_here(self):

        try:
            self.services.start_here(self.id_panel,self.id_assemblie,self.id_part, self.control_back)
        except TypeError:
            print("Service Strar Unavailable ")
        finally:
            self.clear_frame()
            self.clear_labels()

            self.render_scroll_frame_panels()
            self.control_back = 0

    def clear_labels(self):
        self.label_skip_button.config(text="")
        self.label_start_here_button.config(text="")
        self.label_front_button.config(text="")

    #----------------------------------------------------------------------------------
    # ---------------------------------Validation Back Button--------------------------
    def control_button_back(self):

        if self.control_back == 1:
            self.go_back_frame()
            self.control_back = self.control_back - 1
        elif self.control_back == 2:
            self.go_back_assemblie()
            self.control_back = self.control_back - 1
        else:
            print("Variable vacia ")


    def go_back_assemblie(self):
        self.clear_frame()
        self.render_scroll_frame_assemblies()
        self.label_back_button.config(text="Return to Panel list")
        self.id_panel = None
        self.id_assemblie = None
        self.id_part = None
        self.label_skip_button.config(text="")
        self.label_start_here_button.config(text="")

    def go_back_frame(self):
        self.clear_frame()
        self.render_scroll_frame_panels()
        self.label_back_button.config(text="")
        self.id_panel = None
        self.id_assemblie = None
        self.id_part = None
        self.label_skip_button.config(text="")
        self.label_start_here_button.config(text="")

    def clear_skip_and_start(self):
        self.label_skip_button.config(text="")
        self.label_start_here_button.config(text="")

    # ----------------------------------------------------------------------------------
    # ---------------------------------Button Go to-----------------------------
    def control_go_to(self):
            if self.control_back == 0:
                try:
                    self.clear_frame()
                    self.render_scroll_frame_assemblies()
                except TypeError:
                    print("Unable press")
                    self.render_scroll_frame_panels()
                else:
                    self.label_back_button.config(text="Return to Panel list")
                    self.control_back = self.control_back + 1
                finally:
                    self.label_front_button.config(text="")
                    self.clear_skip_and_start()
            elif self.control_back == 1:
                try:
                    self.clear_frame()
                    self.render_scroll_frame_parts()
                except TypeError:
                    print("Unable press")
                    self.render_scroll_frame_assemblies()
                else:
                    self.label_back_button.config(text="Return to Assemblies list")
                    self.control_back = self.control_back + 1
                finally:
                    self.label_front_button.config(text="")
                    self.clear_skip_and_start()
            else:
                print("Variable al max")
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

        #Variable
        panel = self.list_global.globalList[self.id_panel]
        assemblie = panel.list_assemblies[self.id_assemblie]

        #Label of ahere are you
        # TODO: ADD Label where are you(Part/Asseblie/Panel )
        Label(self.frame_list_box, text="List of PARTS to process in :"+str(panel.get_id())+"-"+str(panel.get_name())+"/"
                +str(assemblie.get_id())+"-"+str(assemblie.get_name()),height=1).grid(pady=5, row=0, column=1)

        #Creating the listbox
        self.my_list_parts = Listbox(self.frame_list_box)
        for line in assemblie.list_parts:
            self.my_list_parts.insert(END, str(line.get_id()) + " - " + line.get_name() + " - "
                                      + line.get_wood_type() + "x" + str(line.height))

        #Put it in the grid
        self.my_list_parts.grid(pady=5, row=1, column=1,sticky="nsew")
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
        self.frame_list_box.grid(pady=5, row=1, column=1,sticky="nsew")

    def render_scroll_frame_assemblies(self):
        """
        Description:
            Frame with the Assemblies in the Panel

        Returns:
            VOID

        """
        # Creating the main frame who could be render
        self.frame_list_box = ttk.Frame(self, padding=10)

        #Variable
        panel = self.list_global.globalList[self.id_panel]

        #Label of where are you
        # TODO: ADD Label where are you(Panel)
        Label(self.frame_list_box, text="List of ASSEMBLIES to process in " +str(panel.get_id()) +"-"+str(panel.get_name()), height=1).\
            grid(pady=5, row=0, column=1)

        #Creating the listbox
        self.my_list_assemblies = Listbox(self.frame_list_box)
        for line in panel.list_assemblies:
            self.my_list_assemblies.insert(END, str(line.get_id()) + " - " + line.get_name())

        #Punt it in the grid
        self.my_list_assemblies.grid(pady=5, row=1, column=1,sticky="nsew")
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
        self.frame_list_box.grid(pady=5, row=1, column=1,sticky="nsew")


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
        self.my_list_panels.grid(pady=5, row=1, column=1,sticky="nsew")
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
        self.frame_list_box.grid(pady=5, row=1, column=1,sticky="nsew")


    #----------------------------------------------------------------------------------
    # ---------------------------------Events-List-Box---------------------------------

    def event_panels(self,event):
        cs = self.my_list_panels.curselection()
        self.item_selected = True
        self.label_front_button.config(text="See assemblies in: \n " + self.my_list_panels.get(cs))
        self.label_skip_button.config(text="You want to skip: \n " + self.my_list_panels.get(cs))
        self.label_start_here_button.config(text="You want to start in: \n " + self.my_list_panels.get(cs))
        for i in cs:
            self.id_panel = i
            print(self.list_global.globalList[i])


    def event_parts(self,event):
        cs = self.my_list_parts.curselection()
        self.item_selected = True
        self.label_skip_button.config(text="You want to skip: \n " + self.my_list_parts.get(cs))
        self.label_start_here_button.config(text="You want to start in: \n " + self.my_list_parts.get(cs))
        for i in cs:
            self.id_part = i
            print(self.list_global.globalList[self.id_panel].list_assemblies[self.id_assemblie].list_parts[i])

    def event_assemblies(self,event):
        cs = self.my_list_assemblies.curselection()
        self.item_selected = True
        self.label_front_button.config(text=" See parts in:  \n " + self.my_list_assemblies.get(cs))
        self.label_skip_button.config(text="You want to skip: \n " + self.my_list_assemblies.get(cs))
        self.label_start_here_button.config(text="You want to start in: \n " + self.my_list_assemblies.get(cs))
        for i in cs:
            self.id_assemblie =i
            print(self.list_global.globalList[self.id_panel].list_assemblies[i])


    #----------------------------------------------------------------------------------
    # ---------------------------------Render-app--------------------------------------
    # -----------------------------Destroy widgets-------------------------------------
    def clear_frame(self):
        self.frame_list_box.destroy()



