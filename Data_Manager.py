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
        MATCH (u:User {username: $username})-[:RATES]->(c:Career)
        WHERE c.rating <> -1
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
        MATCH (u:User {username: $username})-[:RATES]->(c:Career)
        WHERE c.rating = -1
        RETURN c.name AS career_name
        """
      with self.driver.session() as session:
         result = session.run(query, username=username)
         for record in result:
            unrated_careers.append(record["career_name"])
      return unrated_careers

         
