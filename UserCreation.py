import tkinter as tk
from tkinter import messagebox
import numpy as np
from Data_Manager import Data_Manager
from User import user
from Predict import Predict
from Recommend import Recommend
from MainMenu import Menu

class UserCreationGUI:
    def __init__(self, array, np_array, username):
        self.array = array
        self.np_array = np_array
        self.index = 0
        self.username = username
        self.data = Data_Manager()
        self.predictor = Predict()
        self.recomendatior = Recommend()
        self.window = tk.Tk()
        self.window.title("User Creation")
        self.window.geometry("300x200")
        self.window.configure(bg="#F4F4F4")

        self.label_message = tk.Label(self.window, text="Creando tu usuario", font=("Arial", 16), bg="#F4F4F4", fg="#000000")
        self.label_message.pack(pady=10)

        line = tk.Frame(self.window, height=2, width=300, bg="#000000")
        line.pack()

        self.label_array_element = tk.Label(self.window, text=self.array[self.index], font=("Arial", 12), bg="#F4F4F4", fg="#000000")
        self.label_array_element.pack(pady=10)

        self.entry_value = tk.Entry(self.window)
        self.entry_value.pack(pady=5)

        self.button_next = tk.Button(self.window, text="Siguiente", command=self.nextClicked, bg="#ECECEC", fg="#000000")
        self.button_next.pack(pady=10)

        self.window.mainloop()

    def nextClicked(self):
        value = self.entry_value.get()
        if value == "":
            messagebox.showinfo("Error", "Ingresa un valor")
        elif not value.isnumeric():
            messagebox.showinfo("Error", "Por favor ingresa un valor numérico")
        else:
            self.np_array[self.index] += float(value)
            self.index += 1
            if self.index == len(self.array):
                Rated_Careers = self.data.getRatedCareers(self.username)
                Unrated_Careers = self.data.getUnratedCareers(self.username)
                userRating = self.data.createUserRating(self.username, Rated_Careers)
                Features = self.data.getFeaturenames()
                career_Feature = self.data.getName(Rated_Careers,Features)
                feature_career = self.data.getName2(Features, Unrated_Careers)
                User_feature = self.predictor.normalize(self.np_array)
                print(User_feature)
                Predictions = self.predictor.predict(User_feature, feature_career)
                print(Predictions)
                Recomendations = self.recomendatior.recommend(Predictions, Unrated_Careers)
                print(Recomendations)
                Names = self.data.getNames()
                User = user(self.username, User_feature, userRating, Rated_Careers, Unrated_Careers, Features, feature_career, career_Feature, Recomendations, Predictions, Names)

                self.window.destroy()
                Menu(User, Recomendations)
                
            else:
                self.label_array_element.config(text=self.array[self.index])
                self.entry_value.delete(0, tk.END)

