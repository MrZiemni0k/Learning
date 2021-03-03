import tkinter as tk
from tkinter import messagebox
import random

#TODO: Documentation Test_building and Basic_stuff
#TODO: Add tries and hide fp_text button
#TODO: Delete fptext when setting new cord or adding new cord to focus

class Test_Building(tk.Frame):
    def __init__(self,parent=None,canv_width=1000,canv_height=700):
        
        tk.Frame.__init__(self,parent)
        
        #Canvas Size
        self.canv_width = canv_width
        self.canv_height = canv_height
        
        #Point of focus
        self.focus_point = tuple([int(self.canv_width/2),int(self.canv_height*7/10)])
        
        #Perspective points
        self.left_2point = tuple([0,self.canv_height*3/10])
        self.right_2point = tuple([self.canv_width,self.canv_height*3/10])
        
        #Lists to store info about canvas objects for editing/deleting
        self.store_horizontal_var = []
        self.store_fpoints = []
        self.store_perspective_lines = []
        self.store_line_var = []
        
        #Layout
        self.create_top_panel()
        self.create_sub_panel()
        self.create_canvas()
        

    def create_top_panel(self):
        '''
        Creates top panel with buttons directing to different sub panels.
        ''' 
        #Panel
        self.top_panel = tk.Frame(self,bg='#425362')
        self.top_panel.grid(row=0,column=0,sticky='news')
        
        #Button to basic functions subpanel 
        self.basic_button = tk.Button(self.top_panel,text='Basic',command=lambda: self.show_subpanel(Basic_Stuff))
        self.basic_button.pack(side='left')
        #Button to geometry building subpanel
        self.geometry_button = tk.Button(self.top_panel,text='Geometry',command=lambda: self.show_subpanel(Other_Stuff))
        self.geometry_button.pack(side='left')
        
        #Clear Canvas button
        self.clear_button = tk.Button(self.top_panel,text='Clear',command=lambda: self.canvas.delete('all'))
        self.clear_button.pack(side='right')      
        
    def create_sub_panel(self):
        '''
        Sub_Panel for easier navigating
        '''
        #Sub Panel
        self.sub_panel = tk.Frame(self)
        self.sub_panel.grid(row=1,column=0,sticky='news')
        
        #Empty Dict for subpanels(frames)
        self.subpanels = {}
        
        #Store all sub panels and lay them on top of eachother.
        for F in (Basic_Stuff, Other_Stuff):
            subpanel = F(self.sub_panel, self)
            self.subpanels[F] = subpanel
            subpanel.grid(row = 0, column = 0, sticky = "nsew")
        
        #Show first sub panel at the start
        self.show_subpanel(Basic_Stuff)
    
    def show_subpanel(self, stored):
        '''
        Changes frame depending on button click
        '''
        self.showsubpanel = self.subpanels[stored]
        self.showsubpanel.tkraise()
        
    def create_canvas(self):
        '''
        Creates canvas for drawing
        '''
        self.canvas = tk.Canvas(self,bg='#232453',bd=-2,
                                height=self.canv_height,width=self.canv_width)
        self.canvas.grid(row=2,column=0,sticky='news')
        
    def viewer_point(self):
        '''
        Chooses randomly focus point of view
        '''
        #Restart(Clear) Viewer_Point
        if self.store_fpoints:
            for _ in self.store_fpoints:
                self.canvas.delete(_)
            self.store_fpoints = []
        
        #Cords
        self.focus_point = tuple([random.randint(self.left_2point[0],self.right_2point[0]),random.randint(0,self.canv_height)])

        #Visualisation
        fp_text = self.canvas.create_text(self.focus_point,text=f'{self.focus_point}',fill='white')
        
        #List of Visualisation variables to clear them in canvas if function reused.
        self.store_fpoints = [fp_text]
    
    def horizontal_points(self):
        '''
        Chooses randomly flat horizontal points for 2 point perspective drawing.
        '''
        #Restart(Clear) Horizonta_Points
        if self.store_horizontal_var:
            for _ in self.store_horizontal_var:
                self.canvas.delete(_)
            for _ in self.store_perspective_lines:
                self.canvas.delete(_)
            self.store_horizontal_var = []
            self.store_perspective_lines = []
        #Cords    
        cord_horizontal_line = random.randint(0,self.canv_height)
        self.left_2point = tuple([random.randint(0,self.focus_point[0]),cord_horizontal_line])
        self.right_2point = tuple([random.randint(self.focus_point[0],self.canv_width),cord_horizontal_line])
        
        #Visualisation
        draw_horizontal_line = self.canvas.create_line(0,cord_horizontal_line,self.canv_width,cord_horizontal_line,fill="black")
        l2p_text = self.canvas.create_text(self.left_2point,text=f'{self.left_2point}',fill='white')
        r2p_text = self.canvas.create_text(self.right_2point,text=f'{self.right_2point}',fill='white')
        
        #List of Visualisation variables to clear them in canvas if function reused.
        self.store_horizontal_var = [draw_horizontal_line, l2p_text, r2p_text]
    
    def perspective_lines(self,pointcross,todel=False):
        '''
        Paints perspiective lines based on Horizontal and Center Points.
        '''
        
        #Delete Perspective Lines
        if todel and self.store_perspective_lines:
            for _ in self.store_perspective_lines:
                self.canvas.delete(_)
            self.store_perspective_lines = []
        
        #First Perspective Line
        p1_line = StraightLine(self.left_2point,pointcross)
        
        #Calculate x cords for canvas borders
        x_start = p1_line.math_x_crosspoint(0)
        x_end = p1_line.math_x_crosspoint(self.canv_height)
        
        #Draw Perspective Line
        left_line = self.canvas.create_line(x_start,0,x_end,self.canv_height,fill="#4a4646")
        
        #Second Perspective Line
        p2_line = StraightLine(self.right_2point,pointcross)
        
        #Calculate x cords for canvas borders
        x_start = p2_line.math_x_crosspoint(self.canv_height)
        x_end = p2_line.math_x_crosspoint(0)
        
        #Draw Perspective Line
        right_line = self.canvas.create_line(x_start,self.canv_height,x_end,0,fill="#4a4646")
        
        #Store canvas lines in list for deleting/editing
        self.store_perspective_lines.append(left_line)
        self.store_perspective_lines.append(right_line)
    
    def dellast_persplines(self):
        '''
        Deletes last 2 drawn perspective lines
        '''       
        for _ in range(2):
            try:
                self.canvas.delete(self.store_perspective_lines[-1])
                del self.store_perspective_lines[-1]
            except:
                print("No perspective lines to delete. List is empty.")
                
    def focus_addcords(self,todel=False):
        
        #Delete all focus points.
        if self.store_fpoints and todel:
            for _ in self.store_fpoints:
                self.canvas.delete(_)
            self.store_fpoints = []
        try:
                   
            #Setting new cords and marking with cord texts    
            self.focus_point = tuple([self.focus_point[0]+int(self.showsubpanel.focus_setx.get()),self.focus_point[1]+int(self.showsubpanel.focus_sety.get())])
            fp_text = self.canvas.create_text(self.focus_point,text=f'{self.focus_point}',fill='white')            
            
            #Storing canvas object for edit/delete.
            self.store_fpoints.append(fp_text)
    
        except:
            tk.messagebox.showerror(title='Error', message='One or more "Focus" entry boxes\nare empty or wrong input.\nPlease pass an integer.')
            
    def focus_setcords(self,todel=False):
        #Delete all focus points.
        if self.store_fpoints and todel:
            for _ in self.store_fpoints:
                self.canvas.delete(_)
            self.store_fpoints = []
        
        #Setting new cords and marking with cord texts
        try:
            self.focus_point = tuple([int(self.showsubpanel.focus_setx.get()),int(self.showsubpanel.focus_sety.get())])
            fp_text = self.canvas.create_text(self.focus_point,text=f'{self.focus_point}',fill='white')
            
            #Storing canvas object for edit/delete.
            self.store_fpoints.append(fp_text)
        except:
            tk.messagebox.showerror(title='Error', message='One or more "Focus" entry boxes\nare empty or wrong input.\nPlease pass an integer.')
    def horizontal_setcords(self):
        
        #Restart(Clear) Vanishing_Points
        if self.store_horizontal_var:
            for _ in self.store_horizontal_var:
                self.canvas.delete(_)
            for _ in self.store_perspective_lines:
                self.canvas.delete(_)
            self.store_horizontal_var = []
            self.store_perspective_lines = []
        #Cords 
        try:   
            self.left_2point = tuple([int(self.showsubpanel.horizontal_setx1.get()),int(self.showsubpanel.horizontal_sety.get())])
            self.right_2point = tuple([int(self.showsubpanel.horizontal_setx2.get()),int(self.showsubpanel.horizontal_sety.get())])
            #Visualisation
            draw_horizontal_line = self.canvas.create_line(0,int(self.left_2point[1]),self.canv_width,self.left_2point[1],fill="black")
            l2p_text = self.canvas.create_text(self.left_2point,text=f'{self.left_2point}',fill='white')
            r2p_text = self.canvas.create_text(self.right_2point,text=f'{self.right_2point}',fill='white')
            
            #List of Visualisation variables to clear them in canvas if function reused.
            self.store_horizontal_var = [draw_horizontal_line, l2p_text, r2p_text]
        except:
            tk.messagebox.showerror(title='Error', message='One or more "Horizontal" entry boxes\nare empty or wrong input.\nPlease pass an integer.')
        
    def draw_line(self,todel=False):
        
        if self.store_line_var and todel:
            for _ in self.store_fpoints:
                self.canvas.delete(_)
            self.store_line_var = []
        try:
            self.x1y1 = tuple([int(self.showsubpanel.draw_x1.get()),int(self.showsubpanel.draw_y1.get())])
            self.x2y2 = tuple([int(self.showsubpanel.draw_x2.get()),int(self.showsubpanel.draw_y2.get())])
            drawline = self.canvas.create_line(self.x1y1,self.x2y2,fill='black')
            
            fp_text = self.canvas.create_text(self.x1y1,text=f'{self.x1y1}',fill='white')
            self.store_fpoints.append(fp_text)
            fp_text = self.canvas.create_text(self.x2y2,text=f'{self.x2y2}',fill='white')
            self.store_fpoints.append(fp_text)
            
        except:
            tk.messagebox.showerror(title='Error', message='One or more "Line" entry boxes\nare empty or wrong input.\nPlease pass an integer.')  
        
        self.store_line_var.append(drawline)
        
    def dellast_drawline(self):
        '''
        Deletes last drawn line
        '''       
        try:
            self.canvas.delete(self.store_line_var[-1])
            del self.store_line_var[-1]
        except:
            print("There is nothing to delete from. List is empty.")
    
    def draw_line_basedonpersp(self,vanishpoint,crosspoint1,crosspoint2,singlecord):
        
        p_line1 = StraightLine(vanishpoint,crosspoint1)
        
        y1 = p_line1.math_y_crosspoint(singlecord)
        
        p_line2 = StraightLine(vanishpoint,crosspoint2)
        
        y2 = p_line2.math_y_crosspoint(singlecord)
        
        drawline = self.canvas.create_line(singlecord,y1,singlecord,y2,fill='black')
        
        self.store_line_var.append(drawline)
        
        #Visualisation
        fp_text = self.canvas.create_text(singlecord,y1,text=f'{singlecord,y1}',fill='white')
        self.store_fpoints.append(fp_text)
        
        fp_text = self.canvas.create_text(singlecord,y2,text=f'{singlecord,y2}',fill='white')
        self.store_fpoints.append(fp_text)
        
