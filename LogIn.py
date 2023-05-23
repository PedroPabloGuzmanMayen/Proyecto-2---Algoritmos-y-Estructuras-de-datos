class LogIn:
     def __init__(self):
        pass
     def checkData(self, username, password, array1, array2):
         if username not in array1:
             return False
         else:
            userIndex = array1.index(username)
            if(password == array2[userIndex] and username == array2[userIndex]):
                return True
            else: 
                return False
            
     def newUser(username, array1):
         if (username in array1):
             return False
         else:
             return True
