import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_list = ([random.choice(LETTERS) for _ in range(random.randint(8, 10))] +
                     [random.choice(NUMBERS) for _ in range(random.randint(2, 4))] +
                     [random.choice(SYMBOLS) for _ in range(random.randint(2, 4))]
                    )

    random.shuffle(password_list)

    pass_input.delete(0, tk.END)
    password = "".join(password_list)
    pass_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_inputs():
    return tuple([web_input.get(), email_input.get(), pass_input.get()])

def save_to_file():
    info = get_inputs()
    new_password = {
        info[0]: {
            "email": info[1],
            "password": info[2]
        }
    }

    if "" in info:
        messagebox.showwarning(title='Empty fields', message='Please don\'t leave any fields empty!')

    else:
        is_ok = messagebox.askokcancel(title='Data OK?', 
                                    message=('Please confirm data below: \n'
                                                f'Website:              {info[0]} \n'
                                                f'Email/Username: {info[1]} \n'
                                                f'Password:            {info[2]}')
                                    )
        if is_ok:
            # with open(file='passwords.txt', mode='a') as file:
            #     file.write(f"{info[0]} | {info[1]} | {info[2]} \n")
            try:
                with open(file='passwords.json', mode='r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open(file='passwords.json', mode='w') as file:
                    json.dump(new_password, file, indent=4)
            else:    
                data.update(new_password)
                with open(file='passwords.json', mode='w') as file:
                    json.dump(data, file, indent=4)
            finally:
                web_input.delete(0, tk.END)
                pass_input.delete(0, tk.END)
                messagebox.showinfo(title='Success', message='Password successfully stored')

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_info():
    website = get_inputs()[0]
    try:
        with open(file='passwords.json', mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title='Not Exist', message='Data file not found')
    else:
        if website in data:
            messagebox.showinfo(title=website, message=(f'Email/Username: {data[website]["email"]} \n'
                                                        f'Password:            {data[website]["password"]}'))
        else:
            messagebox.showwarning(title='Not Found', message='Provided website does not exist in database')
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

_canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
lock_picture = tk.PhotoImage(file='logo.png')
_canvas.create_image(100, 100, image=lock_picture)
_canvas.grid(row=0, column=1)

web_label = tk.Label(text='Website:', padx=10)
web_label.grid(row=1, column=0, sticky='e')
web_input = tk.Entry(width=30)
web_input.grid(row=1, column=1, sticky='w')
web_input.focus()
search_btn = tk.Button(text='Search', command=find_info)
search_btn.grid(row=1, column=2, sticky='w')

email_label = tk.Label(text='Email/Username:', padx=10)
email_label.grid(row=2, column=0, sticky='e')
email_input = tk.Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2, sticky='w')
email_input.insert(0, "some_email@protonmail.com")

pass_label = tk.Label(text='Password:', padx=10)
pass_label.grid(row=3, column=0, sticky='e')
pass_input = tk.Entry(width=30)
pass_input.grid(row=3, column=1, sticky='w')
generate_btn = tk.Button(text='Generate Password', command=generate_password)
generate_btn.grid(row=3, column=2, sticky='w')

add_btn = tk.Button(text='Add', command=save_to_file, width=36)
add_btn.grid(row=4, column=1, columnspan=2, sticky='e')

window.mainloop()