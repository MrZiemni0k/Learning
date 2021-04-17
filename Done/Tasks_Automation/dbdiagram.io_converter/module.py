import tkinter as tk
import sql_db_convert as sql_db
import pyperclip
COLOR = sql_db.COLOR


class ListGenerator(tk.Frame):
    
    def __init__(self, parent=None, **kwargs):
        
        tk.Frame.__init__(self, parent, **kwargs)
        self.header_color = COLOR[0]
        self.clearbtn1 = tk.Button(self, bg='#7E4D5D', text='Clear',
                                   command=self.clear_inputtext)
        self.clearbtn1.grid(row=6, column=0, sticky='news')
        self.copybtn1 = tk.Button(self, bg='white', text='Copy',
                                  command=self.copy_inputtext)
        self.copybtn1.grid(row=6, column=1, sticky='news')
        self.clearbtn2 = tk.Button(self, bg='#7E4D5D', text='Clear',
                                   command=self.clear_outputtext)
        self.clearbtn2.grid(row=6, column=2, sticky='news')
        self.copybtn2 = tk.Button(self, bg='white', text='Copy',
                                  command=self.copy_outputtext)
        self.copybtn2.grid(row=6, column=3, sticky='news')
        
        self.input_box = tk.Text(self, fg='#cfd1c2', bg='#313134',
                                 height=50, width=75, bd=5, relief='groove')
        self.input_box.grid(row=0, column=0, sticky='news',
                            rowspan=6, columnspan=2)
        self.output_box = tk.Text(self, fg='#cfd1c2', bg='#313134',
                                  height=50, width=75, bd=5, relief='groove')
        self.output_box.grid(row=0, column=2, sticky='news',
                             rowspan=6, columnspan=2)
        self.button_table = tk.Button(self, bg='#466182', text='\nTable\n',
                                      command=self.convert_todb)
        self.button_table.grid(row=7, column=0, columnspan=4, sticky='news')
        self.color_label = tk.Label(self, bg=self.header_color, bd=10)
        self.color_label.grid(row=6, column=4, rowspan=2,
                              columnspan=int(len(COLOR) / 6), sticky='news')
        self.color_buttons = []
        self.make_color_btns()


    def make_color_btns(self):
        row = 0
        column = 4
        for color in COLOR:
            if row == 6:
                row = 0
                column += 1
            print(color)
            btn = tk.Button(self, text=color, bg=color, highlightthickness=0,
                            command=lambda _c=color: self.set_color(_c),
                            width=20, bd=0)
            btn.grid(row=row, column=column, sticky='news')
            self.color_buttons.append(btn)
            row += 1

    def set_color(self, color_):
        self.header_color = color_
        print(self.header_color)
        self.color_label.config(bg=self.header_color)

    def convert_todb(self):
        
        if not self.input_box.compare("end-1c", "==", "1.0"):
            text = self.input_box.get("1.0", "end-1c")
            if not self.output_box.compare("end-1c", "==", "1.0"):
                self.output_box.delete("1.0", "end-1c")
            output_text = sql_db.make_dbtable(text, self.header_color)
            self.output_box.insert("1.0", output_text)
            pyperclip.copy(output_text)
            
    def clear_inputtext(self):
        self.input_box.delete("1.0", "end-1c")
    
    def clear_outputtext(self):
        self.output_box.delete("1.0", "end-1c")
        
    def copy_inputtext(self):
        self.clipboard_clear()
        self.clipboard_append(self.input_box.get("1.0", "end-1c"))
    
    def copy_outputtext(self):
        self.clipboard_clear()
        self.clipboard_append(self.output_box.get("1.0", "end-1c"))
