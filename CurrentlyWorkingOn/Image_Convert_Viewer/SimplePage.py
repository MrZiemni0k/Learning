
#TODO: Prepare some icons for buttons.
#TODO: Style
#TODO: Repair a bug when exiting from WINDOWS DIR GUI -> Entrybox -> it fills listboxes with variables.


import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
from Classes import ImgConvert
import os, os.path
import glob
import AdvancedPage as _ap
from Classes import SimpleTable as _st
from Classes import StoreInfo as _si
import time
from PIL import Image, ImageTk
                     
                                                           
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
    
    chck_entrybox(tk.entry.event)
        Event function mostly used for 1 image conversion.
        
    get_imgdir(tk.button.command)
        Command function to open WINDOWS GUI directory and store info into entry box provided by user.
        
    look_for_extensions()
        Checking directory for image extensions. 
        
    from_what(tk.listbox.event)
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
    def __init__(self,parent=None):
        
        self.tuplefiletype = ('.jpg','.png','.tiff')
        self.create_filetypelist()
        self.fromchosenfile = None   #Convert From
        self.tochosenfile = None     #Conver To
        
        self.imgdir = os.getcwd()     #Current Directory
        
        self.todelete = tk.BooleanVar(parent) #Switch for permanently deleting files.
        self.todelete.set(False)
        
        self.deltextinfo = tk.StringVar(parent) #Caution info for Delete Frame
        self.deltextinfo.set("")
        
        self.refresh_data()
        

        
        tk.Frame.__init__(self,parent,bg='#c7cfb7')
        


        parent.title("Simple Converter")
        parent.geometry("1000x600")
        self.top_panel()
        self.sub_panel()
        self.main_panel()

        self.f_status_panel = tk.Frame(self, bg="#f2f4ff")
        self.f_border1 = tk.Frame(self,bg="#f2f4ff")
        self.f_border2 = tk.Frame(self,bg="#f2f4ff")
        self.grid_layout()
        self.pack(fill="both",expand=True)

        self.refresh_listbox()

        
    #/////////////////////////////////////////////////////////
    #Layout functions
    # 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 
    # 10 |   BTN   |     ENTRY BOX     | DIR BTN | 19
    # 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 
    # 30 |   BG    |                   |   BG    | 39 
    # 40 |   BG    |                   |   BG    | 49 
    # 50 |   BG    |     Main Panel    |   BG    | 59 
    # 60 |   BG    |                   |   BG    | 69 
    # 70 |   BG    |                   |   BG    | 79 
    # 80 |   BG    |                   |   BG    | 89 
    # 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99  
    #/////////////////////////////////////////////////////////
       
    def top_panel(self):
        '''
        Creating and layouting top panel with:
      
        '''       
        self.f_top_panel = tk.Frame(self,bg="#f2f4ff")
        self.f_space_panel = tk.Frame(self,bg="#c7cfb7")
            
    def sub_panel(self):
        '''
        Creating and layouting sub panel with:
                * Button to change from Simple to Advanced Page 
                * Functional entry box for directory location.
                (Functional means copy-paste and writing work - No need to use Open Dir button)
                * Button to open Windows Directory GUI.                                  
        '''
        
        #Divide Panel onto 3. Left // Center  // Right
        self.f_sub_panel_left = tk.Frame(self,bg='#6c756b',bd=2, relief='groove')
        self.f_sub_panel_left.grid(row=1, column=1, rowspan=1, columnspan=2, sticky="news")
        
        self.f_sub_panel_center = tk.Frame(self,bg='#6c756b',bd=2, relief='groove')
        self.f_sub_panel_center.grid(row=1, column=3, rowspan=1, columnspan=4, sticky="news")
        
        self.f_sub_panel_right = tk.Frame(self,bg='#6c756b',bd=2, relief='groove')
        self.f_sub_panel_right.grid(row=1, column=7, rowspan=1, columnspan=2, sticky="news")
        
        #//////////////////////
        #Sub Panel - Left
        #//////////////////////
        self.f_sub_panel_left.rowconfigure((0,2), weight=1)
        self.f_sub_panel_left.rowconfigure((1), weight=2)
        self.f_sub_panel_left.columnconfigure((0,2), weight=1)
        self.f_sub_panel_left.columnconfigure((1), weight=2)
        
        #Button to change from Simple to Advanced Page     
        self.simple_adv_btn = tk.Button(self.f_sub_panel_left,command=self.change_page,text="Main")
        self.simple_adv_btn.grid(row=1,column=1,rowspan=1, columnspan=1,sticky="news")
        
        #//////////////////////
        #Sub Panel - Center
        #//////////////////////
        
        self.f_sub_panel_center.rowconfigure((0,2), weight=1)
        self.f_sub_panel_center.rowconfigure((1), weight=2)
        self.f_sub_panel_center.columnconfigure((0,5), weight=1)
        self.f_sub_panel_center.columnconfigure((1,2,3,4), weight=5)
        
        #Entry directory box
        self.entry_dir = tk.Entry(self.f_sub_panel_center)
        self.entry_dir.grid(row=1,column=1,rowspan=1, columnspan=4,sticky="news")
        self.entry_dir.insert(0,self.imgdir)
        self.entry_dir.bind("<Return>",self.chck_entrybox)
        
        #Button with WINDOWS GUI Directory
        self.open_dir = tk.Button(self.f_sub_panel_right,text="Open DIR",command=lambda:self.get_imgdir())
        self.open_dir.grid(row=1,column=1,rowspan=1, columnspan=1,sticky="news")

        self.f_sub_panel_right.rowconfigure((0,2), weight=1)
        self.f_sub_panel_right.rowconfigure((1), weight=2)
        self.f_sub_panel_right.columnconfigure((0,2), weight=1)
        self.f_sub_panel_right.columnconfigure((1), weight=2)

    #/////////////////////////////////////////////////////////
    #Main Panel
    # 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 
    # 10 | 11 | 12 |       Table       | 17 | 18 | 19
    # 20 | 21 | 22 |                   | 27 | 28 | 29 
    # 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 
    # 40 |   DEL   |  LBL    |   LBL   | 47 | 48 | 49 
    # 50 |   DEL   |  LSTBOX | LSTBOX  | 57 | 58 | 59 
    # 60 |   DEL   |         |         |  Start  | 69 
    # 70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 
    # 80 |             Progress Bar              | 89 
    # 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99  
    #/////////////////////////////////////////////////////////    
    def main_panel(self):
        '''
        Creating and layouting main panel with:
                Listboxes(Format types) with its labels
                Radio buttons in a 'delonframe' frame (Delete used files?)
                Start button to begin conversion process.        
        '''
        
        self.f_main_panel = tk.Frame(self,bg="#dbe4ee")
        
        #Table with info:
        self.refresh_table()              
        
        #Label "FROM"
        self.l_from = tk.Label(self.f_main_panel,text="From",bg="#96c5f7")
        self.l_from.grid(row=4,column=3,rowspan=1, columnspan=2,sticky="news")
        
        #Label "TO"
        self.l_to = tk.Label(self.f_main_panel,text="To",bg="#f4f9f9")
        self.l_to.grid(row=4,column=5,rowspan=1, columnspan=2,sticky="news")
        
        #Listbox Convert_From
        self.convert_from = tk.Listbox(self.f_main_panel, selectmode=tk.BROWSE, exportselection = 0)
        self.convert_from.grid(row=5,column=3,rowspan=2, columnspan=2,sticky="news")
       	self.convert_from.bind("<<ListboxSelect>>",self.from_what)

        #Listbox Convert_To
       	self.convert_to = tk.Listbox(self.f_main_panel, selectmode=tk.BROWSE, exportselection = 0)
        self.convert_to.grid(row=5,column=5,rowspan=2, columnspan=2,sticky="news")
        self.convert_to.bind("<<ListboxSelect>>",self.into_what)
        
        #Delonframe for radio buttons
        self.delonframe = tk.LabelFrame(self.f_main_panel,text="Delete old files?")
        self.delonframe.grid(row=15,column=17,rowspan=1, columnspan=2,sticky="news")
        
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
        self.start_pixel_img = Image.open("E:\\Learning\\Learning\\CurrentlyWorkingOn\\Image_Convert_Viewer\\Icons\\Start_Pixel2small.png")
        self.start_pixel_img = ImageTk.PhotoImage(self.start_pixel_img)
        self.start_btn = ttk.Button(self.f_main_panel,text="Convert",command=lambda:self.convert())  
        self.start_btn.grid(row=16,column=17,rowspan=2, columnspan=2,sticky="news")
        #Weight configuration for window expanding.
        self.f_main_panel.rowconfigure((0,3,7,9,10,11,12,13,14,15,16,17,18,19), weight=2)
        self.f_main_panel.rowconfigure((1,2,4,5,6,8), weight=3)
        self.f_main_panel.columnconfigure((0,9), weight=2)
        self.f_main_panel.columnconfigure((1,2,3,4,5,6,7,8), weight=3)
        
    #TODO: Style nicely 
    def grid_layout(self):
        '''
        Setting up layout by grid. 
        '''
        self.f_top_panel.grid(row=0, column=0, rowspan=1, columnspan=10, sticky="news")
        self.f_space_panel.grid(row=2, column=0, rowspan=1, columnspan=10, sticky="news")
        
        self.f_border1.grid(row=1, column=0, rowspan=8, columnspan=1, sticky="news")
        self.f_border2.grid(row=1, column=9, rowspan=8, columnspan=1, sticky="news")
        
        self.f_main_panel.grid(row=3, column=3, rowspan=6, columnspan=4, sticky="news")
        self.f_status_panel.grid(row=9, column=0, rowspan=1, columnspan=10, sticky="news")

        self.rowconfigure((0,2,9), weight=1)
        self.rowconfigure((1), weight=2)
        self.rowconfigure((3,4,5,6,7,8), weight=3)
        self.columnconfigure((0,1,2,3,7,8,9), weight=3)
        for c in range(4,7):
            self.columnconfigure(c, weight=4)
        
    #/////////////////////////////////////////////////////////
    #Command/Event Functions
    #/////////////////////////////////////////////////////////
    def btn_script(self):
        '''
        Copy-paste func to not repeat code -> Used to block BTN.
        '''
        return(
            self.tochosenfile in self.tuplefiletype and
            self.fromchosenfile in self.tuplefiletype and 
            (
            self.entry_dir.get().lower().endswith(self.tuplefiletype) or
            os.path.isdir(self.entry_dir.get())
            ) 
           )

    def change_page(self):
        '''
        Command function to change layout to AdvancedPage (Module)
        '''
        self.master.change(_ap.AdvancedPage)
      
    def chck_entrybox(self,event):
        '''
        Event function mostly used to convert only 1 picture instead of many.
        Will be more useful for Advanvced Page.
        '''
        self.imgdir = self.entry_dir.get()
        if os.path.isfile(self.imgdir):
            if self.imgdir.lower().endswith(self.tuplefiletype):
                self.avaiabletypes = [os.path.splitext(self.imgdir)[-1].lower()]
                self.create_filetypelist()
                self.refresh_listbox()
                
            else:
                tk.messagebox.showinfo(
                    title="Wrong Format", 
                    message="The file is not supported by programm.\nSupported file types: .jpg, .png, .tiff"
                    )
        else:
            tk.messagebox.showinfo(
                    title="File not found", 
                    message="Please make sure dir path or file path is provided correctly"
                    )
         
    def chck_listbox_imgtypes(self):
        '''
        Checks if same file conversion is chosen. 
        For True automaticaly swithces to other option to avoid conversing images to same type.
        '''
        if self.fromchosenfile == self.tochosenfile:

            self.convert_to.selection_clear(0,tk.END)
            
            if self.listfiletype.index(self.fromchosenfile) == 0:
                
                self.convert_from.select_set(0)
                self.convert_to.select_set(1)
                self.tochosenfile = self.listfiletype[1]
                
            else:
                
                self.convert_from.select_set(1)
                self.convert_to.select_set(0)
                self.tochosenfile = self.listfiletype[0]                                               
    
    def convert(self):
        '''
        Function using ImgConvert module class for converting 1 or all image files.
        ''' 
        
        result = True #Abstract parameter for continuing with conversion.
        
        #Check if files exist - For example someone added sth to entry box and such path does not exist.
        if self.btn_script():
            pass    
        else:
            self.avaiabletypes = []
            self.refresh_listbox()
            return(tk.messagebox.showinfo(
                    title="Path not correct!", 
                    message="Please make sure dir path or file path is provided correctly"
                    )
            )
        
            
        conv = ImgConvert.ImgConvert(self.fromchosenfile,self.tochosenfile,self.entry_dir.get(),self.todelete.get())       
        
        #Ask if continue with permanently removing used files.
        if self.todelete.get(): 
            
            result = tk.messagebox.askyesno(title='CAUTION', message='After conversion used files will be deleted. Continue?\nDelete option will be automatically switched to off if "NO" is chosen.')
        
        #Convert 1 image
        if result and self.entry_dir.get().lower().endswith(self.tuplefiletype): 
              
            conv.convert_one()
            if conv.img_count:
                tk.messagebox.showinfo(title='Conversion completed', message=f"Successfully converted image from {self.fromchosenfile} to {self.tochosenfile}")

        #Convert all images
        elif result:
                
            conv.convert_all()
            if conv.img_count:
                tk.messagebox.showinfo(title='Conversion completed', message=f"Successfully converted {conv.img_count} images to {self.tochosenfile}")
        
        else: #Automatically set 'todelete' radio button on False.
            
            self.deltextinfo.set("")
            self.todelete.set(False)

    def create_dict(self):
        
        self._typedic = {}
        for _type in self.avaiabletypes:
            self._typedic[_type] = [0,0,0]

    def create_filetypelist(self):
        self.listfiletype = [x for x in self.tuplefiletype]
        self.listfiletype.sort()
        
    def deleteonconvert(self):
        '''
        Command function for 'todelete' radio buttons.
        '''
        
        if self.todelete.get():
            self.deltextinfo.set("Files will be permamently deleted!")
        else:
            self.deltextinfo.set("")
    
    def from_what(self,event):
        '''
        Event function to change format type from which conversion should be done. Used for convert_from listbox in main panel.
        Also changes convert_to listbox selection when choice would the same - Avoiding conversion to same format.
        '''
        self.fromchosenfile = self.convert_from.get(self.convert_from.curselection())
        self.chck_listbox_imgtypes()
                        
    def get_imgdir(self):
        '''
        Command function to open WINDOWS GUI directory and store info into entry box provided by user.
        '''

        folder_path = tk.StringVar() 
        self.imgdir = fd.askdirectory()
        folder_path.set(self.imgdir)
        self.entry_dir.delete(0,tk.END)
        self.entry_dir.insert(0, self.imgdir)
        
        
        self.loadinglabel = tk.Label(self.f_main_panel,text="Loading")
        self.loadinglabel.grid(row=0,column=0,rowspan=3,columnspan=3,sticky="news")
        
        time.sleep(0.2)
        self.create_filetypelist()
        self.refresh_data()
        #del self.loadinglabel
        self.refresh_listbox()
        self.refresh_table()  
        
        
        if not self.avaiabletypes:
            self.loadinglabel.config(text="No pictures")

    def into_what(self,event):
        '''
        Event function to change format type to which conversion should be done. Used for convert_to listbox in main panel.
        Also changes convert_from listbox selection when choice would the same - Avoiding conversion to same format.
        '''

        self.tochosenfile = self.convert_to.get(self.convert_to.curselection()) 
        if self.tochosenfile == self.fromchosenfile:

            self.convert_from.selection_clear(0,tk.END) 
            
            if self.avaiabletypes.index(self.tochosenfile) == 0:
                
                self.convert_from.select_set(1)
                self.fromchosenfile = self.avaiabletypes[1]
                
            else:
                
                self.convert_from.select_set(0)
                self.fromchosenfile = self.avaiabletypes[0]

    def look_for_extensions(self):
        '''
        Checking directory for image extensions. If found adding them to list which will be used for listboxes in mainpanel.
        '''

        self.avaiabletypes = []   

        for file in glob.glob(self.imgdir+'/*'):
            if file.lower().endswith(self.tuplefiletype):
                if os.path.isfile(file):
                    ext = os.path.splitext(file)[-1].lower()
                    if ext not in self.avaiabletypes:
                        self.avaiabletypes.append(ext)
                        if len(self.avaiabletypes)==len(self.listfiletype):
                            break
        self.avaiabletypes.sort()

    
    def state_btn_start(self):
        '''
        Block start button if parameters are missing.
        '''
        
        if self.btn_script():
            
            self.start_btn.config(state = "normal", text="Convert")
            self.start_btn.config(image=self.start_pixel_img,compound='left')
        else:
            
            self.start_btn.config(state = "disabled", text="No Images Found")
            self.start_btn.config(image='')
                                 
    def refresh_data(self):
        
        self.look_for_extensions()
        self.create_dict()
        self.storeddate = _si.StoreInfo(self._typedic,self.imgdir)
        self.storeddate.count_imgs() 
   
    def refresh_listbox(self):
        '''
        Refreshes listboxes in mainpanel based on avaiable img types in directory.
        '''

        #For No Img Files - Clear List Boxes
        if len(self.avaiabletypes) == 0:

            self.fromchosenfile = None
            self.tochosenfile = None
            self.convert_to.delete(0,tk.END)
            self.convert_from.delete(0,tk.END)
            
        #For 1 Img Type File - Clear Box/Make 1 option avaiable in Convert_From Listbox/Automatic choice   
        elif len(self.avaiabletypes) == 1:

            #Set types and delete file type to avoid conversion to same type.
            self.fromchosenfile = self.avaiabletypes[0]
            self.listfiletype.remove(self.fromchosenfile)
            self.tochosenfile = self.listfiletype[0]

            #Refresh lists
            self.convert_to.delete(0,tk.END)
            for x in self.listfiletype:
        	    self.convert_to.insert(tk.END, x)
             
            self.convert_from.delete(0,tk.END)
            for x in self.avaiabletypes:
        	    self.convert_from.insert(tk.END, x)
            
            #Refresh selection 
            self.convert_from.selection_clear(0,tk.END)
            self.convert_from.select_set(0)
            
            self.convert_to.selection_clear(0,tk.END)
            self.convert_to.select_set(0)
            
        #For multiple Img Type File - Clear Box/
        #Make many options avaiable and automaticaly switch options to avoid conversing same types.
        else:
            
            #Refresh lists
            self.convert_from.delete(0,tk.END)
            for x in self.avaiabletypes:
        	    self.convert_from.insert(tk.END, x)
             
            self.convert_to.delete(0,tk.END)
            for x in self.listfiletype:
        	    self.convert_to.insert(tk.END, x)
            
            #Set types for images.
            self.fromchosenfile = self.avaiabletypes[0]
            self.tochosenfile = self.listfiletype[0]
            
            #Avoid same types.
            self.chck_listbox_imgtypes()
        self.state_btn_start()
        
    def refresh_table(self):
        
        HeadList = ["Type","Quantity","Size (MB)", "Avarage (MB)",]

        self.table = _st.SimpleTable(self.f_main_panel,len(self._typedic.keys())+1,len(HeadList),"#9dc8c9")
        self.table.filltable(HeadList,self._typedic)
        self.table.grid(row=1,column=3,rowspan=2,columnspan=4,sticky="news")
    
     




          
  

