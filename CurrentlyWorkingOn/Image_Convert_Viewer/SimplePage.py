#TODO:Display format type options for avaiable format types. If there are no JPG not show JPG in listbox. - Convert From still not working.
     #Chck for if_corrct_entry in SimplePage class.
#TODO:Advanced Page.
#TODO:Advanved Image_Converter with Image_Viewing and multiple selection.
#TODO:Connection with PostgreSQL - tagging pictures and storing location(?) - if possible in database for machine learning.

import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk, messagebox, font
from PIL import ImageTk
from Classes import ImgConvert
import os, os.path
import glob
import AdvancedPage as _ap
                     
                                                           
class SimplePage(tk.Frame):
    '''
    Class to create a very simple page with Convert option.
    ........

    Methods
    ----------
    //LAYOUT//
    
    top_panel(tk.frame)
        Creating top panel with its contents.
    sub_panel(tk.frame)
        Creating sub panel with its contents.
    main_panel(tk.frame)
        Creating main panel with its contents.
    grid_layout(tk.frame)
        Layouting and setting weight for above and not mentioned frames.
        
    // COMMAND/EVENT FUNCTIONS // 
    
    if_corrct_entry(tk.entry.event)
        Event function mostly used for 1 image conversion.
        
    get_imgdir(tk.button.command)
        Command function to open WINDOWS GUI directory and store info into entry box provided by user.
        
    look_for_extensions()
        Checking directory for image extensions. 
        
    what_to_compress(tk.listbox.event)
        Event function for getting information from what type of file to compress.
        
    into_what(tk.listbox.event)
        Event function for getting information to what type of file to compress.
        
    change_page(tk.button.command)
         Command function to change layout to Advanced Page.
         
    deleteonconvert(tk.radiobutton.command)
        Command function for 'todelete' radio buttons.
        
    convert(tk.button.command)
        Function using ImgConvert class for converting image files.
    '''
    def __init__(self,parent=None, **kwargs):
        
        self.tuplefiletype = ('.jpg','.png','tiff')
        self.filetypelist = [_type for _type in self.tuplefiletype] #Supporting format type
        self.avaiabletypes = []
        self.fromchosenfile = None   #Convert From
        self.tochosenfile = None     #Conver To
        #self.typedic = {'.jpg':[0,0,0],'.png':[0,0,0],'.tiff':[0,0,0]} - For Advanced Page
        self.imgdir = os.getcwd()       #Current Directory
        
        
        self.todelete = tk.BooleanVar(parent) #Switch for permanently deleting files.
        self.todelete.set(False)
        
        self.deltextinfo = tk.StringVar(parent) #Caution info for Delete Frame
        self.deltextinfo.set("") 
        
        tk.Frame.__init__(self,parent, **kwargs)
        


        parent.title("Simple Converter")
        parent.geometry("400x400")
        self.top_panel()
        self.sub_panel()
        self.main_panel()
        #TODO:Organize rest Frames.
        self.f_status_panel = tk.Frame(self, bg="#ccf2f4")
        self.f_border1 = tk.Frame(self,bg="#557174")
        self.f_border2 = tk.Frame(self,bg="#557174")
        self.grid_layout()
        self.pack(fill="both",expand=True)
        self.look_for_extensions()
        
    #/////////////////////////////////////////////////////////
    #Layout functions
    #/////////////////////////////////////////////////////////
    
    #TODO: Style nicely. Fill Top Panel with something.    
    def top_panel(self):
        '''
        Creating and layouting top panel with:
                * Button to change from Simple to Advanced Page       
        '''  
              
        self.f_top_panel = tk.Frame(self,bg="#aaaaaa")
        
        #Button to change from Simple to Advanced Page     
        self.simple_adv_btn = tk.Button(self.f_top_panel,command=self.change_page,text="SP/AP")
        self.simple_adv_btn.grid(row=1,column=1,rowspan=1, columnspan=1,sticky="news")
        
    #TODO: Make Windows GUI directory show pictures - not only directories.
    def sub_panel(self):
        '''
        Creating and layouting sub panel with:
                * Functional entry box for directory location.
                (Functional means copy-paste and writing work - No need to use Open Dir button)
                * Button to open Windows Directory GUI.   
        '''
        
        self.f_sub_panel = tk.Frame(self,bg="#a4ebf3")
        
        #Entry directory box
        self.entry_dir = tk.Entry(self.f_sub_panel)
        self.entry_dir.grid(row=1,column=1,rowspan=1, columnspan=5,sticky="news")
        self.entry_dir.insert(0,self.imgdir)
        self.entry_dir.bind("<Return>",self.if_corrct_entry)
        
        #Button with WINDOWS GUI Directory
        self.open_dir = tk.Button(self.f_sub_panel,text="Open DIR",command=lambda:self.get_imgdir())
        self.open_dir.grid(row=1,column=7,rowspan=1, columnspan=1,sticky="news")

        #Weight configuration for window expanding.
        self.f_sub_panel.rowconfigure((0,1,2), weight=1)
        self.f_sub_panel.columnconfigure((1,2,3,4,5), weight=3)
        self.f_sub_panel.columnconfigure((0,6,7,8), weight=1)
        
    def main_panel(self):
        '''
        Creating and layouting main panel with:
                Listboxes(Format types) with its labels
                Radio buttons in a 'delonframe' frame (Delete used files?)
                Start button to begin conversion process.        
        '''
        
        self.f_main_panel = tk.Frame(self,bg="#f4f9f9")
        
        #Label "FROM"
        self.l_from = tk.Label(self.f_main_panel,text="From",bg="#f4f9f9")
        self.l_from.grid(row=0,column=1,rowspan=1, columnspan=1,sticky="news")
        
        #Label "TO"
        self.l_to = tk.Label(self.f_main_panel,text="To",bg="#f4f9f9")
        self.l_to.grid(row=0,column=3,rowspan=1, columnspan=1,sticky="news")
        
        #Listbox ConvertFrom
        self.convertfrom = tk.Listbox(self.f_main_panel, selectmode=tk.BROWSE, exportselection = 0)
        self.convertfrom.grid(row=1,column=1,rowspan=1, columnspan=1,sticky="news")
        for x in self.avaiabletypes:
        	self.convertfrom.insert(tk.END, x)
       	self.convertfrom.bind("<<ListboxSelect>>",self.what_to_compress)
       	self.convertfrom.select_set(0)

        #Listbox Convert_To
       	self.convert_to = tk.Listbox(self.f_main_panel, selectmode=tk.BROWSE, exportselection = 0)
        self.convert_to.grid(row=1,column=3,rowspan=1, columnspan=1,sticky="news")
        for x in self.filetypelist:
        	self.convert_to.insert(tk.END, x)
       	self.convert_to.bind("<<ListboxSelect>>",self.into_what)
       	self.convert_to.select_set(1)
        
        #Delonframe for radio buttons
        self.delonframe = tk.LabelFrame(self.f_main_panel,text="Delete old files?")
        self.delonframe.grid(row=3,column=1,rowspan=1, columnspan=1,sticky="news")
        
        #Delete button
        self.delonconv = tk.Radiobutton(self.delonframe,variable=self.todelete,text="Yes",value=True,command=self.deleteonconvert)
        self.delonconv.pack()
        
        #Not_Delete button
        self.notdelonconv = tk.Radiobutton(self.delonframe,variable=self.todelete,text="No",value=False,command=self.deleteonconvert)
        self.notdelonconv.pack()
        
        #TODO: Style LABEL to make warning more noticable        
        #Warning Label about permanently removing files.
        self.dellabel= tk.Label(self.delonframe,textvariable=self.deltextinfo)
        self.dellabel.pack()   
        
        #Start Button
        self.start_btn = tk.Button(self.f_main_panel,text="Start",command=lambda:self.convert(),bg="#557174",fg="#f4f9f9")  
        self.start_btn.grid(row=3,column=3,rowspan=1, columnspan=1,sticky="news")
        
        #Weight configuration for window expanding.
        self.f_main_panel.rowconfigure((0,1,2,3,4,5), weight=1)
        self.f_main_panel.columnconfigure((1,2,3), weight=1)
        self.f_main_panel.columnconfigure((0,5), weight=3)
        
    #TODO: Style nicely 
    def grid_layout(self):
        '''
        Setting up layout by grid. 
        '''
        self.f_top_panel.grid(row=0, column=0, rowspan=1, columnspan=10, sticky="news")
        self.f_sub_panel.grid(row=1, column=1, rowspan=1, columnspan=8, sticky="news")
        
        self.f_border1.grid(row=1, column=0, rowspan=8, columnspan=1, sticky="news")
        self.f_border2.grid(row=1, column=9, rowspan=8, columnspan=1, sticky="news")
        
        self.f_main_panel.grid(row=2, column=1, rowspan=7, columnspan=8, sticky="news")
        self.f_status_panel.grid(row=9, column=0, rowspan=1, columnspan=10, sticky="news")

        self.rowconfigure((0,1,9), weight=2)
        self.columnconfigure((0,1,9), weight=2)

        for r in range(2,9):
            self.rowconfigure(r, weight=5)
        for c in range(2,9):
            self.columnconfigure(c, weight=4)
        
    #/////////////////////////////////////////////////////////
    #Command/Event Functions
    #/////////////////////////////////////////////////////////
       
    #TODO: Improve func for img type list expansion
    def if_corrct_entry(self,event):
        '''
        Event function mostly used to convert only 1 picture instead of many.
        Will be more useful for Advanvced Page.
        '''
        self.imgdir = self.entry_dir.get()
        if os.path.isdir(self.imgdir):
            pass
            #self.count_imgs()
            #self.t.filltable(self.theader,self.typedic)
        elif os.path.isfile(self.imgdir):
            if self.imgdir.endswith(('.jpg',".png",'.jpeg','.tiff')):
                pass
            else:
                messagebox.showinfo(
                    title="Wrong Format", 
                    message="The file is not supported by programm.\nSupported file types: .jpg, .png, .tiff"
                    )
    def get_imgdir(self):
        '''
        Command function to open WINDOWS GUI directory and store info into entry box provided by user.
        '''
        self.filetypelist = [x for x in self.tuplefiletype]
        self.avaiabletypes = []
        folder_path = tk.StringVar() 
        self.imgdir = fd.askdirectory()
        folder_path.set(self.imgdir)
        self.entry_dir.delete(0,tk.END)
        self.entry_dir.insert(0, self.imgdir)
        
        self.look_for_extensions()
        self.refresh_listbox()
        
    
    def look_for_extensions(self):
        '''
        Checking directory for image extensions. If found adding them to list which will be used for listboxes in mainpanel.
        '''   
        print(self.imgdir)
        for file in glob.glob(self.imgdir+'/*'):
            if file.lower().endswith(('.jpg','.png','.tiff')):
                if os.path.isfile(file):
                    ext = os.path.splitext(file)[-1].lower()
                    if ext not in self.avaiabletypes:
                        self.avaiabletypes.append(ext)
                        if len(self.avaiabletypes)==3:
                            break
        self.avaiabletypes.sort()

    def refresh_listbox(self):
        #For No Img Files - Clear List Boxes
        if len(self.avaiabletypes) == 0:
            self.fromchosenfile = None
            self.tochosenfile = None
            self.convert_to.delete(0,tk.END)
            self.convertfrom.delete(0,tk.END)
            print(self.fromchosenfile)
            print(self.tochosenfile)
            
        #For 1 Img Type File - Clear Box/Make 1 option avaiable in ConvertFrom Listbox/Automatic choice   
        elif len(self.avaiabletypes) <= 1:
            
            #Set types and delete file type to avoid conversion to same type.
            self.fromchosenfile = self.avaiabletypes[0]
            self.filetypelist.remove(self.fromchosenfile)
            self.tochosenfile = self.filetypelist[0]
            
            #Refresh lists
            self.convert_to.delete(0,tk.END)
            for x in self.filetypelist:
        	    self.convert_to.insert(tk.END, x)
             
            self.convertfrom.delete(0,tk.END)
            for x in self.avaiabletypes:
        	    self.convertfrom.insert(tk.END, x)
            
            #Refresh selection 
            self.convertfrom.selection_clear(0,tk.END)
            self.convertfrom.select_set(0)
            
            self.convert_to.selection_clear(0,tk.END)
            self.convert_to.select_set(0)
            
            print(self.fromchosenfile)
            print(self.tochosenfile)
            
        else:
            self.convertfrom.delete(0,tk.END)
            for x in self.avaiabletypes:
        	    self.convertfrom.insert(tk.END, x)
             
            self.convert_to.delete(0,tk.END)
            for x in self.filetypelist:
        	    self.convert_to.insert(tk.END, x)
            self.fromchosenfile = self.avaiabletypes[0]
            self.tochosenfile = self.filetypelist[0]
             
            self.chck_listbox_imgtypes()
             

    def chck_listbox_imgtypes(self):
        
        if self.fromchosenfile == self.tochosenfile:

            self.convert_to.selection_clear(0,tk.END)
            
            if self.filetypelist.index(self.fromchosenfile) == 0:
                
                self.convert_to.select_set(1)
                self.tochosenfile = self.filetypelist[1]
                
            else:
                
                self.convert_to.select_set(0)
                self.tochosenfile = self.filetypelist[0]    
                                  
    #TODO: Improve func for img type list expansion
    def what_to_compress(self,event):
        '''
        Event function to change format type from which conversion should be done. Used for convertfrom listbox in main panel.
        Also changes convert_to listbox selection when choice would the same - Avoiding convsion to same format.
        '''
        
        self.fromchosenfile = self.convertfrom.get(self.convertfrom.curselection())
        self.chck_listbox_imgtypes()
        

    #TODO: Improve func for img type list expansion
    def into_what(self,event):
        '''
        Event function to change format type to which conversion should be done. Used for convert_to listbox in main panel.
        Also changes convertfrom listbox selection when choice would the same - Avoiding convsion to same format.
        '''

        self.tochosenfile = self.convert_to.get(self.convert_to.curselection()) 

        if self.tochosenfile == self.fromchosenfile:

            self.convertfrom.selection_clear(0,tk.END)
            inx = self.filetypelist.index(self.tochosenfile)
            
            if inx == 0:
                
                self.convertfrom.select_set(1)
                self.tochosenfile = self.filetypelist[1]
                
            else:
                
                self.convertfrom.select_set(0)
                self.tochosenfile = self.filetypelist[0]
                
    def change_page(self):
        '''
        Command function to change layout to Advanced Page
        '''
        self.master.change(_ap.AdvancedPage)
        
    def deleteonconvert(self):
        '''
        Command function for 'todelete' radio buttons.
        '''
        
        if self.todelete.get():
            self.deltextinfo.set("Files will be permamently deleted!")
        else:
            self.deltextinfo.set("")
      
    def convert(self):
        '''
        Function using ImgConvert module class for converting image files.
        '''
        
        result = True #Abstract parameter for continuing with conversion.
        
        if self.todelete.get(): #Ask one more time if continue with permanently removing used files.
            
            result = tk.messagebox.askyesno(title='CAUTION', message='After conversion used files will be deleted. Continue?\nDelete option will be automatically switched to off if "NO" is chosen.')
        
        if result: #Convert
            
            conv = ImgConvert.ImgConvert(self.fromchosenfile,self.tochosenfile,self.entry_dir.get(),self.todelete.get())
            conv.convert()
            tk.messagebox.showinfo(title='Conversion completed', message=f"Successfully converted {conv.img_count} images to {self.tochosenfile}")
        
        else: #Automatically set 'todelete' radio button on False.
            
            self.deltextinfo.set("")
            self.todelete.set(False)
 