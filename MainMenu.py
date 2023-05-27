import tkinter as tk
from CareerGUI import CareerGUI
from ExploreGUI import ExploreGUI

class Menu:
    def __init__(self, user, recommendations):
        self.window = tk.Tk()
        self.window.title("MyCareer Menu")
        self.window.geometry("300x400")
        self.window.configure(bg="#F4F4F4")
        self.user = user
        print(self.user.username)
        self.recommendations = recommendations
        self.buttons = []  
        self.create_widgets()

    def create_widgets(self):
 
        title_label = tk.Label(self.window, text="MyCareer Menu", font=("Arial", 16), bg="#F4F4F4")
        title_label.pack(pady=10)


        line1 = tk.Frame(self.window, height=2, bd=1, relief=tk.SUNKEN)
        line1.pack(fill=tk.X, padx=5, pady=5)


        explore_button = tk.Button(self.window, text="Explorar", font=("Arial", 12), bg="#2196F3", fg="white",
                               command=lambda: self.explore_action())
        explore_button.pack(pady=10)

        line2 = tk.Frame(self.window, height=2, bd=1, relief=tk.SUNKEN)
        line2.pack(fill=tk.X, padx=5, pady=5)


        message_label = tk.Label(self.window, text="Para ti", font=("Arial", 16), bg="#F4F4F4")
        message_label.pack(pady=10)

        self.generate_buttons()

    def generate_buttons(self):

        for i, element in enumerate(self.recommendations):
            button = tk.Button(self.window, text=str(element), command=lambda i=i: self.button_action(i))
            button.pack(pady=5)
            self.buttons.append(button)  

    def update_buttons(self, new_recommendations):

        print(self.user.username)
        for button in self.buttons:
            button.destroy()

        self.recommendations = new_recommendations
        self.buttons = []  
        self.generate_buttons()

    def like_action(self):
        print("Tus me gusta button clicked")

    def explore_action(self):
        ExploreGUI(self.user.careerNames,self, self.user)

    def button_action(self, index):

        self.window.withdraw()
        CareerGUI(self.recommendations[index], self, self.user)

    def update_user(self, new_user):

        self.user = new_user
        

    def run(self):
        self.window.mainloop()
