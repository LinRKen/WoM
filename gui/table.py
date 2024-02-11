from tkinter import *
from tkinter.ttk import Treeview
from mysql.WordsSQL import WORDS

class TABLE():
    def __init__(
        self,
        fa: object,
        sql: object,
        ) -> None:
        super().__init__()
        self.sql = sql
        columns = self.sql.get_columns()
        values = self.sql.get_values()
        self.table = Treeview(fa, height=10, show="headings", columns=columns)
        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=100, minwidth=100, anchor='center')
        for value in values:
            self.table.insert('', END, values=value)
    
    def insert(self, values):
        # self.table.insert('', END, values=values)
        self.sql.insert_word(values)
        
    def get_table(self):
        return self.table
    
    def set_cell_value(self, event): # 双击进入编辑状态
        for item in self.table.selection():
            #item = I001
            item_text = self.table.item(item, "values")
            print(item_text[0:2])  # 输出所选行的值
        column= self.table.identify_column(event.x)# 列
        row = self.table.identify_row(event.y)  # 行
        cn = int(str(column).replace('#',''))
        rn = int(str(row).replace('I',''))