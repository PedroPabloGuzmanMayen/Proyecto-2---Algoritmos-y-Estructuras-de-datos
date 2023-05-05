import numpy as np
class user:
    def __init__(self) :
        self.username = ""
        self.password = ""
        self.user_feature = np.array([[]])
        self.user_career = np.array([[]])
        self.user_predictions = np.array([[]])
        self.user_rated_careers = []
        self.user_not_rated_careers = []