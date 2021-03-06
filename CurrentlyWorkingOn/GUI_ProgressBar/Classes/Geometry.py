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
        Then based on corners, draws all cuboid lines and stores them in a list
        for future configurations.
        
        
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
            #Behind Top Cuboid Corner - Intersection of two persp lines.
            self.behind_btmcorner = self.blp_line1.math_line_intersection(
                                                    self.brp_line1.slope,
                                                    self.brp_line1.y_intercept
                                                    )
            #Behind Bottom Cuboid Corner - Intersection of two persp lines.
            self.behind_topcorner = self.blp_line2.math_line_intersection(
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
            
            #Behind Top Cuboid Corner - Intersection of two persp lines.
            self.behind_topcorner = self.blp_line1.math_line_intersection(
                                                    self.brp_line1.slope,
                                                    self.brp_line1.y_intercept
                                                    )
            #Behind Bottom Cuboid Corner - Intersection of two persp lines.
            self.behind_btmcorner = self.blp_line2.math_line_intersection(
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
        #Behind Top Right Edge
        self.btr_edge = self.canvas.create_line(self.right_corner2,
                                               self.behind_topcorner,
                                               fill=lcolor
                                               )
        #Behind Top Left Edge                  
        self.btl_edge = self.canvas.create_line(self.left_corner2,
                                               self.behind_topcorner,
                                               fill=lcolor
                                               )
        #Behind Mid Edge  
        self.bmd_edge = self.canvas.create_line(self.behind_topcorner,
                                               self.behind_btmcorner,
                                               fill=lcolor
                                               )
        #Behind Bottom Left Edge
        self.bbl_edge = self.canvas.create_line(self.behind_btmcorner,
                                               self.left_corner1,
                                               fill=lcolor
                                               )        
        #Behind Bottom Right Edge
        self.bbr_edge = self.canvas.create_line(self.behind_btmcorner,
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
           
    def not_visible_lines(self,vanishing_height,lcolor='black',
                          notvlcolor='grey',state='normal'):
        #Check if corners are visible -> Perspective Point/Vanishing Points
        if self.startcoord[1] < vanishing_height:
            #Bottom visible
            self.canvas.itemconfig(self.btl_edge,fill=lcolor)
            self.canvas.itemconfig(self.btr_edge,fill=lcolor)
            #Top not visible
            self.canvas.itemconfig(self.bbl_edge,fill=notvlcolor,state=state)
            self.canvas.itemconfig(self.bbr_edge,fill=notvlcolor,state=state)
            self.canvas.itemconfig(self.bmd_edge,fill=notvlcolor,state=state)           
        
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
        self.bhdtopcorner_text = self.canvas.create_text(self.behind_topcorner,
                                          text=f'BT{self.behind_topcorner}',
                                          fill='white'
                                          )   
        self.bhdbtmcorner_text = self.canvas.create_text(self.behind_btmcorner,
                                          text=f'BM{self.behind_btmcorner}',
                                          fill='white'
                                          )                               
        
        
              