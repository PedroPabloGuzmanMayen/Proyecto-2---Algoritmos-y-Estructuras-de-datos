import tkinter as tk
from tkinter import messagebox

class LoginPage:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login")
        self.window.geometry("300x200")

        # Create a label with the title
        title_label = tk.Label(self.window, text="Login", font=("Arial", 16))
        title_label.pack(pady=20)

        # Create username label and entry field
        username_label = tk.Label(self.window, text="Username:")
        username_label.pack()
        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack()

        # Create password label and entry field
        password_label = tk.Label(self.window, text="Password:")
        password_label.pack()
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack()

        # Create the login button
        login_button = tk.Button(self.window, text="Login", command=self.login)
        login_button.pack(pady=10)

        self.window.mainloop()

    def login(self):
        # Get the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the username and password are valid
        if username == "admin" and password == "password":
            messagebox.showinfo("Success", "Login Successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password")

# Create an instance of the LoginPage class
page = LoginPage()
