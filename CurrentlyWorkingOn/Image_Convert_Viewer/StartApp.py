import SimplePage as _sp
import AdvancedPage as _ap
import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = _sp.SimplePage(self)
        self.frame.pack

    def change(self,frame):
        self.frame.pack_forget()
        self.frame = frame(self)
        self.frame.pack()

if __name__ == "__main__": 
    app = Application()
    app.mainloop()