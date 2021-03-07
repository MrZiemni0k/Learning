import StraightLine as sl
import tkinter as tk

class Cuboid():
    '''
    A class used to draw cuboid on tk.Canvas
    
    
    ¤ ATTRIBUTES
    ¯¯¯¯¯¯¯¯¯¯¯¯¯
            
        canvas : tk.Canvas
            Canvas parent on which cuboid painting should be made.       
        startcord : tup(int,int)
            Start point coordinates for drawing a cuboid.
        _x1 : int
            x-coordinate for "left" corner of cuboid.
        _x2 : int
            x-coordinate for "right" corner of cuboid.
        _y : int
            y-cordinate for "middle" edge ending of cuboid.
    
    ¤ METHODS
    ¯¯¯¯¯¯¯¯¯¯¯¯¯ 
        draw_cuboid_2persp()
            Draws cuboid based on 2 vanishing points.
            
    '''
    def __init__(self,canvas,startcoord,_x1,_x2,_y):
        '''
        ¤ Parameters
        ¯¯¯¯¯¯¯¯¯¯¯¯¯
        
            canvas : tk.Canvas
                Canvas parent on which cuboid painting should be made.
            startcord : tuple(int,int)
                Start point coordinates for drawing a cuboid.
            _x1 : int
                x-coordinate for "left" corner of cuboid.
            _x2 : int
                x-coordinate for "right" corner of cuboid.
            _y : int
                y-cordinate for "middle" edge ending of cuboid.
        '''
        self.canvas = canvas
        self.startcoord = startcoord
        self._x1 = _x1
        self._x2 = _x2 
        self._y = _y
    
    def draw_cuboid_2persp(self,
                           left_vp,
                           right_vp,
                           lcolor='black'
                           ):
        """
        Draws cuboid based on 2 vanishing points.
        
        Calculates cuboid's corners using line equations.
        Then based on corners, draws all cuboid lines and stores them in 
        line_list : list - for future configurations.
        
        
        ¤ PARAMETERS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯
        
            left_vp : tuple(int,int)
                Left vanishing point coordinates.
            right_vp : tuple(int,int)
                Right vanishing point coordinatates.
            lcolor : str/hex code, ¤ OPTIONAL ¤ 
                Lines' color. Defaults to 'black'.
               
        """

        #Finding equations of all needed lines:

        #Left Perspective Lines to Mid Edge
        self.lp_line1 = sl.StraightLine(self.startcoord,left_vp)
        self.lp_line2 = sl.StraightLine((self.startcoord[0],self._y),
                                        left_vp)
        
        #Right Perspective Lines to Mid Edge
        self.rp_line1 = sl.StraightLine(self.startcoord,right_vp)
        self.rp_line2 = sl.StraightLine((self.startcoord[0],self._y),
                                        right_vp)   
        
        #Cuboid Corners:
        self.left_corner1 = tuple([self._x1,
                                int(self.lp_line1.math_y_crosspoint(self._x1))
                                ]
                                )
        self.left_corner2 = tuple([self._x1,
                                int(self.lp_line2.math_y_crosspoint(self._x1))
                                ]
                                )
        self.right_corner1 = tuple([self._x2,
                                int(self.rp_line1.math_y_crosspoint(self._x2))
                                ]
                                )
        self.right_corner2 = tuple([self._x2,
                                int(self.rp_line2.math_y_crosspoint(self._x2))
                                ]
                                )
        self.midtop_corner = tuple([self.startcoord[0],self._y])
        
        #Additional Perspective Lines:
        #Also need to define top/bottom of the cuboid.
        if self._y < self.startcoord[1]: 

            #Bottom
            self.blp_line1 = sl.StraightLine(left_vp,self.right_corner1)
            self.brp_line1 = sl.StraightLine(right_vp,self.left_corner1)
            #Top
            self.blp_line2 = sl.StraightLine(left_vp,self.right_corner2)      
            self.brp_line2 = sl.StraightLine(right_vp,self.left_corner2)
            #Back Top Cuboid Corner - Intersection of two persp lines.
            self.back_btmcorner = self.blp_line1.math_line_intersection(
                                                    self.brp_line1.slope,
                                                    self.brp_line1.y_intercept
                                                    )
            #Back Bottom Cuboid Corner - Intersection of two persp lines.
            self.back_topcorner = self.blp_line2.math_line_intersection(
                                                    self.brp_line2.slope,
                                                    self.brp_line2.y_intercept
                                                    )
        else:
            #Bottom
            self.blp_line1 = sl.StraightLine(left_vp,self.right_corner2)      
            self.brp_line1 = sl.StraightLine(right_vp,self.left_corner2)
            #Top
            self.blp_line2 = sl.StraightLine(left_vp,self.right_corner1)
            self.brp_line2 = sl.StraightLine(right_vp,self.left_corner1)
            
            #Back Top Cuboid Corner - Intersection of two persp lines.
            self.back_topcorner = self.blp_line1.math_line_intersection(
                                                    self.brp_line1.slope,
                                                    self.brp_line1.y_intercept
                                                    )
            #Back Bottom Cuboid Corner - Intersection of two persp lines.
            self.back_btmcorner = self.blp_line2.math_line_intersection(
                                                    self.brp_line2.slope,
                                                    self.brp_line2.y_intercept
                                                    )
        #Drawing Lines
        #Mid Edge 
        self.mid_edge = self.canvas.create_line(self.startcoord,
                                               (self.startcoord[0],self._y),
                                               fill=lcolor
                                               )
        #Left Down Edge
        self.ldn_edge = self.canvas.create_line(self.startcoord,
                                               (self.left_corner1),
                                               fill=lcolor
                                               )
        #Left-Left Edge
        self.lft_edge = self.canvas.create_line(self.left_corner1,
                                               (self.left_corner2),
                                               fill=lcolor
                                               )
        #Left Top Edge   
        self.ltp_edge = self.canvas.create_line(self.left_corner2,
                                               (self.startcoord[0],self._y),
                                               fill=lcolor
                                               )
        #Right Down Edge
        self.rdn_edge = self.canvas.create_line(self.startcoord,
                                               (self.right_corner1),
                                               fill=lcolor
                                               )
        #Right-Right Edge
        self.rrt_edge = self.canvas.create_line(self.right_corner1,
                                               (self.right_corner2),
                                               fill=lcolor
                                               )
        #Right-Top Edge   
        self.rtp_edge = self.canvas.create_line(self.right_corner2,
                                               (self.startcoord[0],self._y),
                                               fill=lcolor
                                               )
        #Back Top Right Edge
        self.btr_edge = self.canvas.create_line(self.right_corner2,
                                               self.back_topcorner,
                                               fill=lcolor
                                               )
        #Back Top Left Edge                  
        self.btl_edge = self.canvas.create_line(self.left_corner2,
                                               self.back_topcorner,
                                               fill=lcolor
                                               )
        #Back Mid Edge  
        self.bmd_edge = self.canvas.create_line(self.back_topcorner,
                                               self.back_btmcorner,
                                               fill=lcolor
                                               )
        #Back Bottom Left Edge
        self.bbl_edge = self.canvas.create_line(self.back_btmcorner,
                                               self.left_corner1,
                                               fill=lcolor
                                               )        
        #Back Bottom Right Edge
        self.bbr_edge = self.canvas.create_line(self.back_btmcorner,
                                               self.right_corner1,
                                               fill=lcolor
                                               )
        
        #Store lines for future configurations.
        self.line_list = [self.mid_edge,
                          self.ldn_edge,
                          self.lft_edge,
                          self.ltp_edge,
                          self.rdn_edge,
                          self.rrt_edge,
                          self.rtp_edge,
                          self.btl_edge,
                          self.btr_edge,
                          self.bmd_edge,
                          self.bbl_edge,
                          self.bbr_edge
                          ]
    
    def perspective_lines(self,canv_height,lcolor="orange",ldash=(10,50)):
        """
        Draws perspective lines for cuboid.
        
        Based on equations at draw_cuboid_2persp() draws perspective lines,
        then stores them in a perspline_list for future configurations.
        
        
        ¤ PARAMETERS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯
        
            canv_height : int
                Maximum height of canvas.
            lcolor : str/hex, ¤ OPTIONAL ¤
                Color of line. Defaults to "orange".
            ldash : tuple(int,int), ¤ OPTIONAL ¤
                [description]. Defaults to (10,50).
            dash : tuple(int,int) ¤ OPTIONAL ¤
                Creates dash for line. (Fill/Space)
        
        """
        
        #Calculate x cords for TOP/BOTTOM canvas borders by given line equation
        #Drawing perspective lines based on equations at draw_cuboid_2persp()
        
        #Left Vanish Point - Startcoord
        x_start = int(self.lp_line1.math_x_crosspoint(0))
        x_end = int(self.lp_line1.math_x_crosspoint(canv_height))
        self.p1 = self.canvas.create_line((x_start,0),
                                          (x_end,canv_height),
                                          fill=lcolor,
                                          dash=ldash
                                          )
        #Right Vanish Point - Startcoord
        x_start = int(self.rp_line1.math_x_crosspoint(canv_height))
        x_end = int(self.rp_line1.math_x_crosspoint(0))
        self.p2 = self.canvas.create_line((x_start,canv_height),
                                          (x_end,0),
                                          fill=lcolor,
                                          dash=ldash
                                          )
        #Left Vanish Point - Midtop_Corner
        x_start = int(self.lp_line2.math_x_crosspoint(0))
        x_end = int(self.lp_line2.math_x_crosspoint(canv_height))
        self.p3 = self.canvas.create_line((x_start,0),
                                          (x_end,canv_height),
                                          fill=lcolor,
                                          dash=ldash
                                          )
        #Right Vanish Point - Midtop_Corner
        x_start = int(self.rp_line2.math_x_crosspoint(canv_height))
        x_end = int(self.rp_line2.math_x_crosspoint(0))
        self.p4 = self.canvas.create_line((x_start,canv_height),
                                          (x_end,0),
                                          fill=lcolor,
                                          dash=ldash
                                          )
        #Left Vanish Point - Right_Corner2
        x_start = int(self.blp_line2.math_x_crosspoint(0))
        x_end = int(self.blp_line2.math_x_crosspoint(canv_height))
        self.p5 = self.canvas.create_line((x_start,0),
                                          (x_end,canv_height),
                                          fill=lcolor,
                                          dash=ldash
                                          )
        #Right Vanish Point - Left_Corner2
        x_start = int(self.brp_line2.math_x_crosspoint(canv_height))
        x_end = int(self.brp_line2.math_x_crosspoint(0))
        self.p6 = self.canvas.create_line((x_start,canv_height),
                                          (x_end,0),
                                          fill=lcolor,
                                          dash=ldash
                                          )
        #Left Vanish Point - Right_Corner1
        x_start = int(self.blp_line1.math_x_crosspoint(0))
        x_end = int(self.blp_line1.math_x_crosspoint(canv_height))
        self.p7 = self.canvas.create_line((x_start,0),
                                          (x_end,canv_height),
                                          fill=lcolor,
                                          dash=ldash
                                          )
        #Right Vanish Point - Left_Corner1
        x_start = int(self.brp_line1.math_x_crosspoint(canv_height))
        x_end = int(self.brp_line1.math_x_crosspoint(0))
        self.p8 = self.canvas.create_line((x_start,canv_height),
                                          (x_end,0),
                                          fill=lcolor,
                                          dash=ldash
                                          )
        self.perspline_list = [self.p1,
                               self.p2,
                               self.p3,
                               self.p4,
                               self.p5,
                               self.p6,
                               self.p7,
                               self.p8
                               ]
           
    def not_visible_lines(self,vanishing_height,lcolor='black',
                          notvlcolor='grey',state='normal'):
        """
        Changes color and visibility configuration of backlines.
        
        Stores backlines in not_vislines_list : list
        
        
        ¤ PARAMETERS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯
        
            vanishing_height : int
                Y-Coordinate of any vanishing point.
            lcolor : str/hex code, ¤ OPTIONAL ¤
                Visible (FRONT) line color. Defaults to 'black'.
            notvlcolor : str, ¤ OPTIONAL ¤
                Not visible (BACK) lines color. Defaults to 'grey'.
            state : str, ¤ OPTIONAL ¤
                Toggles visibility of lines. Defaults to 'normal'.
                Avaiable options: 'hidden'/'normal' 
        
        """
        
        self.not_vislines_list = []
        #Check if corners are visible -> Corner Points/Vanishing Points
        
        #Start over horizontal line
        if self.startcoord[1] < vanishing_height:
            #Bottom visible
            self.canvas.itemconfig(self.btl_edge,fill=lcolor)
            self.canvas.itemconfig(self.btr_edge,fill=lcolor)
            #Top not visible
            self.canvas.itemconfig(self.bbl_edge,fill=notvlcolor,state=state)
            self.canvas.itemconfig(self.bbr_edge,fill=notvlcolor,state=state)
            self.canvas.itemconfig(self.bmd_edge,fill=notvlcolor,state=state)
            
            #Store not visible lines for future configurations.
            self.not_vislines_list = [self.bbl_edge,
                                      self.bbr_edge,
                                      self.bmd_edge
                                     ]
            
            if self.back_btmcorner[1] < vanishing_height:
                #Bottom not visible - Under horizontal line /Reversed Cuboid
                self.canvas.itemconfig(self.btl_edge,
                                        fill=notvlcolor,state=state)
                self.canvas.itemconfig(self.btr_edge,
                                        fill=notvlcolor,state=state)
                
                self.not_vislines_list.extend([self.btl_edge,self.btr_edge]) 
                            
        #Start under horizontal line 
        if self.startcoord[1] > vanishing_height:
            #Top visible
            self.canvas.itemconfig(self.bbl_edge,fill=lcolor)
            self.canvas.itemconfig(self.bbr_edge,fill=lcolor)
            #Bottom not visible
            self.canvas.itemconfig(self.btl_edge,fill=notvlcolor,state=state)
            self.canvas.itemconfig(self.btr_edge,fill=notvlcolor,state=state)
            self.canvas.itemconfig(self.bmd_edge,fill=notvlcolor,state=state)
            
            #Store not visible lines for future configurations.
            self.not_vislines_list = [self.btl_edge,
                                      self.btr_edge,
                                      self.bmd_edge
                                     ]
            
            if self.back_btmcorner[1] > vanishing_height:
                #Top not visible - Over horizontal line /Reversed Cuboid
                self.canvas.itemconfig(self.bbl_edge,
                                        fill=notvlcolor,state=state)
                self.canvas.itemconfig(self.bbr_edge,
                                        fill=notvlcolor,state=state)
                
                self.not_vislines_list.extend([self.bbl_edge,self.bbr_edge])
    
    def change_lines(self,
                     line_list,
                     lcolor='black',
                     state='normal',
                     width=1,
                     dash=()):
        """
        Changes style and visibility of lines passed in a list.
        
        
        ¤ PARAMETERS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯
        
            line_list : list
                List of lines that needs to be configurated.
            lcolor : str/hex code, ¤ OPTIONAL ¤
                Color of lines. Defaults to 'black'.
            state : str, ¤ OPTIONAL ¤
                Toggles visibility of lines. Defaults to 'normal'.
                Avaiable options: 'hidden'/'normal'
            width : int, ¤ OPTIONAL ¤
                Width of line. Defaults to 1.
            dash : tuple(int,int) ¤ OPTIONAL ¤
                Creates dash for line. (Fill/Space)
        
        """
        for _ in line_list:
            self.canvas.itemconfig(_,fill=lcolor,state=state,width=width)
        
    def del_lines(self,line_list):
        """
        Deletes lines that are in a list
        
        ¤ PARAMETERS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯
        
            line_list : list
                List of lines that needs to be deleted.
          
        """
        for _ in line_list:
            self.canvas.delete(_)

        
                
                
                 
        #Coords Texts On Cuboid Corners
        self.startcoord_text = self.canvas.create_text(self.startcoord,
                                          text=f'{self.startcoord}',
                                          fill='white'
                                          )
        self.midtopcorner_text = self.canvas.create_text(self.midtop_corner,
                                          text=f'{self.midtop_corner}',
                                          fill='white'
                                          )
        self.leftcorner1_text = self.canvas.create_text(self.left_corner1,
                                          text=f'{self.left_corner1}',
                                          fill='white'
                                          )
        self.leftcorner2_text = self.canvas.create_text(self.left_corner2,
                                          text=f'{self.left_corner2}',
                                          fill='white'
                                          )
        self.rightcorner1_text = self.canvas.create_text(self.right_corner1,
                                          text=f'{self.right_corner1}',
                                          fill='white'
                                          )  
        self.rightcorner2_text = self.canvas.create_text(self.right_corner2,
                                          text=f'{self.right_corner2}',
                                          fill='white'
                                          )
        self.bhdtopcorner_text = self.canvas.create_text(self.back_topcorner,
                                          text=f'BT{self.back_topcorner}',
                                          fill='white'
                                          )   
        self.bhdbtmcorner_text = self.canvas.create_text(self.back_btmcorner,
                                          text=f'BM{self.back_btmcorner}',
                                          fill='white'
                                          )                               
        
        
              