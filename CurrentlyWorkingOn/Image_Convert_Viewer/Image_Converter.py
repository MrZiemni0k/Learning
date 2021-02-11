# Uporzadkowanie kodu
# Do zrobienia - Listbox dla plikow 
# Filtr do listboxa - wyswietlic np tylko jpg / jpegi
# Zaznaczenie pliku konwertuje insert - zmienia rowniez obraz w nowym oknie
# Kompresja obrazu 
# Dodac opcje .svg jezeli mozliwy convert
# Dodac guzik do convertu
# Napisac kod do convertu
# Zabawic sie w "CSS"



import tkinter as tk
from tkinter import filedialog as fd
from tkinter import *
from tkinter import ttk, messagebox, font
from PIL import Image,ImageTk
import os, os.path

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
            Set a parent to the table  
        rows (int):
            Number of rows to be made
        columns (int):
            Number of columns to be made

        '''
        tk.Frame.__init__(self, parent, background="black") #background=border
        self.tablecell = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                tablelabel = tk.Label(self, text="{}/{}".format(row, column), 
                                 borderwidth=2, width=10)
                tablelabel.grid(row=row, column=column, sticky="nsew", padx=_padx, pady=_pady)
                current_row.append(tablelabel)
            self.tablecell.append(current_row)




        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

        self.tablestyle(0,0,0,3)
        self.tablestyle(1,3,0,3,stylelist[1])

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






class Application(tk.Frame):

    imgdir = os.getcwd()




    def __init__(self, master=None):

        super().__init__(master)
        #imgdir = fd.askdirectory()
        self.filetypelist = ['.jpg', '.png', '.tiff']
        self.fromchosenfile = '.jpg'
        self.tochosenfile = '.png'
        self.typedic = {'.jpg':[0,0,0],'.png':[0,0,0],'.tiff':[0,0,0,0]} #Setting info display for user. Amount of files/Files' size
        												#If type of file is not found -> Convert option from the type will be removed.
        self.todelete = tk.BooleanVar(self.master)
        self.deltextinfo = tk.StringVar(self.master)

        self.todelete.set(False) 
        self.deltextinfo.set("")
        self.master = master
        self.pack()
        self.create_widgets()

    def getimgdir(self):
    	return self.imgdir
        

    def create_widgets(self):       

        self.theader = ["Type","Quantity","Size (MB)", "Avarage (KB)",]

        a = self.typedic.keys()
        b = list(a)
        print(a)
        print(b)

        self.t = SimpleTable(self,len(b)+1,len(self.theader),"#9dc8c9")
        self.t.pack(side="top", fill="x") 

        self.t.filltable(self.theader,self.typedic)




        

        self.delonframe = LabelFrame(text="After conversion - Delete old files?")
        self.delonframe.pack()
        self.delonconv = Radiobutton(self.delonframe,variable=self.todelete,text="Yes",value=True,command=self.deleteonconvert)
        self.delonconv.pack()
        self.notdelonconv = Radiobutton(self.delonframe,variable=self.todelete,text="No",value=False,command=self.deleteonconvert)
        self.notdelonconv.pack()
        self.dellabel= Label(self.delonframe,textvariable=self.deltextinfo)
        self.dellabel.pack()

        
      

        self.open_dir = tk.Button(self)
        self.open_dir["text"] = "Open DIR"
        self.open_dir["command"] = self.imgdirfunc
        self.open_dir.pack(side="top")

        self.entry_dir = tk.Entry(width=50)
        self.entry_dir.pack()
        self.entry_dir.insert(0,self.imgdir)
        self.entry_dir.bind("<Return>",self.tescik)
        
        self.testbtn = tk.Button(self, text="TEST",command=lambda : NewWindow(root))
        self.testbtn.pack()

        self.testbtn2 = tk.Button(self, text="TEST",command=self.what_to_compress)
        self.testbtn2.pack()
        

        self.convertfrom = tk.Listbox(self, selectmode=BROWSE, exportselection = 0)
        self.convertfrom.pack()
        for x in self.filetypelist:
        	self.convertfrom.insert(END, x)
       	self.convertfrom.bind("<<ListboxSelect>>",self.what_to_compress)
       	self.convertfrom.select_set(0)


       	self.convert_to = tk.Listbox(self, selectmode=BROWSE, exportselection = 0)
        self.convert_to.pack(expand=True,fill="both")
        for x in self.filetypelist[:2]:
        	self.convert_to.insert(END, x)
       	self.convert_to.bind("<<ListboxSelect>>",self.into_what)
       	self.convert_to.select_set(1)


        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def tescik(self,event):
        self.imgdir = self.entry_dir.get()
        if os.path.isdir(self.imgdir):
        	print("True")
        	print("Enteruje")
        	self.count_imgs()
        	self.t.filltable(self.theader,self.typedic)
        elif os.path.isfile(self.imgdir):
        	if self.imgdir.endswith(('.jpg',".png",'.jpeg','.tiff')):
        		print("Mam zdjecie")
        	else:
        		print("Exists")
        		messagebox.showinfo(
        			title="Wrong Format", 
        			message="The file is not supported by programm.\nSupported file types: .jpg, .png, .tiff"
        			)

        else:	
        	print("False")
        	messagebox.showerror(
        		title="Path not Found", 
        		message="Path/File could not be found."
        		)



    def imgdirfunc(self):

        print(self.imgdir)
        folder_path = StringVar() 
        self.imgdir = fd.askdirectory()
        folder_path.set(self.imgdir)
        self.entry_dir.delete(0,END)
        self.entry_dir.insert(0, self.imgdir)
        self.count_imgs()
        self.t.filltable(self.theader,self.typedic)

        

    def chck_for_pic(self):

    	file_num = len([imfile for imfile in os.listdir(self.imgdir)])


    def what_to_compress(self,event):

    	print("From: " + self.fromchosenfile + " to" + self.tochosenfile )
    	self.fromchosenfile = self.convertfrom.get(self.convertfrom.curselection()) 
    	
    	if self.fromchosenfile == ".jpg":

    		self.convert_to.selection_clear(0,END)
    		self.convert_to.select_set(1)
    		self.tochosenfile = '.png'

    	elif self.fromchosenfile == ".png":

    		self.convert_to.selection_clear(0,END)
    		self.convert_to.select_set(0)
    		self.tochosenfile = '.jpg'
    	print("From: " + self.fromchosenfile + " to" + self.tochosenfile )
    

    def into_what(self,event):

    	print("From: " + self.fromchosenfile + " to" + self.tochosenfile )
    	self.tochosenfile = self.convert_to.get(self.convert_to.curselection()) 
    	
    	if self.fromchosenfile != ".tiff":

    		if self.tochosenfile == ".jpg":

    			self.convertfrom.selection_clear(0, tk.END)
    			self.convertfrom.select_set(1)
    			self.fromchosenfile = '.png'

    		elif self.tochosenfile == ".png":

    			self.convertfrom.selection_clear(0, tk.END)
    			self.convertfrom.select_set(0)
    			self.fromchosenfile = '.jpg'

    	print("From: " + self.fromchosenfile + " to" + self.tochosenfile )

    def count_imgs(self):

    	self.typedic[".jpg"]=[0,0,0]
    	self.typedic[".png"]=[0,0,0]
    	self.typedic[".tiff"]=[0,0,0]

    	for imfile in os.listdir(self.imgdir):
    		imfile = imfile.lower()

    		if imfile.endswith(('.jpg','.jpeg')):
    			self.typedic[".jpg"][0] += 1
    			self.typedic[".jpg"][1] += os.path.getsize(self.imgdir+'/'+imfile)/1024/1024			#Round Up did not work for .jpg.

    		elif imfile.endswith('.png'):
    			self.typedic[".png"][0] += 1
    			self.typedic[".png"][1] += round((os.path.getsize(self.imgdir+'/'+imfile))/1024/1024,2)

    		elif imfile.endswith('.tiff'):
    			self.typedic[".tiff"][0] += 1
    			self.typedic[".tiff"][1] += round((os.path.getsize(self.imgdir+'/'+imfile))/1024/1024,2)

    	self.typedic[".jpg"][1] = round(self.typedic[".jpg"][1],2) #This round up works

    	if self.typedic[".jpg"][0] != 0:
    		self.typedic[".jpg"][2] = round(self.typedic[".jpg"][1]/self.typedic[".jpg"][0]*1024,2)

    	if self.typedic[".png"][0] != 0:
    		self.typedic[".png"][2] = round(self.typedic[".png"][1]/self.typedic[".png"][0]*1024,2)

    	if self.typedic[".tiff"][0] != 0:
    		self.typedic[".tiff"][2] = round(self.typedic[".tiff"][1]/self.typedic[".tiff"][0]*1024,2)

    def populateinfo(self):
    	
    	print(self.typedic)

    	#x = 0

    	#for record in self.infotree.get_children():
    		#self.infotree.item(record,values=(self.typedic[self.filetypelist[x]][0],self.typedic[self.filetypelist[x]][1]))
    		#x+=1

    	#self.infotree.item(values=self.typedic[img_type][0],self.typedic[img_type][1])

    	

    def deleteonconvert(self):

    	if self.todelete.get():
    		self.deltextinfo.set("Files will be permamently deleted!")
    	else:
    		self.deltextinfo.set("")

class NewWindow(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("New Window") 
        self.geometry("200x200")
        print(app.getimgdir())
        someimg =ImageTk.PhotoImage(Image.open(app.getimgdir()))
        label = Label(self, image =someimg) 
        label.pack()
        self.mainloop()    
    	


    	
    	#selection = self.filetype.curselection()
    	#text = self.filetype.get(selection)
    	#cos = [self.filetype.get(selection) for selection in self.filetype.curselection()]
    	#print (self.filetypelist)
    	#print (text)
    	#print (cos)

        
root = Tk()
app = Application(master=root)
app.mainloop()




