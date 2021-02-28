import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk

window_lights = [['#425362','#394956'],['#64a4a3','#629aae','#4170a3','#487181']]
roof_lights = ['#c62633','#b52834','#9d2831','#88232b']

class B_ProgressBar(tk.Frame):

    def __init__(self,parent=None,rows=15,columns=14):

        self.rows = rows
        self.columns = columns
        self.canv_width = max(378,int(self.columns*29.5))
        self.canv_height = 100
        self.bdpx = 1
        self._padx = 1
        self.w_percent = '0 %'
        
        tk.Frame.__init__(self,parent,bg='#c7cfb7')
        self.pack()
        self.front_windows = []
        self.left_windows = []
        
        self.create_top()
        self.create_windows()
        self.create_left()
        self.grid_layout()
        self.fill_windows()
        self.change_air_color()
        
    def create_left(self):
        
        self.left_side = tk.Frame(self,bg='#394956',bd=0)
        x = 0
        for row in range(self.rows):
            current_row = []
            for column in range(int(self.columns/2)):
                left_window = tk.Label(self.left_side, 
                                      borderwidth=0, 
                                      width=1,
                                      height=1
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
                                    pady=4
                                    )
                current_row.append(left_window)
            x += 1
            self.left_windows.append(current_row)
        
    def create_top(self):
        
        self.top = tk.Frame(self,bg='#c7cfb7')
        self.top_roof = tk.Canvas(self.top,bg='black',bd=-2,height=self.canv_height,)#width=self.canv_width) 
        self.top_roof.pack(fill=BOTH,expand=YES)
        
        
        self.top_roof.create_rectangle(0,55,int(self.canv_width*3/19),self.canv_height,fill='#3f515f',outline='')
        self.top_roof.create_rectangle(int(self.canv_width*3/19),55,int(self.canv_width*11/19),self.canv_height,fill='#475868',outline='')
        self.top_roof.create_rectangle(int(self.canv_width*11/19),75,self.canv_width,self.canv_height,fill='#475868',outline='')
        self.top_roof.create_rectangle(5,10,int(self.canv_width*4/19),55,fill='#364048',outline='')
        self.top_roof.create_rectangle(int(self.canv_width*4/19),10,int(self.canv_width*14/19),55,fill='#394550',outline='')
        
        self.top_roof.create_rectangle(int(self.canv_width*9/19),55,int(self.canv_width*14/19),self.canv_height,fill='#394550',outline='') 
        self.top_roof.create_rectangle(int(self.canv_width*14/19),50,self.canv_width,self.canv_height,fill='#394550',outline='') 
        self.top_roof.create_polygon([int(self.canv_width*14/19),10,self.canv_width,50,int(self.canv_width*14/19),50],fill='#394550',outline='') 
        self.top_roof.create_rectangle(int(self.canv_width*2/19),0,int(self.canv_width*12/19),10,fill='#2f353b',outline='')   
                  
        self.top_roof.create_line(int(self.canv_width*14/19),10,int(self.canv_width*14/19),self.canv_height,fill='#2f353b')
        self.top_roof.create_rectangle(int(self.canv_width*9/19),75,int(self.canv_width*16/19),self.canv_height,fill='#475868',outline='')
        self.top_roof.create_line(0,self.canv_height-1,self.canv_width,self.canv_height-1,fill='#2f353b')
        self.top_roof.create_line(int(self.canv_width*3/19),55,int(self.canv_width*3/19),self.canv_height,fill='#2f353b')
        
        self.rd1 = self.top_roof.create_oval(0,53,4,57,fill='#c62653',outline='')      
        self.rd2 = self.top_roof.create_oval(int(self.canv_width*3/19)-3,52,int(self.canv_width*3/19)+3,58,fill='#c62653',outline='')  
        self.rd3 = self.top_roof.create_oval(int(self.canv_width*14/19)-3,7,int(self.canv_width*14/19)+3,13,fill='#c62653',outline='')  
        self.rd4 = self.top_roof.create_oval(4,8,8,12,fill='#c62653',outline='') 
        self.rd5 = self.top_roof.create_oval(int(self.canv_width*4/19)-3,7,int(self.canv_width*4/19)+3,13,fill='#c62653',outline='')
        
        self.prcntlightwindow = self.top_roof.create_text(int(self.canv_width*11/19),45,text=self.w_percent,fill='#64a4a3')
        
    def change_air_color(self):
        
        lightslist = [self.rd1,self.rd2,self.rd3,self.rd4,self.rd5]
        numlights = random.randint(0,5)
        chcklist = []
        for x in range(numlights):
            self.top_roof.itemconfig(lightslist[random.randint(0,numlights-x-1)],fill=roof_lights[random.randint(0,3)])
        self.after(1000,self.change_air_color)

    def create_windows(self):
        x = 0
        self.window_frame = tk.Frame(self,bg='#425362')
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                front_window = tk.Label(self.window_frame, 
                                      borderwidth=0, 
                                      width=2,
                                      height=1
                                      )
                if x % 6 == 0:
                    front_window.grid(row=row, 
                                    column=column, 
                                    sticky='nsew',
                                    padx=4,
                                    pady=12
                                    )
                else:
                        front_window.grid(row=row, 
                                    column=column, 
                                    sticky='nsew',
                                    padx=4,
                                    pady=4
                                    )
                current_row.append(front_window)
            x += 1
            self.front_windows.append(current_row)


        
        #Setting weight for the rest
        for row in range(5,self.rows):
            self.window_frame.rowconfigure(row, weight=1)
        for column in range(0,self.rows):
            self.window_frame.columnconfigure(row, weight=1)
    
    def grid_layout(self):
        
        self.top.grid(row=0,column=0,rowspan=max(2,int(self.rows/3)),columnspan=max(2,int(self.columns/3))+self.columns,sticky='news')
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
        emptywindows = 0
        for x in range(0,self.rows):
                for y in range(0,self.columns):
                    turnedoff = random.randint(0,1)
                    if turnedoff:
                        self.front_windows[x][y].config(bg=window_lights[1][random.randint(0,3)])
                    else:
                        self.front_windows[x][y].config(bg=window_lights[0][0])
                        emptywindows += 1
        for x in range(0,self.rows):
                for y in range(0,int(self.columns/2)):
                    if y == (self.columns/2)-1 or y == 0:
                        self.left_windows[x][y].config(bg=window_lights[0][1])
                    else:
                        turnedoff = random.randint(0,1)
                        if turnedoff:
                            self.left_windows[x][y].config(bg=window_lights[1][random.randint(0,3)])
                        else:
                            self.left_windows[x][y].config(bg=window_lights[0][1])
                            emptywindows += 1
        
        self.w_percent = f'{str(round(emptywindows/(((self.rows*int(self.columns*3/2)))-self.rows*2)*100,2))} %'
        print(self.w_percent)
        self.top_roof.itemconfig(self.prcntlightwindow,text=self.w_percent)
        self.after(500,self.fill_windows)
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = B_ProgressBar()
        self.frame.pack()


if __name__ == "__main__": 
    app = Application()
    app.mainloop()  
        
    