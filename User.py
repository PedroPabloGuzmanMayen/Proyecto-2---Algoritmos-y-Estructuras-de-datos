import numpy as np
#Servirá para guardar las matrices y trasladarlas de un archivo a otro
class user:
    def __init__(self, username ,  user_feature, user_ratedCareers, ratedcareers, unratedCareers, feature_names, feature_unratedCareers, ratedcareer_feature, predictionNames, user_Predictions) :
        self.username = username #El nombre de usuario
        self.user_feature = user_feature #La matriz con las preferencias del usuario
        self.user_RatedCareers = user_ratedCareers #Matriz con las carreras ya valoradas
        self.ratedCareers = ratedcareers #Lista con los nombres de las carreras valoradas por el usuario
        self.unratedCareers = unratedCareers #Lista con los nombres de las carreras no valoradas del usuario
        self.featurenames = feature_names #Lista con el nombre de las características
        self.feature_Unrated = feature_unratedCareers #Matriz con las características de las carreras no valoradas por el usuario
        self.predictionNames = predictionNames #Lista con los nombres de las carreras recomendadas al usuario
        self.userPredictions = user_Predictions #Lista con los valores predichos del usuario