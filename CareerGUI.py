import tkinter as tk
class CareerGUI:
   def __init__(self, career_name, user):
      self.window = tk.Tk()
      self.window.title("MyCareer Menu")
      self.window.geometry("300x400")
      self.window.configure(bg="#F4F4F4")
      self.window.mainloop()
      self.user = user
      self.name = career_name

   def generateWidgets():
      pass

