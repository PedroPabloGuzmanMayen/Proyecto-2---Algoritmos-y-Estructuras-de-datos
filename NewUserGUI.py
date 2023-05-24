import tkinter as tk
from new_window import NewWindow

class NewUserGUI:
    def __init__(self, root, array):
        self.root = root
        self.array = array

        self.create_buttons()

    def create_buttons(self):
        self.buttons = []
        for i, element in enumerate(self.array):
            button = tk.Button(self.root, text=str(element), command=lambda i=i: self.open_window(i))
            button.pack()
            self.buttons.append(button)

    def open_window(self, index):
        if 0 <= index < len(self.array):
            element = self.array[index]

            # Create a new window
            window = tk.Toplevel(self.root)
            window.title("Element Window")

            # Close the main window
            self.root.withdraw()

            # Create an instance of the NewWindow class
            new_window = NewWindow(window, element, lambda e: self.delete_element(e, index), self.go_back)

            # Callback function to go back and destroy the new window
            def close_window():
                window.destroy()
                self.root.deiconify()

            new_window.close_callback = close_window

    def delete_element(self, element, index):
        if element in self.array:
            self.array.remove(element)
            self.buttons[index].destroy()
            self.buttons.pop(index)

    def go_back(self):
        self.root.deiconify()

# Example usage
if __name__ == '__main__':
    # Sample array
    my_array = [1, 2, 3, 4, 5]

    # Create the Tkinter window
    root = tk.Tk()

    # Create an instance of the NewUserGUI class
    gui = NewUserGUI(root, my_array)

    # Start the Tkinter event loop
    root.mainloop()
