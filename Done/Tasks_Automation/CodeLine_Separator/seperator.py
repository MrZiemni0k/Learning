import tkinter as tk


class MakeLine(tk.Frame):

    def __init__(self, parent=None, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        self.copy_button = tk.Button(self, bg='white', text='Copy',
                                     command=self.copy_output)
        self.input_box = tk.Entry(self, fg='#cfd1c2', bg='#515249', width=80)
        self.button_to = tk.Button(self, bg='#31592a', text='Convert',
                                   command=self.convert_text)
        self.output_box = tk.Entry(self, fg='#cfd1c2', bg='#515249', width=80)
        self.interface_layout()

    def interface_layout(self):
        self.copy_button.grid(row=1, column=1, sticky='ew')
        self.input_box.grid(row=0, column=0, sticky='ew')
        self.button_to.grid(row=0, column=1, sticky='ew')
        self.output_box.grid(row=1, column=0, sticky='ew')

    def convert_text(self):
        self.output_box.delete(0, tk.END)
        text = f' 💡💻 {self.input_box.get()} 💻💡 '.upper()
        output_text = '# ' + text.center(74, '-')
        print(output_text)
        self.output_box.insert(0, output_text)

    def copy_output(self):
        self.clipboard_clear()
        self.clipboard_append(self.output_box.get())
