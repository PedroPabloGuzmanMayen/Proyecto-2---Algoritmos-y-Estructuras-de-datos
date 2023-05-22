from Data_Manager import Data_Manager
data_manager = Data_Manager()
data_manager.getLogInData()


# Access the usernames, passwords, career-feature matrix, career names, and feature names
usernames = data_manager.usernames
passwords = data_manager.passwords
ratedcareers = data_manager.getRatedCareers("Freddie")
unratedcareers = data_manager.getUnratedCareers("Freddie")
ratingMatrix = data_manager.createUserRating("Freddie",ratedcareers)
CareerFeature = data_manager.getCareerFeature("Freddie")
feature_names = data_manager.getFeaturenames()
var = data_manager.getName(ratedcareers,feature_names)
matrix = data_manager.test(ratedcareers,feature_names, "strong","MATCH (c:Career{name:$career})-[r:HAS_TAG]->(f:Feature{name:$feature}) RETURN r.Strong AS strong")

# Print the lists and matrix
print("Usernames:", usernames)
print("Passwords:", passwords)
print()
print(ratedcareers)
print()
print(unratedcareers)
print()
print(ratingMatrix)
print()
print(feature_names)
print()
print(matrix)
print()

