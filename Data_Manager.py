from neo4j import GraphDatabase
import numpy as np

class Data_Manager:
   def __init__(self):
      self.driver = GraphDatabase.driver("neo4j+s://b0a9a659.databases.neo4j.io", auth=("neo4j", "n9_qBLezCVCaPJaivvf08qdDk47l4UGKaTx1x_d5QDk"))
      self.usernames =[]
      self.passwords =[]
      self.Career_feature = np.empty((0, 0))
      self.career_names = []
      self.feature_names =[]
   def getLogInData(self):
      with self.driver.session() as session:
         result = session.run("MATCH (u:User) RETURN u.username AS username, u.password AS password")

         for record in result:
            self.usernames.append(record["username"])
            self.passwords.append(record["password"])

   def getCareer_feature(self):
        with self.driver.session() as session:
         result = session.run("MATCH (c:Career)-[r:HAS_TAG]->(f:Feature) RETURN c.name AS career_name, f.name AS feature_name, r.Strong AS strong")

         for record in result:
            career_name = record["career_name"]
            feature_name = record["feature_name"]
            strong = record["strong"]

            if career_name not in self.career_names:
                self.career_names.append(career_name)

            if feature_name not in self.feature_names:
                self.feature_names.append(feature_name)

            career_index = self.career_names.index(career_name)
            feature_index = self.feature_names.index(feature_name)

            if career_index >= self.Career_feature.shape[0]:
                self.Career_feature = np.pad(self.Career_feature, ((0, career_index - self.Career_feature.shape[0] + 1), (0, 0)), mode='constant')
            if feature_index >= self.Career_feature.shape[1]:
                self.Career_feature = np.pad(self.Career_feature, ((0, 0), (0, feature_index - self.Career_feature.shape[1] + 1)), mode='constant')

            self.Career_feature[career_index][feature_index] = strong

   def getUserLikedCareers():
      pass
   def getUserNotLikedCareers():
      pass
   def getUserCareer():
      pass
   
