from neo4j import GraphDatabase
import numpy as np

class Data_Manager:
   #Inicializa las variables de la clase
   def __init__(self):
      self.driver = GraphDatabase.driver("neo4j+s://b0a9a659.databases.neo4j.io", auth=("neo4j", "n9_qBLezCVCaPJaivvf08qdDk47l4UGKaTx1x_d5QDk"))
      self.usernames =[]
      self.passwords =[]
      self.Career_feature = np.empty((0, 0))
      self.career_names = []
      self.feature_names =[]
   #Obtiene los datos que son necesarios para el Login
   def getLogInData(self):
      with self.driver.session() as session:
         result = session.run("MATCH (u:User) RETURN u.username AS username, u.password AS password")

         for record in result:
            self.usernames.append(record["username"])
            self.passwords.append(record["password"])
   #Obtiene los nombres de las carreras ya evaluadas por el usuario
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
   #Obtiene las carreras que aún no han sido evaluadas por el usuario 
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
   #Crea la matriz usuario-rating con las carreras que el usuario ya ha evaluado
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
   
    #Obtiene los nombres de las etiquetas
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
   #Obtiene las matrices career-feature y feature-career
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
   '''
   Guardar el método para encontrar la posible solución más eficiente
   def matrixGenerator(self, array1, array2, query, key):
       matrix= np.zeros((len(array1), len(array2)))
       with self.driver.session() as session:
         for i in range(len(array1)):
             pass
             for j in range(len(array2)):
               result = session.run(query, array1=array1[i],array2=array2[j] )
               for record in result:
                   matrix[i][j] = record[key]

         return matrix

   def arrayGenerator(self, username, query, key):
      with self.driver.session() as session:
         
      
   ''' 
   def getName2(self, feature, career):
       career_feature = np.zeros((len(feature), len(career)))
       with self.driver.session() as session:
         for i in range(len(feature)):
             pass
             for j in range(len(career)):
               query = """
                 MATCH (c:Career{name:$career})-[r:HAS_TAG]->(f:Feature{name:$feature})
                 RETURN r.Strong AS strong
                 """
               result = session.run(query, career=career[j],feature=feature[i] )
               for record in result:
                   career_feature[i][j] = record["strong"]

         return career_feature
       
   def setRating(self,username, rating, career):
      query= """
         MATCH(u:User{username:$username})-[r:RATES]->(c:Career{name:$career})
         SET r.Rating = $rating
         """
      with self.driver.session() as session:
         session.run(query, username=username,rating=rating, career=career)
      
      
   def createUser(username, password):
      query = """
      CREATE(u:User{username:$username, password:$password})
      MATCH(c:Career)
      CREATE (u)-[:RATES{rating:-1}]->(c)
      """
       
   

