import tkinter as tk
import converter

class ListGenerator(tk.Frame):
    
    def __init__(self,parent=None, **kwargs):
        
        tk.Frame.__init__(self,parent, **kwargs)
        self._converter = converter.MakeList()
        self.interface()
        self.convert_text()
        
    def interface(self):
        
        self.clearbtn1 = tk.Button(self,bg='white',text='Clear',command=lambda:self.clear_inputtext())
        self.clearbtn1.grid(row=0,column=0,sticky='news')
        self.copybtn1 = tk.Button(self,bg='white',text='Copy',command=lambda:self.copy_inputtext())
        self.copybtn1.grid(row=1,column=0,sticky='news')
        self.clearbtn2 = tk.Button(self,bg='white',text='Clear',command=lambda:self.clear_outputtext())
        self.clearbtn2.grid(row=2,column=0,sticky='news')
        self.copybtn2 = tk.Button(self,bg='white',text='Copy',command=lambda:self.copy_outputtext())
        self.copybtn2.grid(row=3,column=0,sticky='news')
        
        self.input_box = tk.Text(self,fg='#cfd1c2',bg='#515249',height=22,width=100)
        self.input_box.grid(row=0,column=1,sticky='news',rowspan=2)
        self.button_to = tk.Button(self,bg='#31592a',text='Convert',command=lambda:self.convert_text())
        self.button_to.grid(row=0,column=2,sticky='news',rowspan=2)
        self.output_box = tk.Text(self,fg='#cfd1c2',bg='#515249',height=22,width=100)
        self.output_box.grid(row=2,column=1,sticky='news',rowspan=2)
        self.button_back = tk.Button(self,bg='#692e21',text='Unconvert',command=lambda:self.unconvert_text())
        self.button_back.grid(row=2,column=2,sticky='news',rowspan=2)
        self.button_table = tk.Button(self,bg='#466182',text='Table',command=lambda:self.convert_todb())
        self.button_table.grid(row=0,column=3,rowspan=4,sticky='news')
    
    def convert_text(self):
        
        if not self.input_box.compare("end-1c", "==", "1.0"):
            if not self.output_box.compare("end-1c", "==", "1.0"):
                self.output_box.delete("1.0","end-1c")
            text = self.input_box.get("1.0","end-1c")
            output_text = self._converter.make_list1(text)
            self.output_box.insert("1.0",output_text)
            
    def unconvert_text(self):
        
        if not self.output_box.compare("end-1c", "==", "1.0"):
            if not self.input_box.compare("end-1c", "==", "1.0"):
                self.input_box.delete("1.0","end-1c")
            text = self.output_box.get("1.0","end-1c")
            output_text = self._converter.unmake_list1(text)
            self.input_box.insert("1.0",output_text)
            
    def convert_todb(self):
        
        if not self.input_box.compare("end-1c", "==", "1.0"):
            text = self.input_box.get("1.0","end-1c")    
            if not self.output_box.compare("end-1c", "==", "1.0"):
                self.output_box.delete("1.0","end-1c")
            output_text = self._converter.make_table_list(text)
            self.output_box.insert("1.0",output_text)
            
    def clear_inputtext(self):
        self.input_box.delete("1.0","end-1c")
    
    def clear_outputtext(self):
        self.output_box.delete("1.0","end-1c")
        
    def copy_inputtext(self):
        self.clipboard_clear()
        self.clipboard_append(self.input_box.get("1.0","end-1c"))
    
    def copy_outputtext(self):
        self.clipboard_clear()
        self.clipboard_append(self.output_box.get("1.0","end-1c"))