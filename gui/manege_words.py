from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
import os
import sys
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mysql.WordsSQL import WORDS
from .table import TABLE


class ManegeWords():
    def __init__(self, fa, window_size) -> None:
        super().__init__()
        self.window = Toplevel(fa)
        self.window.title("WORDs")
        x = int(self.window.winfo_screenwidth()/2 - window_size[0]/2)
        y = int(self.window.winfo_screenheight()/2 - window_size[1]/2)
        self.window.geometry("%sx%s+%s+%s" % (window_size[0], window_size[1], x, y))
        
        self.label = Label(self.window, text="Maneger", font=("Arial Bold", 20), fg="orange")
        
        self.mysql = WORDS()
        self.Table = TABLE(self.window, self.mysql)
        
    
        


        
        self.table = self.Table.get_table()
        self.table.place(relx=0.5, rely=0.6, anchor=CENTER)
        
    def preconfig(self):
        self.table = self.Table.get_table()
        self.label.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.table.place(relx=0.5, rely=0.6, anchor=CENTER)
        
        
    def meanloop(self):
        self.preconfig()
        
        
        