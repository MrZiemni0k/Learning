
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os, os.path

root = Tk()

class SimpleTable(tk.Frame):
    def __init__(self, parent, rows, columns):
        
        tk.Frame.__init__(self, parent, background="black")
        self.tablecell = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                tablelabel = tk.Label(self, text="{}/{}".format(row, column), 
                                 borderwidth=0, width=10)
                tablelabel.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)
                current_row.append(tablelabel)
            self.tablecell.append(current_row)


        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        cell = self.tablecell[row][column]
        cell.configure(text=value)

    def get(self, row, column):
        cell = self.tablecell[row][column]
        return cell.cget()

    def filltable(self,row,column,header,dict):

        store_keys = list(dict.keys())
        print(store_keys)
        for x in range(0,row+1):

        	if x > len(store_keys):
        		break

        	else:
        		for y in range(0,column+1):

        			if y > len(dict[store_keys[x-1]]):
        				break

        			else:
        				if x == 0:
        					self.set(x,y,header[y])

        				elif x <= len(store_keys) and y == 0:
        					self.set(x,y,store_keys[x-1])

        				else:
 	      					self.set(x,y,dict[store_keys[x-1]][y-1])




class Application(tk.Frame):

    #imgdir = fd.askdirectory()
    filetypelist = ['.jpg', '.png', '.tiff']
    fromchosenfile = '.jpg'
    tochosenfile = '.png'
    typedic = {'.jpg':[0,0,0],'.png':[0,0,0],'.tiff':[0,0,0]} #Setting info display for user. Amount of files/Files' size
    													#If type of file is not found -> Convert option from the type will be removed.
    imgdir = os.getcwd()
    todelete = tk.BooleanVar()
    deltextinfo = tk.StringVar()

    todelete.set(False) 
    deltextinfo.set("")

    def __init__(self, master=None):

        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        

    def create_widgets(self):       

        self.theader = ["Type","Quantity","Size (MB)", "Avarage (KB)"]

        self.t = SimpleTable(self,len(self.filetypelist)+1,len(self.theader))
        self.t.pack(side="top", fill="x") 

        self.t.filltable(len(self.theader),len(self.filetypelist),self.theader,self.typedic)




        

        self.delonframe = LabelFrame(text="After conversion - Delete old files?")
        self.delonframe.pack()
        self.delonconv = Radiobutton(self.delonframe,variable=self.todelete,text="Yes",value=True,command=self.deleteonconvert).pack()
        self.notdelonconv = Radiobutton(self.delonframe,variable=self.todelete,text="No",value=False,command=self.deleteonconvert).pack()
        self.dellabel= Label(self.delonframe,textvariable=self.deltextinfo).pack()

        
      

        self.open_dir = tk.Button(self)
        self.open_dir["text"] = "Open DIR"
        self.open_dir["command"] = self.imgdirfunc
        self.open_dir.pack(side="top")

        self.entry_dir = tk.Entry(width=50)
        self.entry_dir.pack()
        self.entry_dir.insert(0,self.imgdir)
        
        self.testbtn = tk.Button(self, text="TEST",command=self.chck_for_pic)
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


    def imgdirfunc(self):

        print(self.imgdir)
        folder_path = StringVar() 
        self.imgdir = fd.askdirectory()
        folder_path.set(self.imgdir)
        self.entry_dir.delete(0,END)
        self.entry_dir.insert(0, self.imgdir)
        self.count_imgs()
        self.t.filltable(len(self.theader),len(self.filetypelist),self.theader,self.typedic)

        

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

    		if imfile.endswith('.jpg') or imfile.endswith('.jpeg'):
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

    
    	


    	
    	#selection = self.filetype.curselection()
    	#text = self.filetype.get(selection)
    	#cos = [self.filetype.get(selection) for selection in self.filetype.curselection()]
    	#print (self.filetypelist)
    	#print (text)
    	#print (cos)

        

app = Application(master=root)
app.mainloop()




