import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=120, height=60)

def calculate(miles):
    km_num_label['text'] = str(round(int(miles) * 1.609344, 3))
#Layout

miles_input = tk.Entry()
miles_input.grid(row=0, column=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = tk.Label(text='is equal to')
is_equal_label.grid(row=1, column=0)

km_num_label = tk.Label(text='0')
km_num_label.grid(row=1, column=1)

km_label = tk.Label(text='Km')
km_label.grid(row=1, column=2)

calculate_button = tk.Button(text='Calculate', command=lambda: calculate(miles_input.get()))
calculate_button.grid(row=2, column=1)

window.mainloop()