from Data_Manager import Data_Manager
from Predict import Predict
from Recommend import Recommend
data_manager = Data_Manager()
predictor = Predict()
recommender = Recommend()
data_manager.getLogInData()


# Definir las variables
usernames = data_manager.usernames
passwords = data_manager.passwords
ratedcareers = data_manager.getRatedCareers("Freddie")
print("Carreras valoradas por el usuario: ")
print()
print(ratedcareers)
print()
unratedcareers = data_manager.getUnratedCareers("Freddie")
print("Carreras no valoradas: ")
print(unratedcareers)
print()
ratingMatrix = data_manager.createUserRating("Freddie", ratedcareers)
print("Valoraciones del usuario a las carreras con la que ha interactuado: ")
print(ratingMatrix)
print()

feature_names = data_manager.getFeaturenames()
print("Nombre de las características: ")
print(feature_names)
print()
CareerFeatureMatrix = data_manager.getName(ratedcareers, feature_names)
print("Carrera y cada etiqueta: ")
print(CareerFeatureMatrix)
print()
FeatureCareerMatrix = data_manager.getName(feature_names, ratedcareers)
print("Caracteristica y cada carrera: ")
print(FeatureCareerMatrix)
print()
#Predecir
#User_feature = predictor.getUser_feature(ratingMatrix, CareerFeatureMatrix)
#User_possible = predictor.predict(User_feature, FeatureCareerMatrix)
#Recommended_carreers = recommender.recommend(User_possible, unratedcareers)
'''
for i in range(len(Recommended_carreers)):
    print(Recommended_carreers[i])
'''



