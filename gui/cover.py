from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
import os
# from WordsSQL import WORDS

from .manege_words import ManegeWords

class COVER(): 
    def __init__(
        self,
        title: str,
        window_size: tuple,
        ) -> None:
        self.window = Tk()
        self.window.title(title)
        x = int(self.window.winfo_screenwidth()/2 - window_size[0]/2)
        y = int(self.window.winfo_screenheight()/2 - window_size[1]/2)
        self.window.geometry("%sx%s+%s+%s" % (window_size[0], window_size[1], x, y))
        
        self.ws = self.window.winfo_screenwidth()
        self.hs = self.window.winfo_screenheight()
        self.label = Label(self.window, text="WORDS", font=("Arial Bold", 50), fg="orange")
        self.btn1 = Button(self.window, text="Learn New Wrods", font=("Arial Bold", 20), command=self.learn_new_words)
        self.btn2 = Button(self.window, text="Manage Words", font=("Arial Bold", 10), command=self.manage_words)
        
        
    def learn_new_words(self):
        self.label.destroy()
        self.btn1.destroy()
        self.btn2.destroy()
        # self.window.geometry("%sx%s+%s+%s" % (self.ws, self.hs, 0, 0))
        # self.window.attributes('-fullscreen', True)
        
    def manage_words(self):
        # self.label.destroy()
        # self.btn1.destroy()
        # self.btn2.destroy()
        self.window_manege_words = ManegeWords(self.window, (1920,1080))
        self.window_manege_words.meanloop()
        # self.window.geometry("%sx%s+%s+%s" % (self.ws, self.hs, 0, 0))
        # self.window.attributes('-fullscreen', True)
        
    def preconfig(self):
        self.label.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.btn1.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.btn2.place(relx=0.5, rely=0.7, anchor=CENTER)
    
    def mainloop(self): 
        self.preconfig()
        
        self.window.mainloop()