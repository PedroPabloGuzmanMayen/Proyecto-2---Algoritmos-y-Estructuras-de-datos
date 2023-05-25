import tkinter as tk
from tkinter import messagebox
from Data_Manager import Data_Manager
from LogIn import LogIn 
from User import user

class NewUser:
    def __init__(self):
        self.window = tk.Tk()

        self.window.title("New user")
        self.window.geometry("300x200")
        self.window.configure(bg="#F4F4F4")


        self.data = Data_Manager()
        self.data.getLogInData()

        self.usernames = self.data.usernames
        self.passwords = self.data.passwords
        print(self.usernames)
        print(self.passwords)
        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        # Title label
        title_label = tk.Label(self.window, text="Crear usuario", font=("Arial", 16), bg="#F4F4F4")
        title_label.pack(pady=10)

        # Username label and entry
        username_label = tk.Label(self.window, text="Nombre de usuario", font=("Arial", 12), bg="#F4F4F4")
        username_label.pack()
        username_entry = tk.Entry(self.window, font=("Arial", 12))
        username_entry.pack(pady=5)

        # Password label and entry
        password_label = tk.Label(self.window, text="Contraseña", font=("Arial", 12), bg="#F4F4F4")
        password_label.pack()
        password_entry = tk.Entry(self.window, show="*", font=("Arial", 12))
        password_entry.pack(pady=5)

        # Login button
        login_button = tk.Button(self.window, text="Login", font=("Arial", 12), bg="#4CAF50", fg="white",
                                 command=lambda: self.login(username_entry.get(), password_entry.get()))
        login_button.pack(pady=10)

    def login(self, username, password):
        if username == "" or password =="":
            messagebox.showinfo("Error", "Ingresa un valor")
        if not password.isnumeric() and username != "":
            messagebox.showinfo("Error","Solo se aceptan contraseñas con valores númericos")
        if (password.isnumeric() and (password != "" and username != "")):
            if username in self.usernames:
                messagebox.showinfo("Error","Nombre de usuario ya existente, intenta con otro")
            else: 
                print("Muy bien")

hola = NewUser()

