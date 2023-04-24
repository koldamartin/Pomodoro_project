from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25/100
SHORT_BREAK_MIN = 5/100
LONG_BREAK_MIN = 20/100
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_button.config(text="")
    global reps
    reps = 0
    label.config(text="Timer")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 7:
        label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 2 == 1:
        label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer
    count_minute = math.floor(count/60)
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count == 0:
        reps += 1
        if reps % 2 == 1:
            check_number = 1+int(reps/2)
            check_button.config(text = "✓"*check_number, fg=GREEN, font=(FONT_NAME,20,"bold"))
        start_timer()
    elif count > 0:
        timer =window.after(1000, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# add the tomato.png as a background using Canvas class
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text =canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Labels
label = Label(text="Timer",fg=GREEN, bg=YELLOW,font=(FONT_NAME,30,"bold"))
label.grid(column=1, row=0)

# Start Button
button = Button(text="Start",command=start_timer)
button.grid(column=0,row=2)
# Reset Button
button = Button(text="Reset", command=reset_timer)
button.grid(column=2,row=2)

# Checkbuttons
check_button = Label(bg=YELLOW, fg=GREEN,font=(FONT_NAME,20,"bold"))
check_button.grid(column=1,row=3)

window.mainloop()