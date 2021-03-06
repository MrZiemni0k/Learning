class StraightLine():
    '''
    Class to store parameters and calculate various things for a straight line.
    ........
    
    Methods
    ----------
    math_slope()
        Calculate slope for itself.
    math_y_intercept()
        Calculate y_intercept for itself.
    math_x_crosspoint(y)
        Calculate x crosspoint based on passed y cord.
    math_y_crosspoint(x)
        Calculate y crosspoint based on passed x cord.
    math_line_intersection()
        Calculate point of intersection for itself and given line.
    '''

    def __init__(self,coord_1,coord_2):
        '''
        Arguments:
        ------------
        coord_1(tup)
            Cords of 1st point (x,y)
        coord_2(tup)
            Cords of 2nd point (x,y)
        '''
        
        self.coord_1 = coord_1
        self.coord_2 = coord_2
        
        self.math_slope()
        self.math_y_intercept()
    

    def math_slope(self):
        '''
        Returns slope for straight line going through 2 points.
        '''
        if self.coord_1[0] != self.coord_2[0]:
            self.slope = (self.coord_1[1]-self.coord_2[1])/(self.coord_1[0]-self.coord_2[0])
        else:
            self.slope = 0
            print("No slope found. It's vertical line.")
    
    def math_y_intercept(self):
        '''
        Returns y intercept of line.
        '''
        self.y_intercept = self.coord_1[1]-self.slope*self.coord_1[0]
    
    def math_x_crosspoint(self, y):
        '''
        Calculating x-line crosspoint for given y cord.  
        '''
        if self.slope != 0:
            return ((y - self.y_intercept) / self.slope)
        else:
            print("Line is Vertical. X not found.")
            return None
    
    def math_y_crosspoint(self, x):
        '''
        Calculating y-line crosspoint for given x cord.
        '''
        return self.slope * x + self.y_intercept      
    def math_line_intersection(self,foreign_slope,foreign_yintercept):
        '''
        Calculating point of intersection for given line.
        If parallel line is given - Returning None
        '''     
        if self.slope != foreign_slope:
            #Calculate X Point of Intersection
            x = int((-self.y_intercept+foreign_yintercept)/(self.slope-foreign_slope))
            #Calculate Y Point of Intersection
            y = -int((self.slope*(-foreign_yintercept)-foreign_slope*(-self.y_intercept))/(self.slope-foreign_slope))
            return(tuple([x,y]))
        else:
            print("Lines are parallel to eachother. No intersection found.")
            return None