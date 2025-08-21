from tkinter import *
import time
from tkinter import messagebox

# ---------------- GUI Setup ----------------
app = Tk()
app.title("🕒 Digital Clock with Alarm")
app.geometry("400x200")
app.resizable(False, False)
app.configure(bg="black")

# ---------------- Clock Labels ----------------
clock_label = Label(app, bg="black", fg="cyan", font=("Helvetica", 40, "bold"))
clock_label.place(x=50, y=20)

date_label = Label(app, bg="black", fg="white", font=("Helvetica", 15))
date_label.place(x=80, y=90)

# ---------------- Alarm Entry ----------------
Label(app, text="Set Alarm (HH:MM:SS AM/PM):", bg="black", fg="yellow", font=("Helvetica", 10)).place(x=20, y=140)
alarm_entry = Entry(app, font=("Helvetica", 12), width=15, justify="center")
alarm_entry.place(x=220, y=140)

# ---------------- Functions ----------------
alarm_time = None

def set_alarm():
    global alarm_time
    alarm_time = alarm_entry.get().strip()
    messagebox.showinfo("Alarm Set", f"⏰ Alarm set for {alarm_time}")

def update_time():
    global alarm_time
    current_time = time.strftime("%I:%M:%S %p")  # 12-hr format with AM/PM
    current_date = time.strftime("%A, %d %B %Y")

    # Dynamic color based on time
    hour = int(time.strftime("%H"))
    if 6 <= hour < 12:
        fg_color = "orange"   # Morning
    elif 12 <= hour < 18:
        fg_color = "green"    # Afternoon
    else:
        fg_color = "cyan"     # Evening/Night

    # Update labels
    clock_label.config(text=current_time, fg=fg_color)
    date_label.config(text=current_date)

    # Check alarm
    if alarm_time == current_time:
        messagebox.showinfo("Alarm 🔔", "Wake up! Time’s up ⏰")
        alarm_time = None   # Reset after ringing

    clock_label.after(1000, update_time)

# ---------------- Buttons ----------------
Button(app, text="Set Alarm", command=set_alarm, bg="yellow", fg="black", font=("Helvetica", 10, "bold")).place(x=160, y=170)

# ---------------- Start ----------------
update_time()
app.mainloop()
