import tkinter as tk
from tkinter import messagebox
from Data_Manager import Data_Manager
from LogIn import LogIn 
from User import user
from Predict import Predict
from Recommend import Recommend
from MainMenu import Menu

class LogInGUI:
    def __init__(self):
        self.window = tk.Tk()

        self.window.title("Login")
        self.window.geometry("300x200")
        self.window.configure(bg="#F4F4F4")

        self.login_manager = LogIn()
        self.data = Data_Manager()
        self.predictor = Predict()
        self.recomendatior = Recommend()
        self.data.getLogInData()

        self.usernames = self.data.usernames
        self.passwords = self.data.passwords
        print(self.usernames)
        print(self.passwords)
        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):

        title_label = tk.Label(self.window, text="Login", font=("Arial", 16), bg="#F4F4F4")
        title_label.pack(pady=10)

        username_label = tk.Label(self.window, text="Nombre de usuario", font=("Arial", 12), bg="#F4F4F4")
        username_label.pack()
        username_entry = tk.Entry(self.window, font=("Arial", 12))
        username_entry.pack(pady=5)


        password_label = tk.Label(self.window, text="Contraseña", font=("Arial", 12), bg="#F4F4F4")
        password_label.pack()
        password_entry = tk.Entry(self.window, show="*", font=("Arial", 12))
        password_entry.pack(pady=5)


        login_button = tk.Button(self.window, text="Login", font=("Arial", 12), bg="#4CAF50", fg="white",
                                 command=lambda: self.login(username_entry.get(), int(password_entry.get())))
        login_button.pack(pady=10)

    def login(self, username, password):
        if self.login_manager.checkData(username, password, self.usernames, self.passwords):
            Rated_Careers = self.data.getRatedCareers(username)
            Unrated_Careers = self.data.getUnratedCareers(username)
            userRating = self.data.createUserRating(username, Rated_Careers)
            Features = self.data.getFeaturenames()
            career_Feature = self.data.getName(Rated_Careers,Features)
            feature_career = self.data.getName2(Features, Unrated_Careers)
            User_feature = self.predictor.getUser_feature(userRating, career_Feature)
            Predictions = self.predictor.predict(User_feature, feature_career)
            Recomendations = self.recomendatior.recommend(Predictions, Unrated_Careers)
            Names = self.data.getNames()
            User = user(username, User_feature, userRating, Rated_Careers, Unrated_Careers, Features, feature_career, career_Feature, Recomendations, Predictions, Names)

            self.window.destroy()
            Menu(User, Recomendations)

        else:
            messagebox.showerror("Login", "Invalid username or password.")


