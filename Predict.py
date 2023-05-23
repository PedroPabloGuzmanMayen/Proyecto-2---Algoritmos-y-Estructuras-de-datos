import numpy as np
class Predict:
     #Obtiene las posibles valoraciones del usuario a las carreras con las que no ha interactuado
     def predict(self, user_feature, feature_unratedCareer): #user_feature: matriz con la valoración del usuario a cada característica de la carrera, #feature_unratedCareer: matriz que muestra la relación entre las carreras no valoradas y cada característica
         predicted_ratings = np.matmul(user_feature, feature_unratedCareer) #Multiplicar las matrices
         predicted_ratings = predicted_ratings*5
         return predicted_ratings #retornar el resultado de la multiplicación
     #Sirve para normalizar la matriz usario-característica
     def normalize(self, user_feature): #user_featue: matriz con la valoracion del usuario a una caracteristica
         number = np.sum(user_feature) #Sumar todos los elementos de la fila 0 de la matriz
         escalar = 1/number #Definir un escalar utilizando el resultado de la suma anterior
         user_feature = user_feature * escalar #Multiplicar la matriz y el escalar
         return user_feature #Retornar la matriz normalizada
     #Sirve para obtener la matriz con la valoración del usuario a cada característica
     def getUser_feature(self, user_ratedCareers, ratedCareers_feature): #user_ratedCareers: matriz con la valoración del usuario a las carreras con las que ha interactuado, ratedCareer_feature: matriz con la relación entre las carreras valoradas por el usuario y las características
         user_feature = np.matmul(user_ratedCareers,ratedCareers_feature) #Multiplicar las matrices 
         user_feature = self.normalize(user_feature) #Normalizar la nueva matriz obtenida
         return user_feature #Retornar el valor
     
