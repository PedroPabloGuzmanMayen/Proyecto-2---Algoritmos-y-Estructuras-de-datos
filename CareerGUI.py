import tkinter as tk
from Data_Manager import Data_Manager
class CareerGUI:
    def __init__(self, career_name, menu, user):
        self.menu = menu
        self.user = user
        self.window = tk.Toplevel()
        self.window.title("MyCareer Menu")
        self.window.geometry("300x400")
        self.window.configure(bg="#F4F4F4")
        self.career = career_name
        self.data = Data_Manager()

        # Create the label with the career name
        career_label = tk.Label(self.window, text=career_name, font=("Arial", 16), bg="#F4F4F4")
        career_label.pack(pady=20)

        # Create the textbox
        textbox = tk.Entry(self.window, font=("Arial", 12))
        textbox.pack()

        # Create the "Valorar" button
        valorar_button = tk.Button(self.window, text="Valorar", font=("Arial", 12), bg="#4CAF50", fg="white",
                                   command=self.valorar_action(textbox.get(), self.user, self.career))
        valorar_button.pack(pady=10)

        # Create the "Atrás" button
        back_button = tk.Button(self.window, text="Atrás", font=("Arial", 12), bg="#FF5722", fg="white",
                                command=self.back_action)
        back_button.pack(side=tk.LEFT, padx=5)

        self.window.protocol("WM_DELETE_WINDOW", self.back_action)

    def valorar_action(self, rating, user, name):
    
        self.data.setRating(user.username, name, int(rating))
        self.user.

        self.menu.update_user(self.user)
        self.menu.update_buttons([1,2,34], self.user.username)
    

    def back_action(self):
        # Action for "Atrás" button
        self.window.withdraw()
        self.menu.window.deiconify()
