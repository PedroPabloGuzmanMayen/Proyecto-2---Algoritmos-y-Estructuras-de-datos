import tkinter as tk
from LogInGUI import LogInGUI
class FirstPage:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bienvenido")

        # Create a frame for the content
        content_frame = tk.Frame(self.window)
        content_frame.pack(pady=20)

        # Create a label with the message
        label = tk.Label(content_frame, text="Bienvenido", font=("Arial", 16))
        label.pack(pady=10)

        # Create a frame for the buttons and image
        buttons_frame = tk.Frame(content_frame)
        buttons_frame.pack(pady=10)

        # Create the "Nuevo Usuario" button
        new_user_button = tk.Button(buttons_frame, text="Nuevo Usuario", font=("Arial", 12), command=self.open_new_user_window)
        new_user_button.pack(side=tk.LEFT, padx=5)

        # Create the "Usuario existente" button
        existing_user_button = tk.Button(buttons_frame, text="Usuario existente", font=("Arial", 12), command=self.open_login_window)
        existing_user_button.pack(side=tk.LEFT, padx=5)

        # ... existing code ...

        self.window.mainloop()

    def open_new_user_window(self):
        pass

    def open_login_window(self):
        self.window.destroy()
        LogInGUI()

# Create an instance of the FirstPage class
first = FirstPage()
