import tkinter as tk


class FirstPage:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Welcome")

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
        new_user_button = tk.Button(buttons_frame, text="Nuevo Usuario", font=("Arial", 12))
        new_user_button.pack(side=tk.LEFT, padx=5)

        # Create the "Usuario existente" button
        existing_user_button = tk.Button(buttons_frame, text="Usuario existente", font=("Arial", 12))
        existing_user_button.pack(side=tk.LEFT, padx=5)

        # Load and display the image
        image = tk.PhotoImage(file="Logo.png")
        image_label = tk.Label(content_frame, image=image)
        image_label.pack(pady=10)

        # Configure window resizing behavior
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        content_frame.grid_rowconfigure(1, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)

        # Bind window resizing event
        self.window.bind("<Configure>", self.on_window_resize)

        self.window.mainloop()

    def on_window_resize(self, event):
        # Adjust the size of the content frame and the image label
        self.window.update_idletasks()
        content_width = self.window.winfo_width() - 20
        content_height = self.window.winfo_height() - 40
        self.window.geometry(f"{content_width}x{content_height}")
        self.window.update_idletasks()

# Create an instance of the FirstPage class
page = FirstPage()
