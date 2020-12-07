import tkinter as tk
from tkinter import ttk

class MainWindow():

    def __init__(self, master, *args, **kwargs):

        self.master = master
        self.frame = ttk.Frame(self.master)
        self.frame.pack(side="top", fill="both", expand=True)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)

        group = tk.LabelFrame(self.frame, text="OAT")
        tk.Button(group, text="Ok").pack()
        group.grid(row=0, column=0)

        group = tk.LabelFrame(self.frame, text="Status")
        tk.Button(group, text="Ok").pack()
        group.grid(row=1, column=0)

        group = tk.LabelFrame(self.frame, text="RA/Dec")
        tk.Button(group, text="Ok").pack()
        group.grid(row=0, column=1)

        group = tk.LabelFrame(self.frame, text="Alt/Az")
        tk.Button(group, text="Ok").pack()
        group.grid(row=1, column=1)
