import tkinter as tk
from CareerGUI import CareerGUI

class Menu:
    def __init__(self, user, recommendations):
        self.window = tk.Tk()
        self.window.title("MyCareer Menu")
        self.window.geometry("300x400")
        self.window.configure(bg="#F4F4F4")

        self.user = user
        self.recommendations = recommendations

        self.buttons = []  # Keep track of generated buttons

        self.create_widgets()

    def create_widgets(self):
        # "MyCareer Menu" label
        title_label = tk.Label(self.window, text="MyCareer Menu", font=("Arial", 16), bg="#F4F4F4")
        title_label.pack(pady=10)

        # First line
        line1 = tk.Frame(self.window, height=2, bd=1, relief=tk.SUNKEN)
        line1.pack(fill=tk.X, padx=5, pady=5)

        # "Tus me gusta" button
        like_button = tk.Button(self.window, text="Tus me gusta", font=("Arial", 12), bg="#4CAF50", fg="white",
                                command=self.like_action)
        like_button.pack(pady=10)

        # "Explorar" button
        explore_button = tk.Button(self.window, text="Explorar", font=("Arial", 12), bg="#2196F3", fg="white",
                                   command=self.explore_action)
        explore_button.pack(pady=10)

        # Second line
        line2 = tk.Frame(self.window, height=2, bd=1, relief=tk.SUNKEN)
        line2.pack(fill=tk.X, padx=5, pady=5)

        # "Para ti" label
        message_label = tk.Label(self.window, text="Para ti", font=("Arial", 16), bg="#F4F4F4")
        message_label.pack(pady=10)

        # Generate buttons from the array
        self.generate_buttons()

    def generate_buttons(self):
        # Generate buttons based on the recommendations array
        for i, element in enumerate(self.recommendations):
            button = tk.Button(self.window, text=str(element), command=lambda i=i: self.button_action(i))
            button.pack(pady=5)
            self.buttons.append(button)  # Add button to the list of buttons

    def update_buttons(self, new_recommendations):
        # Clear existing buttons
        for button in self.buttons:
            button.destroy()

        self.recommendations = new_recommendations
        self.buttons = []  # Clear the list of buttons

        # Generate new buttons
        self.generate_buttons()

    def like_action(self):
        # Action for "Tus me gusta" button
        print("Tus me gusta button clicked")

    def explore_action(self):
        # Action for "Explorar" button
        print("Explorar button clicked")

    def button_action(self, index):
        # Action for each generated button
        self.window.withdraw()
        CareerGUI(self.recommendations[index], self, self.user)

    def update_user(self, new_user):
        # Update the user object
        self.user = new_user

    def run(self):
        self.window.mainloop()
