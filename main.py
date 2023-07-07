import tkinter as tk
from tkinter import font
from tkinter import ttk

def change_color(event):
    if event.state == 1:  # Shift key is pressed
        current_color = event.widget["bg"]
        if current_color == "#121213": # Black
            event.widget["bg"] = "#3a3a3c" # Gray
            event.widget["highlightbackground"] = "#3a3a3c" # Gray
        elif current_color == "#538d4e": # Green
            event.widget["bg"] = "#3a3a3c" # Gray
            event.widget["highlightbackground"] = "#3a3a3c" # Gray
        elif current_color == "#b59f3b": # Yellow
            event.widget["bg"] = "#538d4e" # Green
            event.widget["highlightbackground"] = "#538d4e" # Green
        elif current_color == "#3a3a3c": # Gray
            event.widget["bg"] = "#b59f3b" # yellow
            event.widget["highlightbackground"] = "#b59f3b" # yellow

root = tk.Tk()
root.title("Wordle Solver")
root.geometry("400x475")
root.config(bg="#121213")

# Load the custom font "nyt-karnakcondensed"
font_path = 'font/condensedblack.ttf'
custom_font = font.Font(family='nyt-karnakcondensed', size=20)
root.option_add('*Font', custom_font)

# Define the CSS properties for the title label
title_style = {
    'font': ('KarnakPro-CondensedBlack', 28),
    'bg': '#121213',
    'pady': 10,  # vertical padding
}

title_label = tk.Label(root, text="Wordle Solver", **title_style)
title_label.pack()


# Create padding around the squares
padding_frame = tk.Frame(root, padx=10, pady=20, bg="#121213")
padding_frame.pack()

squares = []
for row in range(6):
    for col in range(5):
        square = tk.Entry(padding_frame, width=2, font=("Helvetica Neue", 50, "bold"), justify='center', bg="#121213", highlightbackground="#3a3a3c", highlightthickness=2 , relief="flat")
        square.grid(row=row, column=col, padx=1.5, pady=1.5)
        square.bind("<Shift-Button-1>", change_color)
        squares.append(square)

root.mainloop()
