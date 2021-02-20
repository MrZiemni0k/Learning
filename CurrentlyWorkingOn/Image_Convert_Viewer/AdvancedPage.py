import tkinter as tk
import SimplePage as _sp

class AdvancedPage(tk.Frame):
    def __init__(self,parent=None, **kwargs):
        tk.Frame.__init__(self,parent, **kwargs)

        parent.title("Advanced Page")
        parent.geometry("800x600")

        self.left_panel()
        self.top_panel()
        self.sub_panel()
        self.main_window_panel()
        self.status_panel()
        self.grid_layout()
        self.pack(fill="both",expand=True)

    def left_panel(self):
        self.f_left_panel = tk.Frame(self,bg="#557174")
        self.button0 = tk.Button(self.f_left_panel)
        self.button0.pack()

    def top_panel(self):
        self.f_top_panel = tk.Frame(self,bg="#aaaaaa")
        self.simple_adv_btn = tk.Button(self.f_top_panel,command=self.cos,text="SP/AP")
        self.simple_adv_btn.grid(row=1,column=1,rowspan=1, columnspan=1,sticky="news")
        self.button2 = tk.Button(self.f_top_panel)
        self.button2.grid(row=1,column=5,sticky="news")
        self.button3 = tk.Button(self.f_top_panel)
        self.button3.grid(row=1,column=9,sticky="news")
        self.button4 = tk.Button(self.f_top_panel)
        self.button4.grid(row=1,column=13,sticky="news")
        self.button5 = tk.Button(self.f_top_panel)
        self.button5.grid(row=1,column=17,sticky="news")

        self.f_top_panel.rowconfigure((0,1,2), weight=1)
        self.f_top_panel.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20), weight=1)

    def sub_panel(self):
        self.f_sub_panel = tk.Frame(self,bg="#a4ebf3")

    def main_window_panel(self):
        self.f_main_panel = tk.Frame(self,bg="#f4f9f9",relief="sunken", bd=1)

    def status_panel(self):
        self.f_status_panel = tk.Frame(self, bg="#ccf2f4")

    def grid_layout(self):
        self.f_top_panel.grid(row=0, column=0, rowspan=1, columnspan=10, sticky="news")
        self.f_sub_panel.grid(row=1, column=3, rowspan=1, columnspan=7, sticky="news")
        self.f_left_panel.grid(row=1, column=0, rowspan=8, columnspan=3, sticky="news")
        self.f_main_panel.grid(row=2, column=3, rowspan=7, columnspan=9, sticky="news")
        self.f_status_panel.grid(row=9, column=0, rowspan=1, columnspan=10, sticky="news")

        self.rowconfigure((0,1,2), weight=2)
        self.columnconfigure((0,1,2), weight=2)

        for r in range(3,9):
            self.rowconfigure(r, weight=5)
        for c in range(3,10):
            self.columnconfigure(c, weight=4)

        self.rowconfigure(9, weight=2)

    def cos(self):
        self.f_top_panel.grid_forget()
        self.f_sub_panel.grid_forget()
        self.f_left_panel.grid_forget()
        self.f_main_panel.grid_forget()
        self.f_status_panel.grid_forget()

        self.master.change(_sp.SimplePage)      