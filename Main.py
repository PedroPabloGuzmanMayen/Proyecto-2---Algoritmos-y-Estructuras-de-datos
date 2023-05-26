from Data_Manager import Data_Manager
from Predict import Predict
from Recommend import Recommend
import numpy as np
data_manager = Data_Manager()
predictor = Predict()
recommender = Recommend()
data_manager.getLogInData()


# Definir las variables
usernames = data_manager.usernames
passwords = data_manager.passwords
ratedcareers = data_manager.getRatedCareers("Freddie") #Carreras valoradas por Freddie
print(ratedcareers)

unratedcareers = data_manager.getUnratedCareers("Freddie") #Carreras no valoradas por Freddie
print(unratedcareers)
ratingMatrix = data_manager.createUserRating("Freddie", ratedcareers) #Ratings dados por Freddie
print(ratingMatrix)

feature_names = data_manager.getFeaturenames() #Nombre de las features
print(feature_names)
CareerFeatureMatrix = data_manager.getName(ratedcareers, feature_names) #Relación entre las características y las carreras valoradas por Freddie
print(CareerFeatureMatrix)
FeatureCareerMatrix = data_manager.getName2(feature_names, unratedcareers) #Relación entre las características y carreeras no valoradas por Freddie
print(FeatureCareerMatrix)


#Predecir
User_feature = predictor.getUser_feature(ratingMatrix, CareerFeatureMatrix)
print(User_feature)
User_possible = predictor.predict(User_feature, FeatureCareerMatrix)
print(User_possible)
Recommended_carreers = recommender.recommend(User_possible, unratedcareers)

for i in range(len(Recommended_carreers)):
    print(Recommended_carreers[i])






