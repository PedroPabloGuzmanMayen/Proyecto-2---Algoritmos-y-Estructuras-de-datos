from Data_Manager import Data_Manager
data_manager = Data_Manager()
data_manager.getLogInData()
data_manager.getCareer_feature()

# Access the usernames, passwords, career-feature matrix, career names, and feature names
usernames = data_manager.usernames
passwords = data_manager.passwords
career_feature = data_manager.Career_feature
career_names = data_manager.career_names
feature_names = data_manager.feature_names

# Print the lists and matrix
print("Usernames:", usernames)
print("Passwords:", passwords)
print("Career-Feature Matrix:")
print(career_feature)
print("Career Names:", career_names)
print("Feature Names:", feature_names)
