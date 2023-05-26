import tkinter as tk
from Data_Manager import Data_Manager
from tkinter import messagebox
from Recommend import Recommend
from Predict import Predict
class CareerGUI:
    def __init__(self, career_name, menu, user):
        self.menu = menu
        self.user = user
        self.window = tk.Toplevel()
        self.window.title("MyCareer Menu")
        self.window.geometry("300x400")
        self.window.configure(bg="#F4F4F4")
        self.career = career_name
        self.data = Data_Manager()
        self.recomend = Recommend()
        self.predictor = Predict()

        career_label = tk.Label(self.window, text=career_name, font=("Arial", 16), bg="#F4F4F4")
        career_label.pack(pady=20)

    
        textbox = tk.Entry(self.window, font=("Arial", 12))
        textbox.pack()


        valorar_button = tk.Button(self.window, text="Valorar", font=("Arial", 12), bg="#4CAF50", fg="white",
                                   command=lambda: self.valorar_action(textbox.get(), self.user, self.career))
        valorar_button.pack(pady=10)

        back_button = tk.Button(self.window, text="Atrás", font=("Arial", 12), bg="#FF5722", fg="white",
                                command=lambda: self.back_action())
        back_button.pack(side=tk.LEFT, padx=5)

        self.window.protocol("WM_DELETE_WINDOW", self.back_action)

    def valorar_action(self, rating, user, name):
        if rating == "":
            pass
        else:
            self.data.setRating(user.username,int(rating), name)
            self.user.ratedCareers = self.data.getRatedCareers(self.user.username)

            self.user.unratedCareers = self.data.getUnratedCareers(self.user.username)
     
            self.user.user_RatedCareers = self.data.createUserRating(self.user.username, self.user.ratedCareers)
 
            self.user.featurenames = self.data.getFeaturenames()

            career_Feature = self.data.getName(self.user.ratedCareers,self.user.featurenames)

            self.user.feature_Unrated = self.data.getName2(self.user.featurenames, self.user.unratedCareers)
 
            self.user.user_feature = self.predictor.getUser_feature(self.user.user_RatedCareers, career_Feature)

            self.user.userPredictions = self.predictor.predict(self.user.user_feature, self.user.feature_Unrated)

            self.user.predictionNames = self.recomend.recommend(self.user.userPredictions, self.user.unratedCareers)


            self.menu.update_user(self.user)
            self.menu.update_buttons(self.user.predictionNames)
    

    def back_action(self):

        self.window.withdraw()
        self.menu.window.deiconify()
