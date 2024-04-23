import random
import tkinter as tk
from tkinter import messagebox

# Create a new window
window = tk.Tk()

# Set the dimensions of the created window
window.geometry("359x356")

# Set background image
bg_image = tk.PhotoImage(file="background_image.png")
background_label = tk.Label(window, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



window.resizable(width=False, height=False)

# Set Window Title
window.title('Number Guessing Game')

# Generate a random number between 0 and 999
number_to_guess = random.randint(0, 999)
attempts = 0

def check_guess():
    global attempts
    guess = entry.get()

    try:
        guess = int(guess)
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter a valid integer.")
        return

    if guess < 0 or guess > 999:
        messagebox.showerror("Error", "Invalid input! Please enter a number between 0 and 999.")
        return

    attempts += 1

    if guess == number_to_guess:
        messagebox.showinfo("Congratulations", f"You guessed the number {number_to_guess} correctly.\nIt took you {attempts} attempts.")
        exit_game()
    elif guess < number_to_guess:
        messagebox.showinfo("Hint", "The number is greater than your guess. Try again!")
    else:
        messagebox.showinfo("Hint", "The number is smaller than your guess. Try again!")

    entry.delete(0, tk.END)

def exit_game():
    window.destroy()

# Create label and entry widgets
label = tk.Label(window, text="Guess a number between\n0 and 999", font=("Arial", 15), fg="black")
label.place(x=70, y=70)

entry = tk.Entry(window, font=("Arial", 12))
entry.place(x=90, y=150)

# Create submit button
submit_button = tk.Button(window, text="Submit", font=("Arial", 14), bg="#45DD26", fg="White", command=check_guess)
submit_button.place(x=150, y=200)

# Create exit button
exit_button = tk.Button(window, text="Exit Game", font=("Arial", 14), fg="White", bg="#b82741", command=exit_game)
exit_button.place(x=135, y=250)


# Start the window
window.mainloop()
