import tkinter as tk
from tkinter import messagebox

# ---------------- Setup ----------------
app = tk.Tk()
app.title("🎯 Multiplayer Number Guessing Game")
app.geometry("400x300")
app.resizable(False, False)
app.configure(bg="black")

# Global variables
secret_number = None
attempts = 0
max_attempts = 7

# ---------------- Functions ----------------
def set_number():
    """
    Player 1 sets the secret number
    """
    global secret_number, attempts
    try:
        secret_number = int(entry_p1.get())
        if not (1 <= secret_number <= 100):
            raise ValueError
        attempts = 0
        entry_p1.delete(0, tk.END)
        entry_p1.config(state="disabled")
        set_btn.config(state="disabled")
        messagebox.showinfo("✅ Number Set", "Player 1 has set the number!\nPlayer 2, start guessing.")
    except ValueError:
        messagebox.showerror("❌ Error", "Enter a valid number (1-100).")

def guess_number():
    """
    Player 2 guesses the number
    """
    global attempts, secret_number
    if secret_number is None:
        messagebox.showwarning("⚠️ Warning", "Player 1 must set a number first!")
        return
    
    try:
        guess = int(entry_p2.get())
        entry_p2.delete(0, tk.END)
        attempts += 1

        if guess == secret_number:
            messagebox.showinfo("🎉 Correct!", f"Player 2 guessed it in {attempts} attempts!")
            reset_game()
        elif guess < secret_number:
            result.set(f"📉 Too low! Attempts left: {max_attempts - attempts}")
        else:
            result.set(f"📈 Too high! Attempts left: {max_attempts - attempts}")

        if attempts >= max_attempts and guess != secret_number:
            messagebox.showinfo("😢 Game Over", f"Out of attempts! The number was {secret_number}.")
            reset_game()

    except ValueError:
        messagebox.showerror("❌ Error", "Enter a valid number.")

def reset_game():
    """
    Reset the game for a new round
    """
    global secret_number, attempts
    secret_number = None
    attempts = 0
    entry_p1.config(state="normal")
    set_btn.config(state="normal")
    entry_p2.delete(0, tk.END)
    result.set("")

# ---------------- Widgets ----------------
title_label = tk.Label(app, text="🎯 Multiplayer Number Guessing", font=("Helvetica", 14, "bold"), bg="black", fg="cyan")
title_label.pack(pady=10)

# Player 1
p1_label = tk.Label(app, text="Player 1: Set a number (1-100)", bg="black", fg="yellow", font=("Helvetica", 10))
p1_label.pack()
entry_p1 = tk.Entry(app, font=("Helvetica", 12), show="*")  # Hidden input
entry_p1.pack(pady=5)
set_btn = tk.Button(app, text="Set Number", command=set_number, bg="yellow", fg="black", font=("Helvetica", 10, "bold"))
set_btn.pack(pady=5)

# Player 2
p2_label = tk.Label(app, text="Player 2: Guess the number", bg="black", fg="lightgreen", font=("Helvetica", 10))
p2_label.pack(pady=10)
entry_p2 = tk.Entry(app, font=("Helvetica", 12))
entry_p2.pack(pady=5)
guess_btn = tk.Button(app, text="Guess", command=guess_number, bg="lightgreen", fg="black", font=("Helvetica", 10, "bold"))
guess_btn.pack(pady=5)

# Result
result = tk.StringVar()
result_label = tk.Label(app, textvariable=result, font=("Helvetica", 12), bg="black", fg="white")
result_label.pack(pady=10)

# Reset Button
reset_btn = tk.Button(app, text="Reset Game", command=reset_game, bg="red", fg="white", font=("Helvetica", 10, "bold"))
reset_btn.pack(pady=5)

# ---------------- Run ----------------
app.mainloop()
