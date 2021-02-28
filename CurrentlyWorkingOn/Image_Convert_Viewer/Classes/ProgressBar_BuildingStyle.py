#TODO: Do some math to make building modular or make whole building Canvas.
#TODO: Grid Layout - CodeClean
#TODO: How_many_windows() - Try to use __init__ lists.

import tkinter as tk
from tkinter import font
from tkinter import *
import random
from math import floor, ceil
from PIL import Image, ImageTk

                #   Walls Colors       /        Window Lights
window_lights = [['#425362','#394956'],['#64a4a3','#629aae','#4170a3','#487181']]
roof_lights = ['#c62633','#b52834','#9d2831','#88232b']
star_colors = ['#8C8CA8','#9393A8','#B0B0C4','#2f353b']

class B_ProgressBar(tk.Frame):
    '''
    Class to create a graphic ProgressBar with high building theme.
    Instead of a bar, here windows with lights on will represent status.
    ........

    Methods
    ----------
    create_left()
        Creates left side of the building with its windows.
    create_top()
        Creates roof, sky and stars in canvas.
    create_front()
        Creates front of the building with its windows.
    grid_layout()
        Creates grid system for create_left(),create_top() and crate_front().
    change_stars()
        Changes colors of stars in create_top tk.Canvas.
    change_roof_lights()
        Changes colors of lights on the roof in create_top tk.Canvas.
    fill_windows()
        Fills randomly windows in create_left() and create_top() with random colors from a list.
    how_many_windows()
        Stores info how many windows are in the building.
    loading_windows()
        Randomly adds lights in create_left() and create_top() windows with random colors from a list until 100%.
    '''

    def __init__(self,parent=None,rows=15,columns=12):
        '''
        Arguments:
        ------------
        parent:
            Set a parent to the Building ProgressBar
        rows (int):
            Number of window rows
        columns (int):
            Number of windows per row
        ------------
        Recommended columns=12. Modular building still in work.
        '''

        self.rows = rows
        self.columns = columns
        
        #Create_Top Canvas Parameters
        self.canv_width = max(378,int(self.columns*29.5)) 
        self.canv_height = 140

        self.w_percent = '0 %'      #Percentage info for user displayed on roof
        self.num = 0                #Counter for filled windows
        
        #Lists of created windows
        self.front_windows = []
        self.left_windows = []
        
        #Creating Layout
        tk.Frame.__init__(self,parent,bg='#c7cfb7')
        self.create_top()
        self.create_front()
        self.create_left()
        self.grid_layout()
        
        #Functions
        #self.fill_windows()
        self.change_roof_lights()
        self.change_stars()
        self.how_many_windows()
        self.loading_windows()

    #Layout Funcs
    def create_front(self):
        '''
        Creates front of the building with turned off windows.
        ''' 
        self.window_frame = tk.Frame(self,bg='#425362')
        
        x = 0   #Counter for rows to divide window sections.
        #Creating windows using labels.
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                front_window = tk.Label(self.window_frame, 
                                      borderwidth=0, 
                                      width=2,
                                      height=1
                                      )
                if x % 6 == 0:                              #Window Section
                    front_window.grid(row=row, 
                                    column=column, 
                                    sticky='nsew',
                                    padx=4,
                                    pady=16
                                    )
                else:                                       #Normal windows
                        front_window.grid(row=row, 
                                    column=column, 
                                    sticky='nsew',
                                    padx=4,
                                    pady=4
                                    )
                current_row.append(front_window)
            x += 1
            self.front_windows.append(current_row)           #Adding lists of columns per row to Left_Windows list.
                                                             #[row1,row2,row3...] row1 = [column1,column2,column3] etc
        del current_row
        
    def create_left(self):
        '''
        Creates left side of the building with turned off windows.
        ''' 
        self.left_side = tk.Frame(self,bg='#394956',bd=0)
        
        x = 0   #Counter for rows to divide window sections.
        #Creating windows using labels.
        for row in range(self.rows):
            current_row = []
            for column in range(int(self.columns/2)+1):
                left_window = tk.Label(self.left_side, 
                                      borderwidth=0, 
                                      width=1,
                                      height=1
                                      )
                if x % 6 == 0:                               #Window Section
                   left_window.grid(row=row, 
                                    column=column, 
                                    sticky='nsew',
                                    padx=1,
                                    pady=16
                                    )
                else:                                        #Normal windows
                        left_window.grid(row=row, 
                                    column=column, 
                                    sticky='nsew',
                                    padx=1,
                                    pady=4
                                    )
                current_row.append(left_window)
            x += 1
            self.left_windows.append(current_row)            #Adding lists of columns per row to Left_Windows list.
                                                             #[row1,row2,row3...] row1 = [column1,column2,column3] etc.
        del current_row
    def create_top(self):
        '''
        Creates canvas on top of the building.
        Draws roof, sky and stars in canvas.
        '''
        self.top = tk.Frame(self,bg='#c7cfb7')
        self.top_roof = tk.Canvas(self.top,bg='#232453',bd=-2,height=self.canv_height,width=self.canv_width)
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
        self.stars = []     #Creating List of stars for change_stars.
        for num in range(10):
            s = random.randint(1,3) #Random size of star
            x = random.randint(0+s,self.canv_width-s) #Random horizontal cords for star
            y = random.randint(0+s,40-s) #Random vertical cords for star
            #Create star based on its size and cords
            self.stars.append(self.top_roof.create_oval(x-s,y-s,x+s,y+s,fill='#7F7F9E',outline='')) 
        
        #Percentage Variable
        self.prcntlightwindow = self.top_roof.create_text(int(self.canv_width*10/19)-15,85,text=self.w_percent,fill='#64a4a3',font=('Helvetica',max(16,int(self.columns*1.4)),'bold'))

    def grid_layout(self):
        '''
        Creates grid system for create_left(),create_top() and crate_front().
        Trying to make create_left as small as possible for 3d effect.
        '''
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
    
    #Active Funcs            
    def change_stars(self):
        '''
        Changes colors of stars in create_top tk.Canvas based on star_colors list.
        '''
        numstars = random.randint(1,len(self.stars))    #How many stars to change
        for x in range(numstars):
            #Changes color - Might change same star couple of times.
            self.top_roof.itemconfig(self.stars[random.randint(0,numstars-x-1)],fill=star_colors[random.randint(0,3)]) 
        self.after(2000,self.change_stars)       
        
    def change_roof_lights(self):
        '''
        Changes colors of lights on the roof in create_top tk.Canvas based on roof_lights list.
        '''
        lightslist = [self.rd1,self.rd2,self.rd3,self.rd4,self.rd5,self.rd6] #Create list of all avaiable lights
        numlights = random.randint(1,6)                                      #How many lights to change
        for x in range(numlights):
            whichlight = random.randint(0,numlights-x-1)
            #Changes color - Then removes light from list to avoid same light changing.
            self.top_roof.itemconfig(lightslist[whichlight],fill=roof_lights[random.randint(0,3)])
            lightslist.pop(whichlight)
        self.after(1000,self.change_roof_lights)    
  
    def fill_windows(self):
        '''
        Restarts and fills randomly windows in create_left() and create_top() 
        with random colors from a window_lights list. 
        Around 50% of windows will be turned off, the rest will be turned on.
        Function mostly for animation.
        '''
        empty_windows = 0
        turned_on_windows = 0        #Counter to count % of turned on windows
        #Configuring All Front Windows 
        for x in range(0,self.rows):
                for y in range(0,self.columns):
                    turnedoff = random.randint(0,1) #For 0 turned off/For 1 turned on
                    if turnedoff:
                        self.front_windows[x][y].config(bg=window_lights[1][random.randint(0,3)])
                        turned_on_windows += 1
                    else:
                        self.front_windows[x][y].config(bg=window_lights[0][0])
                        empty_windows += 1
        #Configuring All Left Windows 
        for x in range(0,self.rows):
                for y in range(0,int(self.columns/2)+1):
                    if y == int(self.columns/2) or y == 0: #First and last columns turn off for 3d effect.
                        self.left_windows[x][y].config(bg=window_lights[0][1])
                    else:
                        turnedoff = random.randint(0,1) #For 0 turned off/For 1 turned on
                        if turnedoff:
                            self.left_windows[x][y].config(bg=window_lights[1][random.randint(0,3)])
                            turned_on_windows += 1
                        else:
                            self.left_windows[x][y].config(bg=window_lights[0][1])
                            empty_windows += 1
        
        #Percentage of turned on windows then input it onto top_create() Canvas.
        self.w_percent = f'{str(round(turned_on_windows*100/(turned_on_windows+empty_windows),2))} %'
        self.top_roof.itemconfig(self.prcntlightwindow,text=self.w_percent)
        
        self.after(2000,self.fill_windows)      
              
    def how_many_windows(self):
        '''
        Stores info how many windows are in the building and makes:
        List = [[left_list],[front_list]]
        '''
        self.front_totallist = []
        self.left_totallist = []
        
        #Adds growing integer per window in create_front() to list
        for x in range(self.rows*self.columns):
            self.front_totallist.append(x)
        self.front_leng = len(self.front_totallist)
        
        #Adds growing integer per window in left_front() to list
        for x in range(self.rows*(int(self.columns/2)+1)):
            self.left_totallist.append(x)
        self.left_leng = len(self.left_totallist)
        
        self.num_windows = self.front_leng+self.left_leng                   #Window amount
        self.both_totallist = [self.left_totallist,self.front_totallist]    #Connecting lists
        
    def loading_windows(self):
        '''
        Randomly adds lights in create_left() and create_top() windows 
        with random colors from a list until all windows are filled. 
        Returns also percentage of filled windows.
        Takes list filled with integers from 0 to ... and counts postion of window
        by dividing integer with columns argument. 
        For Example:
        Int = 123, self.rows = 16, self.columns = 16
        Floor [ceil(123/self.columns)] = 7 Floor from up
        Column [123%self.columns] = 12
        Window[7][12]
        '''
        
        #Abstract variable of amount windows to be filled for self running.
        x = min(random.randint(0,10),(max(len(self.both_totallist[0]),len(self.both_totallist[1]),1))) 
        self.num += x       #Counter of filled windows for percentage equation
        for window in range(x):
            
            #Fill windows for left_side and front windows at the same cycle.
            if self.both_totallist[0] != [] and self.both_totallist[1] != []:
                whichside = random.randint(0,1) #0 for left/1 for front. 
                #For List[1] (Front)
                if whichside:
                    _w = random.choice(self.both_totallist[whichside])   #Choosing window stored as integer
                    _f = floor(_w/self.columns)                          #Calculate floor(row)
                    _c = _w%self.columns                                 #Calculate column
                    
                    #Turning light on and removing window from the turned off lights list.
                    self.front_windows[_f][_c].config(bg=window_lights[1][random.randint(0,3)])
                    self.both_totallist[whichside].pop(self.both_totallist[whichside].index(_w))
                    
                #For List[0] (Left)    
                else:
                    _w = random.choice(self.both_totallist[whichside])   #Choosing window stored as integer
                    _f = floor(_w/(ceil(self.columns/2)+1))              #Calculate floor(row)
                    _c = _w%(ceil(self.columns/2)+1)                     #Calculate column
                    
                    #Turning light on and removing window from the turned off lights list.
                    self.left_windows[_f][_c].config(bg=window_lights[1][random.randint(0,3)])
                    self.both_totallist[whichside].pop(self.both_totallist[whichside].index(_w))
            
            #For all front windows filled with lights continue turning on lights on left side.        
            elif self.both_totallist[0] != []:
                _w = random.choice(self.both_totallist[0])               #Choosing window stored as integer
                _f = floor(_w/(ceil(self.columns/2)+1))                  #Calculate floor(row)
                _c = _w%(ceil(self.columns/2)+1)                         #Calculate column
                
                #Turning light on and removing window from the turned off lights list.
                self.left_windows[_f][_c].config(bg=window_lights[0][random.randint(0,3)])
                self.both_totallist[0].pop(self.both_totallist[0].index(_w))
                
            #For all left windows filled with lights continue turning on lights on front. 
            elif self.both_totallist[1] != []:
                _w = random.choice(self.both_totallist[1])               #Choosing window stored as integer
                _f = floor(_w/self.columns)                              #Calculate floor(row)
                _c = _w%self.columns                                     #Calculate column
                
                #Turning light on and removing window from the turned off lights list.
                self.front_windows[_f][_c].config(bg=window_lights[1][random.randint(0,3)])
                self.both_totallist[1].pop(self.both_totallist[1].index(_w))
            else:
                pass
            
        #Storing percentage of filled windows then updating it onto top_create() Canvas.
        self.w_percent = f'{str(round(self.num/(self.num_windows)*100,2))} %'   
        self.top_roof.itemconfig(self.prcntlightwindow,text=self.w_percent)
        
        #Check if all windows filled to stop refreshing
        if self.both_totallist[0] == [] and self.both_totallist[1] == []:
            self.after_cancel(self.loading_windows)
        else:
            self.after(500,self.loading_windows)
            
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = B_ProgressBar()
        self.frame.pack()


if __name__ == "__main__": 
    app = Application()
    app.mainloop()  
        
    