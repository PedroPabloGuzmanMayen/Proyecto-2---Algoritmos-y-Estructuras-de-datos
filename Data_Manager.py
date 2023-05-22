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

   def getRatedCareers(self, username):
      rated_careers =[]
      query = """
        MATCH (u:User {username: $username})-[r:RATES]->(c:Career)
        WHERE r.rating <> -1
        RETURN c.name AS career_name
        """
      with self.driver.session() as session:
         result = session.run(query, username=username)
         for record in result:
            rated_careers.append(record["career_name"])
      return rated_careers
   
   def getUnratedCareers(self,username):
      unrated_careers =[]
      query = """
        MATCH (u:User {username: $username})-[r:RATES]->(c:Career)
        WHERE r.rating = -1
        RETURN c.name AS career_name
        """
      with self.driver.session() as session:
         result = session.run(query, username=username)
         for record in result:
            unrated_careers.append(record["career_name"])
      return unrated_careers
   def createUserRating(self,name,ratedCareers):
        query = """
        MATCH (u:User{username: $name})-[r:RATES]->(c:Career)
        WHERE r.rating <> -1
        RETURN u.username AS username, c.name AS career_name, r.rating AS rating
        """
        with self.driver.session() as session:
            result = session.run(query,name=name)
            UserRating = np.zeros(len(ratedCareers))
            ratings =[]

            for record in result:
               ratings.append(record["rating"])
            
            for i in range (len(ratings)):
               UserRating[i]=ratings[i]

            return UserRating

   def getCareerFeature(self, name):
    with self.driver.session() as session:
            query = """
            MATCH (u:User{username: $name})-[h:RATES]-(c:Career)-[r:HAS_TAG]->(f:Feature)
            WHERE h.rating <> -1
            RETURN c.name AS career_name, f.name AS feature_name, r.Strong AS strong
            """

            result = session.run(query,name=name)

            career_names = []
            feature_names = []
            data = []

            for record in result:
                career_name = record["career_name"]
                feature_name = record["feature_name"]
                strong = record["strong"]

                if career_name not in career_names:
                    career_names.append(career_name)

                if feature_name not in feature_names:
                    feature_names.append(feature_name)

                data.append((career_name, feature_name, strong))

            career_names = career_names
            feature_names = feature_names

            career_feature = np.zeros((len(career_names), len(feature_names)))

            for career_name, feature_name, strong in data:
                career_index = career_names.index(career_name)
                feature_index = feature_names.index(feature_name)

                career_feature[career_index, feature_index] = strong

            return career_feature
    
   def getFeaturenames(self):


       with self.driver.session() as session:
            features_names=[]
            query = """
            MATCH (c:Career)-[r:HAS_TAG]->(f:Feature)
            RETURN f.name AS feature_names
            """
            result = session.run(query)
            for record in result:
                features_names.append(record["feature_names"])
            
            features_names = list(dict.fromkeys(features_names))

            return features_names
   
   def getName(self, career, feature):
       career_feature = np.zeros((len(career), len(feature)))
       with self.driver.session() as session:
         for i in range(len(career)):
             pass
             for j in range(len(feature)):
               query = """
                 MATCH (c:Career{name:$career})-[r:HAS_TAG]->(f:Feature{name:$feature})
                 RETURN r.Strong AS strong
                 """
               result = session.run(query, career=career[i],feature=feature[j] )
               for record in result:
                   career_feature[i][j] = record["strong"]

         return career_feature
       
   def test(self, career, feature, string, query):
       matrix= np.zeros((len(career), len(feature)))
       with self.driver.session() as session:
         for i in range(len(career)):
             pass
             for j in range(len(feature)):
               result = session.run(query, career=career[i],feature=feature[j] )
               for record in result:
                   matrix[i][j] = record[string]

         return matrix
"MATCH (c:Career{name:$career})-[r:HAS_TAG]->(f:Feature{name:$feature}) RETURN r.Strong AS strong"
