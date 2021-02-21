import tkinter as tk
from tkinter import font

fontlist=[
    ('Segoe UI', 9, 'normal'),
    ('Calibri', 12, 'bold'),        #Heading
    ('Calibri', 11, 'normal')       #Cells
    ]
clrpalette=[
    ["#222831","#393e46","#00adb5","#eeeeee"],
    ['#e7e6e1','#f7f6e7',"#f2a154","#314e52"],
    ["f7f7e8",'#c7cfb7',"#9dad7f","#557174"]
    ]
stylelist=[
    # bckg / txtclr / font / cell: height , width / border indicator / border width / relief / padx / pady
    [clrpalette[1][3],clrpalette[1][0],fontlist[1],"1","12","2px",2,"groove",0,0],
    [clrpalette[1][2],clrpalette[1][3],fontlist[2],"2","12","2px",2,"ridge",0,0]
    ]
    # Relief options: "flat", "raised", "sunken", "ridge", "solid", and "groove"
    
class SimpleTable(tk.Frame):
    '''
    Class to create a simple table using tkinter.Labels.
    ........

    Methods
    ----------
    tablestyle(min_row,max_row,min_column,max_column,style=stylist[0])
        Change styling for table cells
    set(row,column,value)
        Fill in a cell with a Text/Value

    filltable(header,dict)
        Fill in a table with titles(list) and its values(dictionary)

    '''

    def __init__(self, parent, rows, columns,border="black",_padx=0,_pady=0):
        '''
        Parameters:
        ------------
        parent:
            Set a parent to the table  S
        rows (int):
            Number of rows to be made
        columns (int):
            Number of columns to be made
        border (str)/hex:
            Colour of frame filling -> Table border
        _padx (int):
            Space between buttons -> Horizontal borders' thickness
        _pady (int):
            Space between buttons -> Vertical borders' thickness
        '''
        self.rows = rows
        self.columns = columns
        self.border = border
        self._padx = _padx
        self._pady = _pady
        
        tk.Frame.__init__(self, parent, background=border) 
        self.tablecell = []
        
        #Crate a table
        self.create_table()      
        #Set Head Style
        self.tablestyle(0,0,0,3)
        #Set Cells Style
        #self.tablestyle(1,3,0,3,stylelist[1])
        
    def create_table(self,issticky="nsew"):
        '''
        Function to create a table using __init parameters__
        ''' 
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                tablelabel = tk.Label(self, text="{}/{}".format(row, column), 
                                      borderwidth=2, 
                                      width=10
                                      )
                tablelabel.grid(row=row, 
                                column=column, 
                                sticky=issticky, 
                                padx=self._padx, 
                                pady=self._pady
                                )
                current_row.append(tablelabel)
            self.tablecell.append(current_row)

        #Setting weight for head table 
        self.rowconfigure(0, weight=2)  
        
        #Setting weight for the rest
        for row in range(1,self.rows):
            self.rowconfigure(row, weight=1)
        for column in range(0,self.rows):
            self.columnconfigure(row, weight=1)
        

    def tablestyle(self,min_row,max_row,min_column,max_column,style=stylelist[0]):
        '''
        Function to configure table cells
        from top left [min_row][min_column]
        to bottom right [max_row][max_column]
        Other Parameters:
        -----------------
        style (Default -> Stylelist[0])
            [bg: (Background)/str,
             fd: (Text Colour)/str,
             font: (Font Type, Size, Bold/Normal/Italic)/tup,
             height: (Cell height)/str(int),
             width: (Cell width)/str(int),
             bd: (Border around indicator)/str(int)+"px",
             borderwidth: (Border width)/int,
             relief (Relief of border)/str,
             padx: (Horizontal space)/int,
             pady: (Vertical space)/int]

        '''
        if min_row > max_row:
            raise Exception("min_row > max_row")
        elif min_column > max_column:
            raise Exception("min_column > max_column")
        else:
            for x in range(min_row,max_row+1):
                for y in range(min_column,max_column+1):
                    self.tablecell[x][y].config(bg=style[0],
                                                fg=style[1],
                                                font=style[2],
                                                height=style[3],
                                                width=style[4],
                                                bd=style[5],
                                                borderwidth=style[6],
                                                relief=style[7],
                                                padx=style[8],
                                                pady=style[9]
                                                )
        


    def set(self, row, column, value):
        """
        Function to edit value of a cell.
        Value = Text/Value to overwrite a cell.
        """
        cell = self.tablecell[row][column]
        cell.configure(text=value)


    def filltable(self,header,dict):
        '''
        Function to fill in a table with:
        header = List of table heads: 
                            Titles (Row[0]/Column[0:])
        dict = Dictionary: 
                            Keys   (Row[1:]/Column[0:])
                            Values (Row[1:]/Column[1:])
        Hints:
        For empty cell -> Value should be ""
        For empty cell at row[x]column[0] -> Key should start with ".empty"
                                             For example .empty1 / .empty2 / .empty3
        '''

        store_keys = list(dict.keys())
        for x in range(0,len(store_keys)+1):
            #For row in Dictionary Keys + 1(Header)

            for y in range(0,len(header)):
                #For column in Head List

                if x == 0:
                    #If Head Row
                    self.set(x,y,header[y])

                elif x <= len(store_keys) and y == 0:
                    #If (Row[1:]Column[0]) -> Keys

                    if store_keys[x-1].startswith(".empty"):
                        #Check if user wants empty cell at Column[0]
                        self.set(x,y,"")

                    else:
                        self.set(x,y,store_keys[x-1])


                else:
                    #(Row[1:]/Column[1:]) -> Values 
                    try:
                        self.set(x,y,dict[store_keys[x-1]][y-1])
                    except:
                        #Index Value not found within key. Cannot fill a cell if value does not exist.
                        raise Exception(f"Value not found at:\nDictionary: {dict}\nKey: {store_keys[x-1]}\nValue Index: {y-1}")