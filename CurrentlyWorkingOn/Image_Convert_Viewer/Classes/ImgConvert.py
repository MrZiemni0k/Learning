#TODO: Squeeze code into os.path.split instead of str+str+str to avoid duplicates .jpg.svg 
import tkinter as tk
import glob
import os, os.path
from PIL import Image

class ImgConvert():
    '''
    Class with a script for converting image type files.
    ........

    Methods
    ----------
    convert()
        Converting all images in a directory based on parameters passed in class creation.
    does_exist()
        Chck if file path exists to avoid overwriting file issues.
    '''
    
    def __init__(self,from_format,to_format,_directory,to_delete):
        '''
        Parameters:
        ------------
        from_format(str):
            From which format to convert('.'+str)
        to_format(str):
            To which format to convert ('.'+str)
        _directory(str):
            Directory with images to work on.
        to_delete(bool):
            Delete old image file after conversion.
        '''
        self.from_format = from_format
        self.to_format = to_format
        self._directory = _directory
        self.to_delete = to_delete
        self.img_count = 0
        
    def convert_all(self):
        '''
        Script to convert all images based on parameters passed in class creation. 
        Based on to_delete parameter - Deletes or not used files.
        '''
        for file in glob.glob(self._directory+'/*'+self.from_format):
            try:
                img = Image.open(file)
                
                self.img_count += 1
                self.nofrmt_file = str(file).rstrip(self.from_format)
                self.to_file = self.nofrmt_file+self.to_format
                self.does_exist()   
                img.save(self.to_file)
                
                if self.to_delete:
                
                    try:
                        os.remove(self.nofrmt_file+self.from_format)
                    except OSError as e:
                        tk.messagebox.showinfo(title='OSError', message=f"{e}") 
                    except IOError as e:
                        tk.messagebox.showinfo(title='IOError', message=f"{e}")
                
            except OSError as e:
                tk.messagebox.showinfo(title='Error', message=f"{e}\nConversion aborted.")
                break 
                


            
                    
    def convert_one(self):
        '''
        Script to convert one image based on parameters passed in class creation. 
        Based on to_delete parameter - Deletes or not used files.
        '''
        try:
            img = Image.open(self._directory)
            
            self.img_count += 1        
            self.nofrmt_file = str(self._directory).rstrip(self.from_format)
            self.to_file = self.nofrmt_file+self.to_format
            
            self.does_exist()   
             
            img.save(self.to_file)

            if self.to_delete:
                
                try:
                    os.remove(self.nofrmt_file+self.from_format)
                except OSError as e:
                    tk.messagebox.showinfo(title='OSError', message=f"{e}") 
                except IOError as e:
                    tk.messagebox.showinfo(title='IOError', message=f"{e}")
                except OSError as e:
                    tk.messagebox.showinfo(title='Error', message=f"{e}\nConversion aborted.") 
        
        except OSError as e:
            tk.messagebox.showinfo(title='Error', message=f"{e}\nConversion aborted.")
                 
    def does_exist(self):
        '''
        Function for avoiding overwriting by checking if file exists.
        It will index file with _000 format.
        '''
        counter = 0 
        while os.path.exists(self.to_file):
            if len(str(counter)) == 1:
                self.to_file = self.nofrmt_file+'_00'+str(counter)+self.to_format
            elif len(str(counter)) ==2:
                self.to_file = self.nofrmt_file+'_0'+str(counter)+self.to_format
            else:
                self.to_file = self.nofrmt_file+'_'+str(counter)+self.to_format
            counter += 1