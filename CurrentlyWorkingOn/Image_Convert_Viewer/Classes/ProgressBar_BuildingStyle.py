#TODO: Do some math to make building modular.
#TODO: Documentation
#TODO: Clean Code
#TODO: Connect left windows with front windows for percentage.
#TODO: Maybe add some area around with other buildings for 1280x1024 window screen.
#TODO: Not important but maybe make whole screen canvas and pain there if time avaiable.

import tkinter as tk
from tkinter import font
from tkinter import *
import random
from math import floor
from PIL import Image, ImageTk

window_lights = [['#425362','#394956'],['#64a4a3','#629aae','#4170a3','#487181']]
roof_lights = ['#c62633','#b52834','#9d2831','#88232b']
star_colors = ['#8C8CA8','#9393A8','#B0B0C4','#2f353b']

class B_ProgressBar(tk.Frame):

    def __init__(self,parent=None,rows=15,columns=12):

        self.rows = rows
        self.columns = columns
        self.canv_width = max(378,int(self.columns*29.5))
        self.canv_height = 140
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
        #self.fill_windows()
        #self.change_roof_lights()
        #self.change_stars()
        self.loading()
        self.loading_windows()
        
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
                                    pady=16
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
        self.top_roof = tk.Canvas(self.top,bg='#232453',bd=-2,height=self.canv_height,)#width=self.canv_width) 
        self.top_roof.pack(fill=BOTH,expand=YES)
        
    #Roof
        #Most Top/Behind Part
        self.top_roof.create_rectangle(int(self.canv_width*2/19),40,int(self.canv_width*12/19),self.canv_height,fill='#2f353b',outline='')
        self.top_roof.create_polygon([int(self.canv_width*12/19),40,self.canv_width,90,int(self.canv_width*12/19),90],fill='#2f353b',outline='')  
        self.top_roof.create_rectangle(int(self.canv_width*12/19),90,self.canv_width,self.canv_height,fill='#2f353b',outline='')  
        
        #Middle Top Part 
        self.top_roof.create_rectangle(int(self.canv_width*4/19),50,int(self.canv_width*16/19),self.canv_height,fill='#394550',outline='')
        
        #Middle-Left Top Part
        self.top_roof.create_rectangle(5,50,int(self.canv_width*4/19),self.canv_height,fill='#364048',outline='')
        
        #Front-Left Top Part
        self.top_roof.create_rectangle(int(self.canv_width*1/19),95,int(self.canv_width*4/19)+11,self.canv_height,fill='#394956',outline='')
        self.top_roof.create_rectangle(10,115,int(self.canv_width*1/19),self.canv_height,fill='#394956',outline='')
        
        #Front Top Part
        self.top_roof.create_rectangle(int(self.canv_width*4/19)+11,95,int(self.canv_width*12/19),self.canv_height,fill='#425362',outline='')
        self.top_roof.create_rectangle(int(self.canv_width*12/19),115,int(self.canv_width*18/19),self.canv_height,fill='#425362',outline='')       
        
        #Bottom Line
        self.top_roof.create_line(0,self.canv_height-1,10,self.canv_height-1,fill='#2f353b')
        self.top_roof.create_line(10,self.canv_height-1,10,115,fill='#2f353b')
        self.top_roof.create_line(10,115,int(self.canv_width*1/19),115,fill='#2f353b')
        self.top_roof.create_line(int(self.canv_width*1/19),115,int(self.canv_width*1/19),95,fill='#2f353b')
        self.top_roof.create_line(int(self.canv_width*1/19),95,int(self.canv_width*12/19),95,fill='#2f353b')
        self.top_roof.create_line(int(self.canv_width*12/19),95,int(self.canv_width*12/19),115,fill='#2f353b')
        self.top_roof.create_line(int(self.canv_width*12/19),115,int(self.canv_width*18/19),115,fill='#2f353b')
        self.top_roof.create_line(int(self.canv_width*18/19),115,int(self.canv_width*18/19),self.canv_height,fill='#2f353b')
        self.top_roof.create_line(int(self.canv_width*18/19),self.canv_height,self.canv_width,self.canv_width,fill='#2f353b')
        
        #Roof Lights
        self.rd1 = self.top_roof.create_oval(int(self.canv_width*1/19)-2,93,int(self.canv_width*1/19)+2,97,fill='#c62653',outline='')      
        self.rd2 = self.top_roof.create_oval(int(self.canv_width*4/19)+8,92,int(self.canv_width*4/19)+13,98,fill='#c62653',outline='')  
        self.rd3 = self.top_roof.create_oval(int(self.canv_width*16/19)-3,47,int(self.canv_width*16/19)+2,53,fill='#c62653',outline='')  
        self.rd4 = self.top_roof.create_oval(4,48,8,52,fill='#c62653',outline='') 
        self.rd5 = self.top_roof.create_oval(int(self.canv_width*4/19)-3,47,int(self.canv_width*4/19)+3,53,fill='#c62653',outline='')
        self.rd6 = self.top_roof.create_oval(int(self.canv_width*12/19)-3,92,int(self.canv_width*12/19)+1,98,fill='#c62653',outline='') 
        
        #Stars
        self.stars = []
        for z in range(10):
            s = random.randint(1,3)
            x = random.randint(0+s,self.canv_width-s)
            y = random.randint(0+s,40-s)
            self.stars.append(self.top_roof.create_oval(x-s,y-s,x+s,y+s,fill='#7F7F9E',outline='#8C8CA8'))
        
        #Percentage Variable
        self.prcntlightwindow = self.top_roof.create_text(int(self.canv_width*10/19)-15,85,text=self.w_percent,fill='#64a4a3',font=('Helvetica',max(16,int(self.columns*1.4)),'bold'))
    
    def change_stars(self):
        
        numstars = random.randint(1,len(self.stars))
        for x in range(numstars):
            self.top_roof.itemconfig(self.stars[random.randint(0,numstars-x-1)],fill=star_colors[random.randint(0,3)])
        self.after(1000,self.change_roof_lights)
        
    def change_roof_lights(self):
        
        lightslist = [self.rd1,self.rd2,self.rd3,self.rd4,self.rd5,self.rd6]
        numlights = random.randint(1,6)
        for x in range(numlights):
            whichlight = random.randint(0,numlights-x-1)
            self.top_roof.itemconfig(lightslist[whichlight],fill=roof_lights[random.randint(0,3)])
            lightslist.pop(whichlight)
        self.after(1000,self.change_roof_lights)

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
                                    pady=16
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
        
    def edit_left_window(self,row,column):
        self.left_windows[row][column].config(bg='#8FB9BA')
        
    def edit_front_window(self,row,column):
        self.front_windows[row][column].config(bg='#8FB9BA')
        
    def loading(self):
        
        self.totallist = []
        
        for x in range(self.rows*self.columns):
            self.totallist.append(x)
        self.leng = len(self.totallist)
    def loading_windows(self):
        
        x = min(random.randint(0,10),len(self.totallist)-1)
        for y in range(x+1):
            
            z = random.choice(self.totallist)
            print(z, floor(z/self.columns), z%self.columns)
            _f = floor(z/self.columns)
            _c = z%self.columns
            
            self.front_windows[_f][_c].config(bg=window_lights[1][random.randint(0,3)])
            self.totallist.pop(self.totallist.index(z))
            self.w_percent = f'{str(round(((self.leng-len(self.totallist))/self.leng)*100,2))} %'
        if self.totallist == []:
            self.after_cancel(self.loading_windows)
        self.top_roof.itemconfig(self.prcntlightwindow,text=self.w_percent)
        self.after(500,self.loading_windows)
            

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = B_ProgressBar()
        self.frame.pack()


if __name__ == "__main__": 
    app = Application()
    app.mainloop()  
        
    