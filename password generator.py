import tkinter as tk    # tkinter is used to create GUI elements.
import random

def generate_password():    # Starts the function to generate the password when the user clicks "Generate"
    pw_entry.delete(0, tk.END)  #  Clears the password entry box before adding a new one.
    error_label.config(text="")  # Clears any previous error or success messages.

    try:                        # Gets the length entered by the user and checks if it's a valid number.
        length = int(length_entry.get())
        if length <= 0:
            error_label.config(text=" Enter a number greater than 0")
            return
    except:
        error_label.config(text=" Please enter a valid number")
        return

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    specials = '!@#$%^&*()_+-=[]{}|;:,.<>?/~`'

    char_pool = ''   # Empty string that will store the combined set of characters based on what the user selects.
    if use_letters.get():  # Adds character sets to the pool only if the corresponding checkboxes are selected.
        char_pool += letters
    if use_numbers.get():
        char_pool += numbers
    if use_specials.get():
        char_pool += specials

    if not char_pool:
        error_label.config(text=" Select at least one character set") # hows an error if no checkboxes are selected.
        return

    password = ''.join(random.choice(char_pool) for _ in range(length)) # Generates the password by randomly picking characters from the selected pool.
    pw_entry.insert(0, password)
    error_label.config(text=" Password generated")

def copy_to_clipboard():  # Defines the function to copy password to clipboard.
    password = pw_entry.get()  # Gets the current password from the entry box.
    if password:               # If password exists: copies to clipboard and shows message.
        window.clipboard_clear()
        window.clipboard_append(password)
        error_label.config(text=" Password copied!")
    else:                                         # Else: shows a warning that no password is available.
        error_label.config(text=" No password to copy!")


window = tk.Tk()  # Initializes the main window.
window.title("Raw Password Generator")   # Sets window title, size, prevents resizing, and gives light green background.
window.geometry("500x400")
window.resizable(False, False)
window.config(bg="orange")


length_frame = tk.LabelFrame(window,     # A frame with title to enter password length.
                             text=" Password Length", font=("Arial", 12, "bold"), bg="yellow")
length_frame.pack(pady=10)

length_entry = tk.Entry(length_frame, 
                        font=("Helvetica", 20), width=10, justify='center')
length_entry.pack(pady=10, padx=10)

options_frame = tk.Frame(window, bg="yellow") # Frame for checkboxes to choose character sets.
options_frame.pack(pady=10)

use_letters = tk.BooleanVar(value=True)
use_numbers = tk.BooleanVar(value=True)
use_specials = tk.BooleanVar(value=True)

tk.Checkbutton(options_frame, text="Letters",  
               variable=use_letters, bg="yellow",
               font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w", padx=10)

tk.Checkbutton(options_frame, text="Numbers",
               variable=use_numbers, bg="yellow",
               font=("Helvetica", 10, "bold")).grid(row=1, column=0, sticky="w", padx=10)

tk.Checkbutton(options_frame, text="Special Chars",
               variable=use_specials, bg="yellow",
               font=("Helvetica", 10, "bold")).grid(row=2, column=0, sticky="w", padx=10)


pw_entry = tk.Entry(window,        # Entry box that displays the generated password.
                    font=("Courier", 20), bd=2, justify='center')
pw_entry.pack(pady=20, ipadx=5, ipady=5, fill="x", padx=20)


btn_frame = tk.Frame(window, bg="orange")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text=" Generate", bg = "#00FF00",
          font=("Arial", 12), command=generate_password).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text=" Copy", 
          font=("Helvetica",12),bg = "#73A16C", command=copy_to_clipboard).grid(row=0, column=1, padx=10)


error_label = tk.Label(window, text="", fg="red", font=("Arial", 10, "bold"), bg="orange")
error_label.pack()

window.mainloop()  # Runs the GUI loop – keeps the window open and interactive.
