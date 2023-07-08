import tkinter as tk
from PIL import ImageTk, Image
import wordle_solver as ws

class WordleSolverUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Wordle Solver")
        self.root.geometry("400x570")
        self.root.config(bg="#121213")

        self.solver = ws.wordle_solver()
        self.create_title_image()
        self.create_squares()
        self.root.mainloop()

    def create_title_image(self):
        title_padding_frame = tk.Frame(self.root, padx=10, pady=15, bg="#121213")
        title_padding_frame.pack()
        self.title_padding_frame = title_padding_frame

        title_image = Image.open("Title.png")
        title_image = title_image.resize((int(title_image.width * 0.07), int(title_image.height * 0.07)))
        title_image = ImageTk.PhotoImage(title_image)
        title_label = tk.Label(self.title_padding_frame, image=title_image, bg="#121213")
        
        
        title_label.image = title_image
        title_label.pack()
        
    def create_squares(self):
        padding_frame = tk.Frame(self.root, padx=10, pady=20, bg="#121213")
        padding_frame.pack()
        self.padding_frame = padding_frame

        vcmd = (self.root.register(self.validate))
        box_style = {
            'width': 2,
            'font': ('Helvetica Neue', 50, 'bold'),
            'justify': 'center',
            'bg': '#121213',
            'highlightcolor': '#3a3a3c',
            'highlightbackground': '#3a3a3c',
            'highlightthickness': 2,
            'relief': 'flat',
            'cursor': 'arrow',
            'insertbackground': '#121213',
            'validate': 'key',
            'validatecommand': vcmd
        }
        self.squares = []
        for row in range(6):
            for col in range(5):
                square = tk.Entry(self.padding_frame, **box_style)
                square.grid(row=row, column=col, padx=1.5, pady=1.5)
                square.bind("<Shift-Button-1>", self.change_color)
                square.bind("<Return>", self.enter_word)
                self.squares.append(square)
        self.current_line = self.squares[0:5]
        self.current_line_index = 0
    
    def validate(self):
        return False
    
    def change_color(self, event):
        if event.state == 1:
            current_color = event.widget["bg"]
            if current_color == "#121213":  # Black
                event.widget["bg"] = "#3a3a3c"  # Gray
                event.widget["highlightbackground"] = "#3a3a3c"  # Gray
                event.widget["insertbackground"] = "#3a3a3c"  # Gray
            elif current_color == "#538d4e":  # Green
                event.widget["bg"] = "#3a3a3c"  # Gray
                event.widget["highlightbackground"] = "#3a3a3c"  # Gray
                event.widget["insertbackground"] = "#3a3a3c"  # Gray
            elif current_color == "#b59f3b":  # Yellow
                event.widget["bg"] = "#538d4e"  # Green
                event.widget["highlightbackground"] = "#538d4e"  # Green
                event.widget["insertbackground"] = "#538d4e"  # Green
            elif current_color == "#3a3a3c":  # Gray
                event.widget["bg"] = "#b59f3b"  # Yellow
                event.widget["highlightbackground"] = "#b59f3b"  # Yellow
                event.widget["insertbackground"] = "#b59f3b"  # Yellow

    def enter_word(self, event):
        word = ""
        for square in self.current_line:
            word += square.get()
        print(word)
        self.current_line_index += 1
        self.current_line = self.squares[self.current_line_index * 5: (self.current_line_index + 1) * 5]
        self.current_line[0].focus()
        self.current_line[0].selection_range(0, tk.END)

if __name__ == "__main__":
    WordleSolverUI()
