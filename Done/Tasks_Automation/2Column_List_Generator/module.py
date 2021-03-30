import tkinter as tk
import converter

class ListGenerator(tk.Frame):
    
    def __init__(self,parent=None, **kwargs):
        
        tk.Frame.__init__(self,parent, **kwargs)
        self._converter = converter.MakeList()
        self.interface()
        self.convert_text()
        
    def interface(self):
        
        self.input_box = tk.Text(self,fg='#cfd1c2',bg='#515249',height=20,width=60)
        self.input_box.grid(row=0,column=0,sticky='news')
        self.button_to = tk.Button(self,bg='#31592a',text='Convert',command=lambda:self.convert_text())
        self.button_to.grid(row=0,column=1,sticky='news')
        self.output_box = tk.Text(self,fg='#cfd1c2',bg='#515249',height=20,width=60)
        self.output_box.grid(row=1,column=0,sticky='news')
        self.button_back = tk.Button(self,bg='#692e21',text='Unconvert',command=lambda:self.unconvert_text())
        self.button_back.grid(row=1,column=1,sticky='news')
    
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
