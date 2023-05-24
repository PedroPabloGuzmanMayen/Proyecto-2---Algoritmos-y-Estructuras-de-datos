import tkinter as tk

class Menu:
    def __init__(self, user, Recomendations):
        self.window = tk.Tk()
        self.window.title("Menu")
        self.window.geometry("300x200")
        self.window.configure(bg="#F4F4F4")

        self.user = user
        self.recomendations = Recomendations

        self.create_buttons()
        self.window.mainloop()
    def create_buttons(self):
        self.buttons = []
        for i, element in enumerate(self.recomendations):
            button = tk.Button(self.window, text=str(element), command=lambda i=i: self.open_window(i))
            button.pack()
            self.buttons.append(button)