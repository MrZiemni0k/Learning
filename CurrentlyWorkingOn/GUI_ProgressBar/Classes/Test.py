import tkinter as tk
import Geometry 

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.canvas = tk.Canvas(self,width=500,height=500,bg='blue')
        self.canvas.pack()

        cuboid = Geometry.Cuboid(self.canvas,(200,100),100,300,400)
        cuboid.draw_cuboid_2persp((50,200),(450,200))
        cuboid.not_visible_lines(200,state='hidden')

if __name__ == "__main__": 
    app = Application()
    app.mainloop()