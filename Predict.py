import numpy as np
class Predict:

     def predict(self, user_feature, feature_unratedCareer):
         predicted_ratings = np.matmul(user_feature, feature_unratedCareer)
         return predicted_ratings
     
     def normalize(self, user_feature):
         number = np.sum(user_feature[0])
         escalar = 1/number
         user_feature = user_feature * escalar
         return user_feature
     def getUser_feature(self, user_ratedCareers, ratedCareers_feature):
         user_feature = np.matmul(user_ratedCareers,ratedCareers_feature)
         self.normalize(user_feature)
         return user_feature
     
     def getRecomendation():
         pass