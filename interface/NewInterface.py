import tkinter as tk
from tkinter import ttk
from tkinter.constants import VERTICAL, END

from entities.GlobalListPanelsSingleton import GlobalListPanelsSingleton
from procedures.Services import Services


class NewInterface(tk.Frame):

    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        # External services
        self.list_global = GlobalListPanelsSingleton()
        self.service = Services()

        # Aux variables
        self.id_panel = 0
        self.id_assemble = 0
        self.id_part = 0

        # General widgets
        self.widget_listbox_panel = None
        self.widget_listbox_assemblies = None
        self.widget_listbox_parts = None

        # ListBox
        self.my_list_panels = None
        self.my_list_assemblies = None
        self.my_list_parts = None

        # String variables
        self.lumber = tk.StringVar()
        self.remain = tk.StringVar()
        self.part = tk.StringVar()
        self.partheight = tk.StringVar()
        self.message = tk.StringVar()
        self.alert = tk.StringVar()
        self.laser = tk.StringVar()

    def main_frame(self):

        # Row 1 Widgets
        self.frame_information_panel()
        self.frame_buttons()

        # Row 2 and 3 Widgets
        self.frame_listbox_panels()
        self.frame_listbox_assemblies()
        self.frame_listbox_parts()

        # Distribution in the widgets
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)

    # ------------------Frames-first-row---------------------
    def frame_information_panel(self):
        frame_information = tk.Frame(self)
        """
        ttk.Separator(frame_information, orient=tk.HORIZONTAL).grid(column=1, row=4, sticky='we')
        ttk.Label(frame_information, textvariable=self.laser, text="asdfas").grid(column=1, row=6, pady=5)
        ttk.Label(frame_information, textvariable=self.lumber).grid(column=2, row=1, pady=5)
        ttk.Label(frame_information, textvariable=self.remain).grid(column=2, row=2, pady=5)
        ttk.Separator(frame_information, orient=tk.HORIZONTAL).grid(column=2, row=3, sticky='we')
        ttk.Label(frame_information, textvariable=self.part).grid(column=2, row=4, pady=5)
        ttk.Label(frame_information, textvariable=self.partheight).grid(column=2, row=5, pady=5)
        ttk.Separator(frame_information, orient=tk.HORIZONTAL).grid(column=2, row=6, sticky='we')
        ttk.Label(frame_information, textvariable=self.message).grid(column=2, row=7, pady=5)
        """
        ttk.Separator(frame_information, orient=tk.HORIZONTAL).grid(column=1, row=4, sticky='we')
        tk.Label(frame_information, text="asdfas").grid(column=1, row=6, pady=5)
        tk.Label(frame_information, text="dasdfas").grid(column=2, row=1, pady=5)
        tk.Label(frame_information, text="asdfasdf ad").grid(column=2, row=2, pady=5)
        ttk.Separator(frame_information, orient=tk.HORIZONTAL).grid(column=2, row=3, sticky='we')
        tk.Label(frame_information, text="ADASDFASDF ").grid(column=2, row=4, pady=5)
        tk.Label(frame_information, text="ADASDFASDF ").grid(column=2, row=5, pady=5)
        ttk.Separator(frame_information, orient=tk.HORIZONTAL).grid(column=2, row=6, sticky='we')
        tk.Label(frame_information, text="fasdgfasdgsdf").grid(column=2, row=7, pady=5)
        ttk.Separator(frame_information, orient=tk.HORIZONTAL).grid(column=2, row=8, sticky='we')

        frame_information.columnconfigure(0, weight=1)
        frame_information.columnconfigure(1, weight=1)
        frame_information.columnconfigure(2, weight=8)
        frame_information.columnconfigure(3, weight=1)

        frame_information.grid(row=0, column=1, columnspan=2, sticky="nsew")

    def frame_buttons(self):
        widget_frame_button = tk.Frame(self)

        # Widgets
        tk.Button(widget_frame_button, text="Pause").grid(pady=5, padx=5, row=0, column=1, sticky="nsew")
        tk.Button(widget_frame_button, text="Start").grid(pady=5, padx=5, row=2, column=1, sticky="nsew")
        tk.Button(widget_frame_button, text="Continue").grid(pady=5, padx=5, row=4, column=1, sticky="nsew")

        # Distribution
        widget_frame_button.rowconfigure(0, weight=1)
        widget_frame_button.rowconfigure(1, weight=1)
        widget_frame_button.rowconfigure(2, weight=1)
        widget_frame_button.rowconfigure(3, weight=1)
        widget_frame_button.rowconfigure(4, weight=1)

        widget_frame_button.columnconfigure(0, weight=1)
        widget_frame_button.columnconfigure(1, weight=1)
        widget_frame_button.columnconfigure(2, weight=1)

        widget_frame_button.grid(row=0, column=3, sticky="nsew")

    # ------------------Frames-second-row---------------------
    def frame_listbox_panels(self):
        """
                Description:
                    Frame with the Panels in the project

                Returns:
                    VOID

                """
        # Creating the main frame who could be render.
        self.widget_listbox_panel = ttk.Frame(self, padding=15)

        # Label of where are you
        # TODO: ADD Label where are you(Project)
        tk.Label(self.widget_listbox_panel, text="List of PANELS to process ").grid(pady=5, row=0, column=1)

        # Creating the listBox
        self.my_list_panels = tk.Listbox(self.widget_listbox_panel)
        for line in self.list_global.globalList:
            self.my_list_panels.insert(END, str(line.get_id()) + " - " + line.get_name())

        # Put it in the grid
        self.my_list_panels.grid(pady=5, row=1, column=1, sticky="nsew")
        # Adding the event to navigate
        self.my_list_panels.bind('<Button-1>', self.event_panels)

        # Creating and binding with the listbox
        scrollbar = tk.Scrollbar(self.widget_listbox_panel, orient=VERTICAL, command=self.my_list_panels.yview)
        # Put it in the grid
        scrollbar.grid(pady=5, row=1, column=0, sticky="ns")

        # Communicate back to the scrollbar
        self.my_list_panels.config(yscrollcommand=scrollbar.set)

        # Frame button skip and start here
        frame_skip_start_here = ttk.Frame(self.widget_listbox_panel)
        frame_skip_start_here.grid(pady=10, row=2, column=1, sticky="nsew")

        tk.Button(frame_skip_start_here, text="Skip", command=lambda: self.skip_button(0)).grid(row=0, column=0,
                                                                                                sticky="nsew")
        tk.Button(frame_skip_start_here, text="Start Here", command=lambda: self.start_here_button(0)).\
            grid(row=0, column=1, sticky="nsew")

        # Dimension columns
        frame_skip_start_here.columnconfigure(0, weight=1)
        frame_skip_start_here.columnconfigure(1, weight=1)

        # Dimension rows
        frame_skip_start_here.rowconfigure(0, weight=1)

        # Dimension columns
        self.widget_listbox_panel.columnconfigure(0, weight=0)
        self.widget_listbox_panel.columnconfigure(1, weight=1)

        # Dimension Row
        self.widget_listbox_panel.rowconfigure(0, weight=0)
        self.widget_listbox_panel.rowconfigure(1, weight=1)
        self.widget_listbox_panel.rowconfigure(2, weight=0)

        # Put it in the main grid
        self.widget_listbox_panel.grid(pady=5, row=1, column=1, rowspan=2, sticky="nsew")

    def frame_listbox_assemblies(self):
        """
                Description:
                    Frame with the Assemblies in the Panel

                Returns:
                    VOID

                """
        # Creating the main frame who could be render
        self.widget_listbox_assemblies = ttk.Frame(self, padding=15)

        # Variable
        panel = self.list_global.globalList[self.id_panel]

        # Label of where are you
        # TODO: ADD Label where are you(Panel)
        tk.Label(self.widget_listbox_assemblies,
                 text="List of ASSEMBLIES to process in : \n " + str(panel.get_id()) + "-" + str(panel.get_name())). \
            grid(pady=5, row=0, column=1)

        # Creating the listbox
        self.my_list_assemblies = tk.Listbox(self.widget_listbox_assemblies)
        for line in panel.list_assemblies:
            self.my_list_assemblies.insert(END, str(line.get_id()) + " - " + line.get_name())

        # Punt it in the grid
        self.my_list_assemblies.grid(pady=5, row=1, column=1, sticky="nsew")
        # Adding the event to navigate
        self.my_list_assemblies.bind('<Button-1>', self.event_assemblies)

        # Creating and binding with the listbox
        scrollbar = tk.Scrollbar(self.widget_listbox_assemblies, orient=VERTICAL, command=self.my_list_assemblies.yview)
        # Put it in the grid
        scrollbar.grid(pady=5, row=1, column=0, sticky="ns")

        # Communicate back to the scrollbar
        self.my_list_assemblies.config(yscrollcommand=scrollbar.set)

        # Frame button skip and start here
        frame_skip_start_here = ttk.Frame(self.widget_listbox_assemblies)
        frame_skip_start_here.grid(pady=10, row=2, column=1, sticky="nsew")

        tk.Button(frame_skip_start_here, text="Skip", command=lambda: self.skip_button(1)).grid(row=0, column=0,
                                                                                                sticky="nsew")
        tk.Button(frame_skip_start_here, text="Start Here", command=lambda: self.start_here_button(1))\
            .grid(row=0, column=1, sticky="nsew")

        # Dimension columns
        frame_skip_start_here.columnconfigure(0, weight=1)
        frame_skip_start_here.columnconfigure(1, weight=1)

        # Dimension rows
        frame_skip_start_here.rowconfigure(0, weight=1)

        # Dimension columns
        self.widget_listbox_assemblies.columnconfigure(0, weight=0)
        self.widget_listbox_assemblies.columnconfigure(1, weight=1)

        # Dimension Row
        self.widget_listbox_assemblies.rowconfigure(0, weight=0)
        self.widget_listbox_assemblies.rowconfigure(1, weight=1)
        self.widget_listbox_assemblies.rowconfigure(2, weight=0)

        # Put it in the main grid
        self.widget_listbox_assemblies.grid(pady=5, row=1, column=2, rowspan=2, sticky="nsew")

    def frame_listbox_parts(self):
        """
               Description:
                   Frame with the Parts in the
               Returns:
                   VOID
               """

        # Creating the main frame who could be render
        self.widget_listbox_parts = ttk.Frame(self, padding=15)

        # Variable
        panel = self.list_global.globalList[self.id_panel]
        try:
            assemble = panel.list_assemblies[self.id_assemble]
        except IndexError:
            print("Index Error")
            self.id_assemble = 0
            assemble = panel.list_assemblies[self.id_assemble]

        # Label of ahere are you
        # TODO: ADD Label where are you(Part/Assemble/Panel )
        tk.Label(self.widget_listbox_parts,
                 text="List of PARTS to process in :\n" + str(panel.get_id()) + "-" + str(panel.get_name()) + "/"
                      + str(assemble.get_id()) + "-" + str(assemble.get_name())).grid(pady=5, row=0, column=1)

        # Creating the listbox
        self.my_list_parts = tk.Listbox(self.widget_listbox_parts)
        for line in assemble.list_parts:
            self.my_list_parts.insert(END, str(line.get_id()) + " - " + line.get_name() + " - "
                                      + line.get_wood_type() + "x" + str(line.height))

        # Put it in the grid
        self.my_list_parts.grid(pady=5, row=1, column=1, sticky="nsew")
        # Adding the event to navigate
        self.my_list_parts.bind('<Button-1>', self.event_parts)

        # Creating and binding with the listbox
        scrollbar = tk.Scrollbar(self.widget_listbox_parts, orient=VERTICAL, command=self.my_list_parts.yview)
        # Put it in the grid
        scrollbar.grid(pady=5, row=1, column=0, sticky="ns")

        # Communicate back to the scrollbar
        self.my_list_parts.config(yscrollcommand=scrollbar.set)

        # Frame button skip and start here
        frame_skip_start_here = ttk.Frame(self.widget_listbox_parts)
        frame_skip_start_here.grid(pady=10, row=2, column=1, sticky="nsew")

        tk.Button(frame_skip_start_here, text="Skip", command=lambda: self.skip_button(2)).grid(row=0, column=0,
                                                                                                sticky="nsew")
        tk.Button(frame_skip_start_here, text="Start Here", command=lambda: self.start_here_button(2))\
            .grid(row=0, column=1, sticky="nsew")

        # Dimension columns
        frame_skip_start_here.columnconfigure(0, weight=1)
        frame_skip_start_here.columnconfigure(1, weight=1)

        # Dimension rows
        frame_skip_start_here.rowconfigure(0, weight=1)

        # Dimesion columns
        self.widget_listbox_parts.columnconfigure(0, weight=0)
        self.widget_listbox_parts.columnconfigure(1, weight=1)

        # Dimesion Row
        self.widget_listbox_parts.rowconfigure(0, weight=0)
        self.widget_listbox_parts.rowconfigure(1, weight=1)
        self.widget_listbox_parts.rowconfigure(2, weight=0)

        # Put it in the main grid
        self.widget_listbox_parts.grid(pady=5, row=1, column=3, rowspan=2, sticky="nsew")

        # ------------------Events-ListBox---------------------

    def event_panels(self, event):
        cs = self.my_list_panels.curselection()

        self.widget_listbox_assemblies.destroy()
        self.frame_listbox_assemblies()

        self.widget_listbox_parts.destroy()
        self.frame_listbox_parts()

        for i in cs:
            self.id_panel = i
            print(self.list_global.globalList[i])

    def event_parts(self, event):
        cs = self.my_list_parts.curselection()

        for i in cs:
            self.id_part = i
            print(self.list_global.globalList[self.id_panel].list_assemblies[self.id_assemble].list_parts[i])

    def event_assemblies(self, event):
        cs = self.my_list_assemblies.curselection()
        self.widget_listbox_parts.destroy()
        self.frame_listbox_parts()
        for i in cs:
            self.id_assemble = i
            print(self.list_global.globalList[self.id_panel].list_assemblies[i])

    def render_listbox(self):
        try:
            self.restart_listbox()
        except IndexError:
            self.id_panel = 0
            self.id_assemble = 0
            self.id_part = 0

            self.restart_listbox()

    def restart_listbox(self):
        self.widget_listbox_panel.destroy()
        self.frame_listbox_panels()

        self.widget_listbox_assemblies.destroy()
        self.frame_listbox_assemblies()

        self.widget_listbox_parts.destroy()
        self.frame_listbox_parts()

    # --------- Events in Skip and Start Here -------------------------
    def skip_button(self, index_frame):
        try:
            self.service.skip_here(self.id_panel, self.id_assemble, self.id_part, index_frame)
        except TypeError:
            print("Service Skip Unavailable")
        else:
            self.render_listbox()

    def start_here_button(self, index_frame):
        try:
            self.service.start_here(self.id_panel, self.id_assemble, self.id_part, index_frame)
        except TypeError:
            print("Service Start Unavailable")
        else:
            self.render_listbox()
