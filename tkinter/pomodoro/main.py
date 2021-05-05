from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
BLUE = "#00005c"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    print("reps in reset start",reps)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    #reps = 0
    print("reps at the end of reset", reps)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():

    global reps
    print("reps in start timer", reps)
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="LONG BREAK", fg=RED, bg=GREEN, font=(FONT_NAME, 35))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK", fg=PINK, bg=GREEN, font=(FONT_NAME, 35))
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=BLUE)


    print("reps at end of timer", reps)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    print("reps at start of count_down", reps)
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        working_sessions = math.floor(reps/2)
        for _ in range(working_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)

    print("reps at end of count_down", reps)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=150, pady=120, bg=GREEN)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 128, text="00:00", fill="black", font=(FONT_NAME, 27, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=BLUE, bg=GREEN, font=(FONT_NAME, 35))
timer_label.grid(column=1, row=0)
timer_label.config(padx=50)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

checkmark_label = Label(fg=BLUE, bg=GREEN)
checkmark_label.grid(column=1, row=3)
checkmark_label.config(padx=50)












window.mainloop()
