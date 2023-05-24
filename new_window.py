import tkinter as tk

class NewWindow:
    def __init__(self, root, element, delete_callback, close_callback):
        self.root = root
        self.element = element
        self.delete_callback = delete_callback
        self.close_callback = close_callback

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Element: {}".format(self.element))
        self.label.pack()

        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_element)
        self.delete_button.pack()

        self.go_back_button = tk.Button(self.root, text="Go back", command=self.close_callback)
        self.go_back_button.pack()

    def delete_element(self):
        if self.delete_callback:
            self.delete_callback(self.element)
            self.close_callback()

