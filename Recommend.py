class Recommend:
    #Determina que carreras recomedar al usuario 
    def recommend(self, user_Predicted_ratings, notRated_careers): #user_Predicted_ratings: la matriz que contiene las posibles valoraciones del usuario, notRated_careers: lista que contiene las carreras aún no valoradas por el usuario 
        recommended_careers = [] #Hacer la lista de las carreras que se le recomendaran al usuario
        for i in range(len(notRated_careers)):
            if (user_Predicted_ratings[0] > 3.0): #Si el valor es mayor que 3, ingresar el valor a la lista de reocmendaciones
                recommended_careers.append(notRated_careers[i])
        return recommended_careers #Retornar las carreras recomendadas para el usuario