import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk

from procedures.services import Services
from entities.GlobalListPartSingleton import GlobalListPartSingleton


class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.services = Services()
        self.list_global = GlobalListPartSingleton()


    def screen(self):

        #Section to SKIP PIECE
        ttk.Label(self, text="Introduce the index of the part to skip: ").pack()
        entry_skip = ttk.Entry(self)
        entry_skip.pack()
        ttk.Button(self, text="Skip Piece", command=lambda: self._skip_piece_app(entry_skip.get())).pack()


        #Section to START IN THIS PIECE
        ttk.Label(self, text="Introduce the piece where do want to start: ").pack()
        entry_strat = ttk.Entry(self)
        entry_strat.pack()
        ttk.Button(self, text="Start Here", command=lambda: self._start_here_app(entry_strat.get())).pack()

        self._render_scroll_frame()




    def _render_scroll_frame(self):
        # LIST OF PIECES
        frame_list = ttk.Frame(self, padding=10)

        ttk.Label(frame_list, text="List of Parts to process ").pack()
        scrollbar = ttk.Scrollbar(frame_list)
        scrollbar.pack(side=LEFT, fill=Y)

        mylist = Listbox(frame_list, yscrollcommand=scrollbar.set)
        for line in self.list_global.globalList:
            mylist.insert(END, str(line.get_index()) + " - " + line.get_name())

        mylist.pack(side=RIGHT, fill=BOTH)
        scrollbar.config(command=mylist.yview)
        frame_list.pack()


    def _skip_piece_app(self, index):
        self.services.skip_here(index)
        self.clear()
        self._render_scroll_frame()


    def _start_here_app(self, index):
        self.services.start_here(index)
        self.clear()
        self._render_scroll_frame()

    def clear(self):
        list = self.pack_slaves()
        for l in list:
            if isinstance(l, ttk.Frame):
                print(type(l))
                l.destroy()


