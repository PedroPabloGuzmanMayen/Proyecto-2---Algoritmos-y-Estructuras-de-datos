import tkinter as tk
from CareerGUI import CareerGUI

class ExploreGUI:
    def __init__(self, array, menu, user):
        self.window = tk.Tk()
        self.window.title("Liked careers")
        self.window.geometry("300x400")
        self.window.configure(bg="#F4F4F4")
        self.Careers = array
        self.menu = menu
        self.user = user
        self.buttons = []


        header_frame = tk.Frame(self.window, bg="#F4F4F4")
        header_frame.pack(pady=10)

      
        self.back_button = tk.Button(header_frame, text="Atrás", command=lambda: self.goBack(), bg="#ECECEC", fg="#000000")
        self.back_button.pack(side=tk.LEFT, padx=10)

     
        label = tk.Label(header_frame, text="Carreras disponibles", font=("Arial", 16), bg="#F4F4F4", fg="#000000")
        label.pack(side=tk.TOP)


        line = tk.Frame(self.window, height=2, width=300, bg="#000000")
        line.pack()


        for i, element in enumerate(self.Careers):
            button = tk.Button(self.window, text=str(element), command=lambda i=i: self.buttonClicked(i))
            button.pack(pady=5)
            self.buttons.append(button)

        self.window.mainloop()

    def goBack(self):
        self.window.withdraw()
        self.menu.window.deiconify()


    def buttonClicked(self, index):
       self.window.destroy()
       CareerGUI(self.Careers[index], self.menu, self.user)




        