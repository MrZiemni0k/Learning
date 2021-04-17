import tkinter as tk
import module


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = module.ListGenerator()
        self.frame.pack()


if __name__ == "__main__": 
    app = Application()
    app.mainloop()