class Basic_Stuff(tk.Frame):
    '''
    Subpanel with basic functions called by buttons.
    '''
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)
        
        #Random Focus
        self.focus_button = tk.Button(self,text='Rand Focus Point',
                                      command=lambda: app.frame.viewer_point())
        self.focus_button.grid(row=0,column=0,sticky='news')
        
        #Random Horizontal
        self.horizontal_button = tk.Button(self,text='Rand Horizontal Points',
                                           command=lambda: app.frame.horizontal_points())
        self.horizontal_button.grid(row=1,column=0,sticky='news')
        
        #Draw and delete perspective lines
        self.plines_button = tk.Button(self,text='Draw Persp Lines',
                                       command=lambda: app.frame.perspective_lines(app.frame.focus_point))
        self.plines_button.grid(row=0,column=1,sticky='news')
        self.delplines_button = tk.Button(self,text='Del Last P Lines',
                                          command=lambda: app.frame.dellast_persplines())
        self.delplines_button.grid(row=1,column=1,sticky='news')    
        
        #X and Y info labels
        self.focusx_label = tk.Label(self,text='X')
        self.focusx_label.grid(row=0,column=2,sticky='news')
        self.focusy_label = tk.Label(self,text='Y')
        self.focusy_label.grid(row=1,column=2,sticky='news')
        
        #Frame for add focus point options
        self.addfocus_frame = tk.Frame(self,relief=tk.SUNKEN,bd=2)
        self.addfocus_frame.grid(row=0,column=3,rowspan=2,columnspan=2,sticky='news')
        
        #Options for adding/substracting x,y cords to focus point.
        self.focus_addx = tk.Entry(self.addfocus_frame,width=4)
        self.focus_addx.grid(row=0,column=0,sticky='news')
        self.focus_addx.insert(0,0)
        self.focus_addy = tk.Entry(self.addfocus_frame,width=4)
        self.focus_addy.grid(row=1,column=0,sticky='news')
        self.focus_addy.insert(0,0)
        self.focus_addbutton = tk.Button(self.addfocus_frame,text='F_Add',
                                         command=lambda: app.frame.focus_addcords())
        self.focus_addbutton.grid(row=0,column=1,rowspan=2,sticky='news')
        
        self.addfocus_frame.rowconfigure((0,1),weight=1)
        
        #Frame for setting x,y coors to focus point.
        self.setfocus_frame = tk.Frame(self,relief=tk.SUNKEN,bd=3)
        self.setfocus_frame.grid(row=0,column=5,rowspan=2,columnspan=2,sticky='news')
        
        #Options for setting x,y cords to focus point.
        self.focus_setx = tk.Entry(self.setfocus_frame,width=4)
        self.focus_setx.grid(row=0,column=0,sticky='news')
        self.focus_setx.insert(0,0)
        self.focus_sety = tk.Entry(self.setfocus_frame,width=4)
        self.focus_sety.grid(row=1,column=0,sticky='news')
        self.focus_sety.insert(0,0)
        self.focus_setbutton = tk.Button(self.setfocus_frame,text='F_Set',
                                         command=lambda: app.frame.focus_setcords())
        self.focus_setbutton.grid(row=0,column=1,rowspan=2,sticky='news')
        
        self.setfocus_frame.rowconfigure((0,1),weight=1)
        
        #Frame for setting x,y cords to horizontal points.
        self.sethorizontal_frame = tk.Frame(self,relief=tk.SUNKEN,bd=3)
        self.sethorizontal_frame.grid(row=0,column=7,rowspan=2,columnspan=3,sticky='news')
        
        #Options for setting x,y cords to horizontal points
        self.horizontaly_label = tk.Label(self.sethorizontal_frame,text='Y')
        self.horizontaly_label.grid(row=0,column=0,sticky='news')
        self.horizontalx_label = tk.Label(self.sethorizontal_frame,text='X1,X2')
        self.horizontalx_label.grid(row=1,column=0,sticky='news')
        
        self.horizontal_sety = tk.Entry(self.sethorizontal_frame,width=5)
        self.horizontal_sety.grid(row=0,column=1,sticky='news')
        self.horizontal_sety.insert(0,0)
        self.horizontal_setx1 = tk.Entry(self.sethorizontal_frame,width=5)
        self.horizontal_setx1.grid(row=1,column=1,sticky='news')
        self.horizontal_setx1.insert(0,0)
        self.horizontal_setx2 = tk.Entry(self.sethorizontal_frame,width=5)
        self.horizontal_setx2.grid(row=1,column=2,sticky='news')
        self.horizontal_setx2.insert(0,0)
        self.horizontal_setbutton = tk.Button(self.sethorizontal_frame,text='H_Set',
                                              command=lambda: app.frame.horizontal_setcords())
        self.horizontal_setbutton.grid(row=0,column=2,sticky='news')
        
        self.sethorizontal_frame.rowconfigure((0,1),weight=1)
        
        #Info Labels for drawing line
        self.drawx_label = tk.Label(self,text='X1/Y1')
        self.drawx_label.grid(row=0,column=10,sticky='news')
        self.drawy_label = tk.Label(self,text='X2/Y2')
        self.drawy_label.grid(row=1,column=10,sticky='news')
        
        #Frame for draw normal and perspective lines
        self.draw_frame = tk.Frame(self,relief=tk.SUNKEN,bd=2)
        self.draw_frame.grid(row=0,column=11,rowspan=2,columnspan=7,sticky='news')
        
        #Options as above
        self.draw_x1 = tk.Entry(self.draw_frame,width=4)
        self.draw_x1.grid(row=0,column=0,sticky='news')
        self.draw_x1.insert(0,0)
        self.draw_y1 = tk.Entry(self.draw_frame,width=4)
        self.draw_y1.grid(row=0,column=1,sticky='news')
        self.draw_y1.insert(0,0)
        
        self.draw_x2 = tk.Entry(self.draw_frame,width=4)
        self.draw_x2.grid(row=1,column=0,sticky='news')
        self.draw_x2.insert(0,0)
        self.draw_y2 = tk.Entry(self.draw_frame,width=4)
        self.draw_y2.grid(row=1,column=1,sticky='news')
        self.draw_y2.insert(0,0)
        
        #Draw Line
        self.draw_button = tk.Button(self.draw_frame,text='Draw',
                                     command=lambda: app.frame.draw_line())
        self.draw_button.grid(row=0,column=2,rowspan=2,sticky='news')
        
        #Delete last line
        self.deldraw_button = tk.Button(self.draw_frame,text='Del Line',
                                        command=lambda: app.frame.dellast_drawline())
        self.deldraw_button.grid(row=0,column=3,rowspan=2,sticky='news')
        
        #Draw Perspective based on X1Y1 point
        self.draw_perspline1 = tk.Button(self.draw_frame,text='Draw Persp',
                                         command=lambda: app.frame.perspective_lines(tuple([int(self.draw_x1.get()),int(self.draw_y1.get())])))
        self.draw_perspline1.grid(row=0,column=4,sticky='news')
        
        #Draw Perspective based on X2Y2 point
        self.draw_perspline2 = tk.Button(self.draw_frame,text='Draw Persp',
                                         command=lambda: app.frame.perspective_lines(tuple([int(self.draw_x2.get()),int(self.draw_y2.get())])))
        self.draw_perspline2.grid(row=1,column=4,sticky='news')
        
        self.count_left = tk.Label(self.draw_frame,text='Cro-X')
        self.count_left.grid(row=0,column=5,sticky='news')
        
        self.count_x = tk.Entry(self.draw_frame,width=4)
        self.count_x.grid(row=1,column=5,sticky='news')
        self.count_x.insert(0,0)
        
        self.draw_onperspleft = tk.Button(self.draw_frame,text='Draw on left pers',
                                         command=lambda: app.frame.draw_line_basedonpersp(
                                             app.frame.left_2point,
                                             tuple([int(self.draw_x1.get()),int(self.draw_y1.get())]),
                                             tuple([int(self.draw_x2.get()),int(self.draw_y2.get())]),
                                             int(self.count_x.get())
                                             ))
        self.draw_onperspleft.grid(row=0,column=6,sticky='news')
        
        self.draw_onperspright = tk.Button(self.draw_frame,text='Draw on right pers',
                                         command=lambda: app.frame.draw_line_basedonpersp(
                                             app.frame.right_2point,
                                             tuple([int(self.draw_x1.get()),int(self.draw_y1.get())]),
                                             tuple([int(self.draw_x2.get()),int(self.draw_y2.get())]),
                                             int(self.count_x.get())
                                             ))
        self.draw_onperspright.grid(row=1,column=6,sticky='news')
        
        
        self.draw_frame.rowconfigure((0,1),weight=1)
        

class Other_Stuff(tk.Frame):

    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)
        
        cos = tk.Button(self,text='Cube')
        cos.pack()
    
           
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = Test_Building()
        self.frame.pack()
    

class StraightLine():

    def __init__(self,coord_1,coord_2):
        
        self.coord_1 = coord_1
        self.coord_2 = coord_2
        
        self.math_slope()
        self.math_y_intercept()
    

    def math_slope(self):
        '''
        Returns slope for straight line going through 2 points.
        '''
        self.slope = (self.coord_1[1]-self.coord_2[1])/(self.coord_1[0]-self.coord_2[0])
    
    def math_y_intercept(self):
        '''
        Returns y intercept of line.
        '''
        self.y_intercept = self.coord_1[1]-self.slope*self.coord_1[0]
    
    def math_x_crosspoint(self, y):
        '''
        Calculating x point for given y cord.  
        '''
        return ((y - self.y_intercept) / self.slope)

    
    def math_y_crosspoint(self, x):
        '''
        Calculating y point for given y cord.
        '''
        return self.slope * x + self.y_intercept
                


       
        

if __name__ == "__main__": 
    app = Application()
    app.mainloop()  