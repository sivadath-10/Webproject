import tkinter as tk
import random

def new_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 10
    result_label.config(text="Guess a number between 1 and 100", fg="black")
    attempts_label.config(text=f"Attempts left: {attempts}")
    guess_button.config(state='normal')  
    entry.delete(0, tk.END)  

def check_guess():
    global attempts
    try:
        guessed_number = int(entry.get())
        if guessed_number < 1 or guessed_number > 100:
            result_label.config(text="Please enter a number between 1 and 100.", fg="orange")
            return
        
        attempts -= 1
        if guessed_number == secret_number:
            result_label.config(text="🎉 Congratulations! You guessed it right!", fg="green")
        elif attempts == 0:
            result_label.config(text=f"😢 Out of attempts! The number was {secret_number}.", fg="red")
        elif guessed_number < secret_number:
            result_label.config(text="Too low! Try again.", fg="blue")
            attempts_label.config(text=f"Attempts left: {attempts}")
        else:
            result_label.config(text="Too high! Try again.", fg="blue")
            attempts_label.config(text=f"Attempts left: {attempts}")
        
        if attempts == 0 or guessed_number == secret_number:
            guess_button.config(state='disabled')

    except ValueError:
        result_label.config(text="Please enter a valid integer.", fg="red")

def quit_game():
    root.destroy()


root = tk.Tk()
root.title("Number Guessing Game")
root.configure(bg="#282c34")  
root.geometry("600x400")  


title_label = tk.Label(root, text="Number Guessing Game", bg="#61dafb", font=("Helvetica", 24, "bold"), pady=10)
title_label.pack(pady=10)


entry_frame = tk.Frame(root, bg="#282c34")
entry_frame.pack(pady=10)
entry_label = tk.Label(entry_frame, text="Enter your guess:", bg="#282c34", fg="#ffffff", font=("Helvetica", 16))
entry_label.pack(side=tk.LEFT, padx=5)
entry = tk.Entry(entry_frame, font=("Helvetica", 16), width=10)
entry.pack(side=tk.LEFT)


result_label = tk.Label(root, text="", bg="#282c34", fg="#ffffff", font=("Helvetica", 18))
result_label.pack(pady=10)


attempts_label = tk.Label(root, text="", bg="#282c34", fg="#ff6f61", font=("Helvetica", 16))
attempts_label.pack(pady=5)

button_frame = tk.Frame(root, bg="#282c34")
button_frame.pack(pady=20)

guess_button = tk.Button(button_frame, text="Guess", width=10, height=2, command=check_guess, font=("Helvetica", 14), bg="#98fb98")
guess_button.grid(row=0, column=0, padx=10)

new_game_button = tk.Button(button_frame, text="New Game", width=10, height=2, command=new_game, font=("Helvetica", 14), bg="#61dafb")
new_game_button.grid(row=0, column=1, padx=10)

quit_game_button = tk.Button(button_frame, text="Quit", width=10, height=2, command=quit_game, font=("Helvetica", 14), bg="#ff6f61")
quit_game_button.grid(row=0, column=2, padx=10)


new_game()

root.mainloop()