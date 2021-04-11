import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps 
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label["text"] = ""
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
    global reps
    reps += 1
    if reps % 2 == 1:
        timer_countdown(WORK_MIN * 60)
        timer_label.config(text='Work', fg=GREEN)
    elif reps % 8 == 0:
        timer_countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text='Break', fg=RED)
    else:
        timer_countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text='Break', fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timer_countdown(count):
    global timer
    amount_min = math.floor(count / 60)
    if amount_min < 10:
        amount_min = f'0{amount_min}'        
    
    amount_sec = count % 60
    if amount_sec < 10:
        amount_sec = f'0{amount_sec}'

    canvas.itemconfig(timer_text, text=f"{amount_min}:{amount_sec}")
    if count > 0:
        timer = window.after(1000, timer_countdown, count - 1)
    else:
        timer_start()
        check_count = ""
        for _ in range(math.floor(reps/2)):
            check_count += '✔'
        checkmark_label['text'] = check_count

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tk.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1, sticky='s')

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_btn = tk.Button(text="Start", command=timer_start, highlightthickness=0)
start_btn.grid(row=2, column=0, sticky='e')

reset_btn = tk.Button(text="Reset", command=timer_reset, highlightthickness=0)
reset_btn.grid(row=2, column=2, sticky='w')

checkmark_label = tk.Label(text="", fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=3, column=1)


window.mainloop()