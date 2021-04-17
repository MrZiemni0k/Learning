import tkinter as tk
from seperator import MakeLine


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = MakeLine()
        self.frame.pack()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
