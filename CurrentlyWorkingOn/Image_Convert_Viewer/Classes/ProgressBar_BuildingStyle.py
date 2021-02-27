import tkinter as tk
from tkinter import *

class B_ProgressBar(tk.Frame):

    def __init__(self,parent=None,rows=15,columns=10):

        self.rows = rows
        self.columns = columns
        
        tk.Frame.__init__(self,parent,bg='#c7cfb7')
        self.front_windows = []
        self.left_windows = []
        
        self.create_top()
        self.create_windows()
        self.create_left()
        self.grid_layout()
        self.fill_windows()
    def create_left(self):
        
        self.left_side = tk.Frame(self,bg='#394956')
        x = 0
        for row in range(self.rows):
            current_row = []
            for column in range(int(self.columns/2)):
                left_window = tk.Label(self.left_side, 
                                      borderwidth=0, 
                                      width=1,
                                      height=2
                                      )
                if x % 6 == 0:
                   left_window.grid(row=row, 
                                    column=column, 
                                    sticky='nsew',
                                    padx=1,
                                    pady=12
                                    )
                else:
                        left_window.grid(row=row, 
                                    column=column, 
                                    sticky='nsew',
                                    padx=1,
                                    pady=3
                                    )
                current_row.append(left_window)
            x += 1
            self.left_windows.append(current_row)
        
    
    def create_top(self):
        
        self.top_left = tk.Frame(self,borderwidth=5,bg='#394956')
        self.top_top = tk.Frame(self,borderwidth=5,bg='#425362')
        
        cos = tk.Label(self.top_top, text="cos",
                                      borderwidth=0, 
                                      width=2,
                                      height=2
                                      )
        cos.pack()            
        
    def create_windows(self):
        x = 0
        self.window_frame = tk.Frame(self,bg='#425362')
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                front_window = tk.Label(self.window_frame, 
                                      borderwidth=0, 
                                      width=2,
                                      height=2
                                      )
                if x % 6 == 0:
                    front_window.grid(row=row, 
                                    column=column, 
                                    sticky='nsew',
                                    padx=3,
                                    pady=12
                                    )
                else:
                        front_window.grid(row=row, 
                                    column=column, 
                                    sticky='nsew',
                                    padx=3,
                                    pady=3
                                    )
                current_row.append(front_window)
            x += 1
            self.front_windows.append(current_row)


        
        #Setting weight for the rest
        for row in range(5,self.rows+5):
            self.window_frame.rowconfigure(row, weight=1)
        for column in range(0,self.rows):
            self.window_frame.columnconfigure(row, weight=1)
    
    def grid_layout(self):
        
        self.top_left.grid(row=0,column=0,rowspan=max(2,int(self.rows/3)),columnspan=max(2,int(self.columns/3))+self.columns,sticky='news')
        self.top_top.grid(row=0,column=max(2,int(self.columns/3)),rowspan=max(2,int(self.rows/3)),columnspan=self.columns,sticky='news')
        self.window_frame.grid(row=max(2,int(self.rows/3)),column=max(2,int(self.columns/3)),rowspan=self.rows,columnspan=self.columns,sticky='news')
        self.left_side.grid(row=max(2,int(self.rows/3)),column=0,rowspan=self.rows,columnspan=max(2,int(self.columns/3)),sticky='news')
        
        for x in range(max(2,int(self.rows/3))):
            self.rowconfigure(x, weight=1)
        for x in range(max(2,int(self.rows/3),self.rows+max(2,int(self.rows/3)))):
            self.rowconfigure(x, weight=2)
        for y in range(max(2,int(self.columns/3))):
            self.columnconfigure(y, weight=1)
        for y in range(max(2,int(self.rows/3),self.columns+max(2,int(self.columns/3)))):
            self.columnconfigure(y, weight=2)
            
    def fill_windows(self):
        for x in range(0,self.rows):
                for y in range(0,self.columns):
                    self.front_windows[x][y].config(bg='yellow')
        for x in range(0,self.rows):
                for y in range(0,int(self.columns/2)):
                    self.left_windows[x][y].config(bg='blue')
 
              
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = B_ProgressBar()
        self.frame.pack()


if __name__ == "__main__": 
    app = Application()
    app.mainloop()  
        
    