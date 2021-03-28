import Modules.Support_Classes.StraightLine as sl
import tkinter as tk


class Cuboid():
    """
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
        stopdrawing : bool
                Switch option to avoid programm crashing
                when wrong parameters are passed
        cuboid_reversed: bool
                Switch for calculations in case _y > startcord[1]

    ¤ METHODS
    ¯¯¯¯¯¯¯¯¯¯¯¯¯
        math_cubcorners_2persp()
            Calculates cuboid's corners using line equations.
        draw_2persp_cuboid()
            Draws cuboid based on 2 vanishing points.
        draw_2persp_lines()
            Draws perspective lines for cuboid.
        draw_2persp_walls()
            Colours cuboid's walls.
        lines_not_vis()
            Changes color and visibility configuration of backlines.
        lines_persp_not_vis()
            Changes color and visibility configuration of
            perspective lines going through not visible corners.
        lines_change()
            Changes style and visibility of lines passed in a list.
        lines_del()
            Deletes lines that are in a list.

    """

    def __init__(self, canvas, startcoord, _x1, _x2, _y):
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
            stopdrawing : bool
                Switch option to avoid programm crashing
                when wrong parameters are passed
            cuboid_reversed: bool
                Switch for calculations in case _y > startcord[1]

        '''
        self.canvas = canvas
        self.startcoord = startcoord
        self._x1 = _x1
        self._x2 = _x2
        self._y = _y
        self.stopdrawing = False
        self.cuboid_reversed = False

    def math_cubcorners_2persp(self, left_vp, right_vp):
        """
        Calculates cuboid's corners using line equations.


        ¤ PARAMETERS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯

            left_vp : tuple(int,int)
                Left vanishing point coordinates.
            right_vp : tuple(int,int)
                Right vanishing point coordinatates.

        ¤ RETURNS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯

            None:
                * If vanishing points have same X-Coordinate
        """
        if left_vp[0] == right_vp[0]:
            tk.messagebox.showinfo(title='Wrong coordinates',
                                   message='Only 1 vanishing point was found')
            self.stopdrawing = True
            return None

        # Finding equations of all needed lines:

        # Left Perspective Lines to Mid Edge
        self.lp_line1 = sl.StraightLine(self.startcoord, left_vp)
        self.lp_line2 = sl.StraightLine((self.startcoord[0], self._y),
                                        left_vp)

        # Right Perspective Lines to Mid Edge
        self.rp_line1 = sl.StraightLine(self.startcoord, right_vp)
        self.rp_line2 = sl.StraightLine((self.startcoord[0], self._y),
                                        right_vp)

        # Cuboid Corners:
        self.left_corner1 = tuple([self._x1,
                                   int(self.lp_line1.math_y_crosspoint(
                                       self._x1))
                                   ]
                                  )

        self.left_corner2 = tuple([self._x1,
                                   int(self.lp_line2.math_y_crosspoint(
                                       self._x1))
                                   ]
                                  )
        self.right_corner1 = tuple([self._x2,
                                    int(self.rp_line1.math_y_crosspoint(
                                        self._x2))
                                    ]
                                   )
        self.right_corner2 = tuple([self._x2,
                                    int(self.rp_line2.math_y_crosspoint(
                                        self._x2))
                                    ]
                                   )
        self.midtop_corner = tuple([self.startcoord[0], self._y])

        # Additional Perspective Lines:
        # Also need to define top/bottom of the cuboid.
        if self._y < self.startcoord[1]:

            # Bottom
            self.blp_line1 = sl.StraightLine(left_vp, self.right_corner1)
            self.brp_line1 = sl.StraightLine(right_vp, self.left_corner1)
            # Top
            self.blp_line2 = sl.StraightLine(left_vp, self.right_corner2)
            self.brp_line2 = sl.StraightLine(right_vp, self.left_corner2)
            # Back Top Cuboid Corner - Intersection of two persp lines.
            self.back_btmcorner = self.blp_line1.math_line_intersection(
                                                    self.brp_line1.slope,
                                                    self.brp_line1.y_intercept
                                                    )
            # Back Bottom Cuboid Corner - Intersection of two persp lines.
            self.back_topcorner = self.blp_line2.math_line_intersection(
                                                    self.brp_line2.slope,
                                                    self.brp_line2.y_intercept
                                                    )
        # Reversed Cuboid
        # TopCorner becomes BtmCorner and Btm become Top
        else:
            self.cuboid_reversed = True
            # Bottom
            self.blp_line1 = sl.StraightLine(left_vp, self.right_corner2)
            self.brp_line1 = sl.StraightLine(right_vp, self.left_corner2)
            # Top
            self.blp_line2 = sl.StraightLine(left_vp, self.right_corner1)
            self.brp_line2 = sl.StraightLine(right_vp, self.left_corner1)
            # Back Btm Cuboid Corner - Intersection of two persp lines.
            self.back_topcorner = self.blp_line1.math_line_intersection(
                                                    self.brp_line1.slope,
                                                    self.brp_line1.y_intercept
                                                    )
            # Back Top Cuboid Corner - Intersection of two persp lines.
            self.back_btmcorner = self.blp_line2.math_line_intersection(
                                                    self.brp_line2.slope,
                                                    self.brp_line2.y_intercept
                                                    )

    def draw_2persp_cuboid(self, lcolor='black', lwidth=1, ldash=()):
        """
        Draws cuboid in 2 perspective.

        Based on corners calculated at math_cubcorners_2persp(),
        draws all cuboid lines and stores them in
        line_list : list - for future configurations.

        ¤ PARAMETERS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯

            lcolor : str/hex code, ¤ OPTIONAL ¤
                Color of lines. Defaults to 'black'.
            lwidth : int, ¤ OPTIONAL ¤
                Width of line. Defaults to 1.
            ldash : tuple(int,int) ¤ OPTIONAL ¤
                Creates dash for line. (Fill/Space). Defaults to ()

        ¤ RETURNS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯

            None:
                * If switch "stopdrawing" is turned on.
                  Wrong parameters passed.

        """
        if self.stopdrawing:
            return None
        # Drawing from back to avoid overwriting.

        # Back Top Right Edge
        self.btr_edge = self.canvas.create_line(self.right_corner2,
                                                self.back_topcorner,
                                                fill=lcolor,
                                                width=lwidth,
                                                dash=ldash
                                                )
        # Back Top Left Edge
        self.btl_edge = self.canvas.create_line(self.left_corner2,
                                                self.back_topcorner,
                                                fill=lcolor,
                                                width=lwidth,
                                                dash=ldash
                                                )
        # Back Mid Edge
        self.bmd_edge = self.canvas.create_line(self.back_topcorner,
                                                self.back_btmcorner,
                                                fill=lcolor,
                                                width=lwidth,
                                                dash=ldash
                                                )
        # Back Bottom Left Edge
        self.bbl_edge = self.canvas.create_line(self.back_btmcorner,
                                                self.left_corner1,
                                                fill=lcolor,
                                                width=lwidth,
                                                dash=ldash
                                                )
        # Back Bottom Right Edge
        self.bbr_edge = self.canvas.create_line(self.back_btmcorner,
                                                self.right_corner1,
                                                fill=lcolor,
                                                width=lwidth,
                                                dash=ldash
                                                )
        # Mid Edge
        self.mid_edge = self.canvas.create_line(self.startcoord,
                                                (self.startcoord[0], self._y),
                                                fill=lcolor,
                                                width=lwidth,
                                                dash=ldash
                                                )
        # Left Down Edge
        self.ldn_edge = self.canvas.create_line(self.startcoord,
                                                (self.left_corner1),
                                                fill=lcolor,
                                                width=lwidth,
                                                dash=ldash
                                                )
        # Left-Left Edge
        self.lft_edge = self.canvas.create_line(self.left_corner1,
                                                (self.left_corner2),
                                                fill=lcolor,
                                                width=lwidth,
                                                dash=ldash
                                                )
        # Left Top Edge
        self.ltp_edge = self.canvas.create_line(self.left_corner2,
                                                (self.startcoord[0], self._y),
                                                fill=lcolor,
                                                width=lwidth,
                                                dash=ldash
                                                )
        # Right Down Edge
        self.rdn_edge = self.canvas.create_line(self.startcoord,
                                                (self.right_corner1),
                                                fill=lcolor,
                                                width=lwidth,
                                                dash=ldash
                                                )
        # Right-Right Edge
        self.rrt_edge = self.canvas.create_line(self.right_corner1,
                                                (self.right_corner2),
                                                fill=lcolor,
                                                width=lwidth,
                                                dash=ldash
                                                )
        # Right-Top Edge
        self.rtp_edge = self.canvas.create_line(self.right_corner2,
                                                (self.startcoord[0], self._y),
                                                fill=lcolor,
                                                width=lwidth,
                                                dash=ldash
                                                )
        # Store lines for future configurations.
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

    def draw_2persp_lines(self, canv_height, lcolor="orange", ldash=(10, 50)):
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
                Creates dash for line. (Fill/Space). Defaults to (10,50).

        ¤ RETURNS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯

            None:
                * If switch "stopdrawing" is turned on.
                  Wrong parameters passed.

        """
        if self.stopdrawing:
            return None
        # Calculate x cords for TOP/BOT canvas borders by given line equation

        # Left Vanish Point - Startcoord
        x_start = int(self.lp_line1.math_x_crosspoint(0))
        x_end = int(self.lp_line1.math_x_crosspoint(canv_height))
        self.p1 = self.canvas.create_line((x_start, 0),
                                          (x_end, canv_height),
                                          fill=lcolor,
                                          dash=ldash
                                          )
        # Right Vanish Point - Startcoord
        x_start = int(self.rp_line1.math_x_crosspoint(canv_height))
        x_end = int(self.rp_line1.math_x_crosspoint(0))
        self.p2 = self.canvas.create_line((x_start, canv_height),
                                          (x_end, 0),
                                          fill=lcolor,
                                          dash=ldash
                                          )
        # Left Vanish Point - Midtop_Corner
        x_start = int(self.lp_line2.math_x_crosspoint(0))
        x_end = int(self.lp_line2.math_x_crosspoint(canv_height))
        self.p3 = self.canvas.create_line((x_start, 0),
                                          (x_end, canv_height),
                                          fill=lcolor,
                                          dash=ldash
                                          )
        # Right Vanish Point - Midtop_Corner
        x_start = int(self.rp_line2.math_x_crosspoint(canv_height))
        x_end = int(self.rp_line2.math_x_crosspoint(0))
        self.p4 = self.canvas.create_line((x_start, canv_height),
                                          (x_end, 0),
                                          fill=lcolor,
                                          dash=ldash
                                          )
        # Left Vanish Point - Right_Corner2
        x_start = int(self.blp_line2.math_x_crosspoint(0))
        x_end = int(self.blp_line2.math_x_crosspoint(canv_height))
        self.p5 = self.canvas.create_line((x_start, 0),
                                          (x_end, canv_height),
                                          fill=lcolor,
                                          dash=ldash
                                          )
        # Right Vanish Point - Left_Corner2
        x_start = int(self.brp_line2.math_x_crosspoint(canv_height))
        x_end = int(self.brp_line2.math_x_crosspoint(0))
        self.p6 = self.canvas.create_line((x_start, canv_height),
                                          (x_end, 0),
                                          fill=lcolor,
                                          dash=ldash
                                          )
        # Left Vanish Point - Right_Corner1
        x_start = int(self.blp_line1.math_x_crosspoint(0))
        x_end = int(self.blp_line1.math_x_crosspoint(canv_height))
        self.p7 = self.canvas.create_line((x_start, 0),
                                          (x_end, canv_height),
                                          fill=lcolor,
                                          dash=ldash
                                          )
        # Right Vanish Point - Left_Corner1
        x_start = int(self.brp_line1.math_x_crosspoint(canv_height))
        x_end = int(self.brp_line1.math_x_crosspoint(0))
        self.p8 = self.canvas.create_line((x_start, canv_height),
                                          (x_end, 0),
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

    def draw_2persp_walls(self,
                          vanishing_height,
                          wlsidecolor='#75756c',
                          wrsidecolor='#9d9d91',
                          wtopcolor='#81817e',
                          wbotcolor='#2a2a27',
                          wbacklsidecolor='#3d3d37',
                          wbackrsidecolor='#4e4e48',
                          outline=''
                          ):
        """
        Colours cuboid's walls.

        Colours all cuboid's walls.
        Store walls in a walls_list : list for future configurations.


        ¤ PARAMETERS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯

            vanishing_height : int
                Y-Coordinate of any vanishing point.
            wlsidecolor : str/hex code ¤ OPTIONAL ¤
                Wall left side color. Defaults to '#75756c'.
            wrsidecolor : str/hex code ¤ OPTIONAL ¤
                Wall right side color. Defaults to '#9d9d91'.
            wtopcolor : str/hex code ¤ OPTIONAL ¤
                Wall top color. Defaults to '#81817e'.
            wbotcolor : str/hex code ¤ OPTIONAL ¤
                Wall bottom color. Defaults to '#2a2a27'.
            wbacklsidecolor : str/hex code ¤ OPTIONAL ¤
                Wall back left side color. Defaults to '#3d3d37'.
            wbackrsidecolor : str/hex code ¤ OPTIONAL ¤
                Wall back right side color. Defaults to '#4e4e48'.
            outline : str/hex code ¤ OPTIONAL ¤
                Cuboid's outline color. Defaults to ''.


        ¤ RETURNS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯

            None:
                * If switch "stopdrawing" is turned on.
                  Wrong parameters passed.

        """

        if self.stopdrawing:
            return None

        # Restarts list
        self.walls_list = []

        # Drawing from back of cuboid
        # Drawing from top/bottom depending on vanishing point y-coord
        if self.cuboid_reversed:

            # Going down (_y > startcord[1] -> BTM is TOP and TOP is BTM)
            if self.startcoord[1] > vanishing_height:
                # Bottom/Top (Not Visible) - Drawing from top
                self.top_wall = self.canvas.create_polygon(
                                                    self.back_topcorner,
                                                    self.left_corner2,
                                                    self.midtop_corner,
                                                    self.right_corner2,
                                                    fill=wtopcolor
                                                    )
                self.backlside_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.back_topcorner,
                                                    self.left_corner2,
                                                    self.left_corner1,
                                                    fill=wbacklsidecolor
                                                    )
                self.backrside_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.back_topcorner,
                                                    self.right_corner2,
                                                    self.right_corner1,
                                                    fill=wbackrsidecolor
                                                    )
                self.bottom_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.left_corner1,
                                                    self.startcoord,
                                                    self.right_corner1,
                                                    fill=wbotcolor
                                                    )
                self.lside_wall = self.canvas.create_polygon(
                                                    self.startcoord,
                                                    self.midtop_corner,
                                                    self.left_corner2,
                                                    self.left_corner1,
                                                    fill=wlsidecolor
                                                    )
                self.rside_wall = self.canvas.create_polygon(
                                                    self.startcoord,
                                                    self.midtop_corner,
                                                    self.right_corner2,
                                                    self.right_corner1,
                                                    fill=wrsidecolor
                                                    )
            else:
                # Top or Bottom Wall is Visible
                if self.midtop_corner[1] < vanishing_height:
                    # Bottom (Cuboid's Top) is visible. Drawing from Top
                    self.backlside_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.back_topcorner,
                                                    self.left_corner2,
                                                    self.left_corner1,
                                                    fill=wbacklsidecolor
                                                    )
                    self.backrside_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.back_topcorner,
                                                    self.right_corner2,
                                                    self.right_corner1,
                                                    fill=wbackrsidecolor
                                                    )
                    self.bottom_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.left_corner1,
                                                    self.startcoord,
                                                    self.right_corner1,
                                                    fill=wbotcolor
                                                    )
                    self.lside_wall = self.canvas.create_polygon(
                                                    self.startcoord,
                                                    self.midtop_corner,
                                                    self.left_corner2,
                                                    self.left_corner1,
                                                    fill=wlsidecolor
                                                    )
                    self.rside_wall = self.canvas.create_polygon(
                                                    self.startcoord,
                                                    self.midtop_corner,
                                                    self.right_corner2,
                                                    self.right_corner1,
                                                    fill=wrsidecolor
                                                    )
                    self.top_wall = self.canvas.create_polygon(
                                                    self.back_topcorner,
                                                    self.left_corner2,
                                                    self.midtop_corner,
                                                    self.right_corner2,
                                                    fill=wtopcolor
                                                    )
                else:
                    # Top (Cuboid's BTM) is visible. Drawing from buttom
                    self.top_wall = self.canvas.create_polygon(
                                                    self.back_topcorner,
                                                    self.left_corner2,
                                                    self.midtop_corner,
                                                    self.right_corner2,
                                                    fill=wtopcolor
                                                    )
                    self.backlside_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.back_topcorner,
                                                    self.left_corner2,
                                                    self.left_corner1,
                                                    fill=wbacklsidecolor
                                                    )
                    self.backrside_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.back_topcorner,
                                                    self.right_corner2,
                                                    self.right_corner1,
                                                    fill=wbackrsidecolor
                                                    )
                    self.bottom_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.left_corner1,
                                                    self.startcoord,
                                                    self.right_corner1,
                                                    fill=wbotcolor
                                                    )
                    self.lside_wall = self.canvas.create_polygon(
                                                    self.startcoord,
                                                    self.midtop_corner,
                                                    self.left_corner2,
                                                    self.left_corner1,
                                                    fill=wlsidecolor
                                                    )
                    self.rside_wall = self.canvas.create_polygon(
                                                    self.startcoord,
                                                    self.midtop_corner,
                                                    self.right_corner2,
                                                    self.right_corner1,
                                                    fill=wrsidecolor
                                                    )
        else:
            # Going up (_y < startcord[1] -> BTM is BTM and TOP is TOP)
            if self.startcoord[1] < vanishing_height:
                # Bottom Visible - Drawing from top
                self.top_wall = self.canvas.create_polygon(
                                                    self.back_topcorner,
                                                    self.left_corner2,
                                                    self.midtop_corner,
                                                    self.right_corner2,
                                                    fill=wtopcolor
                                                    )
                self.backlside_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.back_topcorner,
                                                    self.left_corner2,
                                                    self.left_corner1,
                                                    fill=wbacklsidecolor
                                                    )
                self.backrside_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.back_topcorner,
                                                    self.right_corner2,
                                                    self.right_corner1,
                                                    fill=wbackrsidecolor
                                                    )
                self.bottom_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.left_corner1,
                                                    self.startcoord,
                                                    self.right_corner1,
                                                    fill=wbotcolor
                                                    )
                self.lside_wall = self.canvas.create_polygon(
                                                    self.startcoord,
                                                    self.midtop_corner,
                                                    self.left_corner2,
                                                    self.left_corner1,
                                                    fill=wlsidecolor
                                                    )
                self.rside_wall = self.canvas.create_polygon(
                                                    self.startcoord,
                                                    self.midtop_corner,
                                                    self.right_corner2,
                                                    self.right_corner1,
                                                    fill=wrsidecolor
                                                    )
            else:
                # Top is visible or Top and Bottom are not visible.
                if self.midtop_corner[1] > vanishing_height:
                    # Top is visible. Drawing from bottom
                    self.bottom_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.left_corner1,
                                                    self.startcoord,
                                                    self.right_corner1,
                                                    fill=wbotcolor
                                                    )
                    self.backlside_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.back_topcorner,
                                                    self.left_corner2,
                                                    self.left_corner1,
                                                    fill=wbacklsidecolor
                                                    )
                    self.backrside_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.back_topcorner,
                                                    self.right_corner2,
                                                    self.right_corner1,
                                                    fill=wbackrsidecolor
                                                    )
                    self.lside_wall = self.canvas.create_polygon(
                                                    self.startcoord,
                                                    self.midtop_corner,
                                                    self.left_corner2,
                                                    self.left_corner1,
                                                    fill=wlsidecolor
                                                    )
                    self.rside_wall = self.canvas.create_polygon(
                                                    self.startcoord,
                                                    self.midtop_corner,
                                                    self.right_corner2,
                                                    self.right_corner1,
                                                    fill=wrsidecolor
                                                    )
                    self.top_wall = self.canvas.create_polygon(
                                                    self.back_topcorner,
                                                    self.left_corner2,
                                                    self.midtop_corner,
                                                    self.right_corner2,
                                                    fill=wtopcolor
                                                    )
                else:
                    # Top and bottom not visible. Drawing from top
                    self.top_wall = self.canvas.create_polygon(
                                                    self.back_topcorner,
                                                    self.left_corner2,
                                                    self.midtop_corner,
                                                    self.right_corner2,
                                                    fill=wtopcolor
                                                    )
                    self.backlside_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.back_topcorner,
                                                    self.left_corner2,
                                                    self.left_corner1,
                                                    fill=wbacklsidecolor
                                                    )
                    self.backrside_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.back_topcorner,
                                                    self.right_corner2,
                                                    self.right_corner1,
                                                    fill=wbackrsidecolor
                                                    )
                    self.bottom_wall = self.canvas.create_polygon(
                                                    self.back_btmcorner,
                                                    self.left_corner1,
                                                    self.startcoord,
                                                    self.right_corner1,
                                                    fill=wbotcolor
                                                    )
                    self.lside_wall = self.canvas.create_polygon(
                                                    self.startcoord,
                                                    self.midtop_corner,
                                                    self.left_corner2,
                                                    self.left_corner1,
                                                    fill=wlsidecolor
                                                    )
                    self.rside_wall = self.canvas.create_polygon(
                                                    self.startcoord,
                                                    self.midtop_corner,
                                                    self.right_corner2,
                                                    self.right_corner1,
                                                    fill=wrsidecolor
                                                    )

        self.walls_lists = [self.top_wall,
                            self.backlside_wall,
                            self.backrside_wall,
                            self.bottom_wall,
                            self.lside_wall,
                            self.rside_wall
                            ]

    def lines_not_vis(self,
                      vanishing_height,
                      notvlcolor='grey',
                      state='normal'
                      ):
        """
        Changes color and visibility configuration of backlines.

        Backlines are decided by relation of:
            * Corner-Corner Y-Coordinates.
            * Corner-Vanishing Y-Coordinates.
        Stores backlines in not_vislines_list : list
        Other lines stores in vislines_list : list

        ¤ PARAMETERS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯

            vanishing_height : int
                Y-Coordinate of any vanishing point.
            notvlcolor : str, ¤ OPTIONAL ¤
                Not visible (BACK) lines color. Defaults to 'grey'.
            state : str, ¤ OPTIONAL ¤
                Toggles visibility of lines. Defaults to 'normal'.
                Avaiable options: 'hidden'/'normal'

        ¤ RETURNS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯

            None:
                * If switch "stopdrawing" is turned on.
                  Wrong parameters passed.

        """

        if self.stopdrawing:
            return None

        # Restart lists
        self.not_vislines_list = []

        # Check if corners are visible -> Corner Points/Vanishing Points

        if self.cuboid_reversed:

            # Start over vanishing point - Going down (_y > startcoord[1])
            if self.startcoord[1] < vanishing_height:
                # Top not visible (Reversed so TOP -> BTM)
                self.canvas.itemconfig(self.bbl_edge,
                                       fill=notvlcolor,
                                       state=state
                                       )
                self.canvas.itemconfig(self.bbr_edge,
                                       fill=notvlcolor,
                                       state=state
                                       )
                self.canvas.itemconfig(self.bmd_edge,
                                       fill=notvlcolor,
                                       state=state
                                       )
                # Store not visible lines for future configurations.
                self.not_vislines_list = [self.bbl_edge,
                                          self.bbr_edge,
                                          self.bmd_edge
                                          ]
                # Check if bottom is visible
                if self.back_topcorner[1] > vanishing_height:
                    # Bottom not visible (Reversed so BTM -> TOP)
                    self.canvas.itemconfig(self.btl_edge,
                                           fill=notvlcolor,
                                           state=state
                                           )
                    self.canvas.itemconfig(self.btr_edge,
                                           fill=notvlcolor,
                                           state=state
                                           )

                    self.not_vislines_list.extend([self.btl_edge,
                                                   self.btr_edge
                                                   ]
                                                  )
            # Below Vanishing Point and going down so top visible, bottom not
            else:
                # Bottom not visible (Reversed so BTM -> TOP)
                self.canvas.itemconfig(self.btl_edge,
                                       fill=notvlcolor,
                                       state=state
                                       )
                self.canvas.itemconfig(self.btr_edge,
                                       fill=notvlcolor,
                                       state=state
                                       )
                self.canvas.itemconfig(self.bmd_edge,
                                       fill=notvlcolor,
                                       state=state
                                       )
                # Store not visible lines for future configurations.
                self.not_vislines_list = [self.btl_edge,
                                          self.btr_edge,
                                          self.bmd_edge
                                          ]
        # Not Reversed Cuboid
        else:
            # Start below vanishing point - Going up (_y < startcoord[1])
            if self.startcoord[1] > vanishing_height:
                # Bottom not visible
                self.canvas.itemconfig(self.bbl_edge,
                                       fill=notvlcolor,
                                       state=state
                                       )
                self.canvas.itemconfig(self.bbr_edge,
                                       fill=notvlcolor,
                                       state=state
                                       )
                self.canvas.itemconfig(self.bmd_edge,
                                       fill=notvlcolor,
                                       state=state
                                       )
                # Store not visible lines for future configurations.
                self.not_vislines_list = [self.bbl_edge,
                                          self.bbr_edge,
                                          self.bmd_edge
                                          ]
                # Check if top is visible
                if self.back_topcorner[1] < vanishing_height:
                    # Top not visible
                    self.canvas.itemconfig(self.btl_edge,
                                           fill=notvlcolor,
                                           state=state
                                           )
                    self.canvas.itemconfig(self.btr_edge,
                                           fill=notvlcolor,
                                           state=state
                                           )

                    self.not_vislines_list.extend([self.btl_edge,
                                                   self.btr_edge
                                                   ]
                                                  )
            # Over Vanishing Point and going up so bottom visible, top not
            else:
                # Top not visible
                self.canvas.itemconfig(self.btl_edge,
                                       fill=notvlcolor,
                                       state=state
                                       )
                self.canvas.itemconfig(self.btr_edge,
                                       fill=notvlcolor,
                                       state=state
                                       )
                self.canvas.itemconfig(self.bmd_edge,
                                       fill=notvlcolor,
                                       state=state
                                       )
                # Store not visible lines for future configurations.
                self.not_vislines_list = [self.btl_edge,
                                          self.btr_edge,
                                          self.bmd_edge
                                          ]
        # Store visible lines for future configurations.
        self.vis_lines_list = [line for line in self.line_list
                               if line not in self.not_vislines_list]

    def lines_persp_not_vis(self,
                            vanishing_height,
                            notvlcolor='#9dad7f',
                            state='normal'):
        """
        Changes color and visibility configuration of
        perspective lines going through not visible corners.

        These perspective lines are decided by relation of:
            * Corner-Corner Y-Coordinates.
            * Corner-Vanishing Y-Coordinates.
        Stores these lines in not_vis_plines_list : list
        Other lines stores in vis_plines_list : list


        ¤ PARAMETERS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯
            vanishing_height : int
                Y-Coordinate of any vanishing point.
            notvlcolor : str, ¤ OPTIONAL ¤
                "Not visible" lines color. Defaults to 'grey'.
            state : str, ¤ OPTIONAL ¤
                Toggles visibility of lines. Defaults to 'normal'.
                Avaiable options: 'hidden'/'normal'

        ¤ RETURNS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯
            None:
                * If switch "stopdrawing" is turned on.
                  Wrong parameters passed.
        """
        if self.stopdrawing:
            return None

        # Restart lists
        self.not_visplines_list = []

        # Check if corners are visible -> Corner Points/Vanishing Points

        if self.cuboid_reversed:

            # Start over vanishing point - Going down (_y > startcoord[1])
            if self.startcoord[1] < vanishing_height:
                # Top not visible (Reversed so TOP -> BTM)
                self.canvas.itemconfig(self.p5,
                                       fill=notvlcolor,
                                       state=state
                                       )
                self.canvas.itemconfig(self.p6,
                                       fill=notvlcolor,
                                       state=state
                                       )
                # Store not visible plines for future configurations.
                self.not_visplines_list = [self.p5,
                                           self.p6,
                                           ]
                # Check if bottom is visible
                if self.back_topcorner[1] > vanishing_height:
                    # Bottom not visible (Reversed so BTM -> TOP)
                    self.canvas.itemconfig(self.p7,
                                           fill=notvlcolor,
                                           state=state
                                           )
                    self.canvas.itemconfig(self.p8,
                                           fill=notvlcolor,
                                           state=state
                                           )

                    self.not_visplines_list.extend([self.p7,
                                                   self.p8
                                                    ])
            # Below Vanishing Point and going down so top visible, bottom not
            else:
                # Bottom not visible (Reversed so BTM -> TOP)
                self.canvas.itemconfig(self.p7,
                                       fill=notvlcolor,
                                       state=state
                                       )
                self.canvas.itemconfig(self.p8,
                                       fill=notvlcolor,
                                       state=state
                                       )
                # Store not visible plines for future configurations.
                self.not_visplines_list = [self.p7,
                                           self.p8
                                           ]
        # Not Reversed Cuboid
        else:
            # Start below vanishing point - Going up (_y < startcoord[1])
            if self.startcoord[1] > vanishing_height:
                # Bottom not visible
                self.canvas.itemconfig(self.p7,
                                       fill=notvlcolor,
                                       state=state
                                       )
                self.canvas.itemconfig(self.p8,
                                       fill=notvlcolor,
                                       state=state
                                       )
                # Store not visible plines for future configurations.
                self.not_visplines_list = [self.p7,
                                           self.p8
                                           ]
                # Check if top is visible
                if self.back_topcorner[1] < vanishing_height:
                    # Top not visible
                    self.canvas.itemconfig(self.p5,
                                           fill=notvlcolor,
                                           state=state
                                           )
                    self.canvas.itemconfig(self.p6,
                                           fill=notvlcolor,
                                           state=state
                                           )

                    self.not_visplines_list.extend([self.p5,
                                                    self.p6
                                                    ])
            # Over Vanishing Point and going up so bottom visible, top not
            else:
                # Top not visible
                self.canvas.itemconfig(self.p5,
                                       fill=notvlcolor,
                                       state=state
                                       )
                self.canvas.itemconfig(self.p6,
                                       fill=notvlcolor,
                                       state=state
                                       )
                # Store not visible lines for future configurations.
                self.not_visplines_list = [self.p5,
                                           self.p6
                                           ]
        # Store visible lines for future configurations.
        self.vis_plines_list = [line for line in self.perspline_list
                                if line not in self.not_visplines_list]

    def lines_change(self,
                     line_list,
                     lcolor='black',
                     lstate='normal',
                     lwidth=1,
                     ldash=(),
                     loutline=''):
        """
        Changes style and visibility of lines passed in a list.


        ¤ PARAMETERS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯

            line_list : list
                List of lines that needs to be configurated.
            lcolor : str/hex code, ¤ OPTIONAL ¤
                Color of lines. Defaults to 'black'.
            lstate : str, ¤ OPTIONAL ¤
                Toggles visibility of lines. Defaults to 'normal'.
                Avaiable options: 'hidden'/'normal'
            lwidth : int, ¤ OPTIONAL ¤
                Width of line. Defaults to 1.
            ldash : tuple(int,int) ¤ OPTIONAL ¤
                Creates dash for line. (Fill/Space) Defaults to ().
            loutline : str/hex code ¤ OPTIONAL ¤
                Line's outline color. Defaults to ''.

        """
        for _ in line_list:
            self.canvas.itemconfig(_,
                                   fill=lcolor,
                                   state=lstate,
                                   width=lwidth,
                                   dash=ldash,
                                   outline=loutline
                                   )

    def lines_del(self, line_list):
        """
        Deletes lines that are in a list.

        ¤ PARAMETERS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯

            line_list : list
                List of lines that needs to be deleted.

        """
        for _ in line_list:
            self.canvas.delete(_)

    def walls_change(self,
                     walls_list,
                     wcolor='black',
                     wstate='normal',
                     wwidth=1,
                     wdash=(),
                     woutline=''):
        """
        Changes style and visibility of lines passed in a list.


        ¤ PARAMETERS
        ¯¯¯¯¯¯¯¯¯¯¯¯¯

            line_list : list
                List of lines that needs to be configurated.
            lcolor : str/hex code, ¤ OPTIONAL ¤
                Color of lines. Defaults to 'black'.
            lstate : str, ¤ OPTIONAL ¤
                Toggles visibility of lines. Defaults to 'normal'.
                Avaiable options: 'hidden'/'normal'
            lwidth : int, ¤ OPTIONAL ¤
                Width of line. Defaults to 1.
            ldash : tuple(int,int) ¤ OPTIONAL ¤
                Creates dash for line. (Fill/Space) Defaults to ().
            loutline : str/hex code ¤ OPTIONAL ¤
                Line's outline color. Defaults to ''.

        """
        for _ in walls_list:
            self.canvas.itemconfig(_,
                                   fill=wcolor,
                                   state=wstate,
                                   width=wwidth,
                                   dash=wdash,
                                   outline=woutline
                                   )

# TODO: Add 1-perspective cuboid options