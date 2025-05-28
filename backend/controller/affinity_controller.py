
import math


class AffinityController:

    def __init__(self, student_1, studdent_2, vote_student_1,vote_student_2):

        self.student_1 = student_1
        self.student_2 = studdent_2
        self.vote_student_1 = vote_student_1
        self.vote_student_2 = vote_student_2
        

    #calculate the affinity between two students bases on
    def get_affinity(self):
        return math.ceil((self.vote_student_1 + self.vote_student_2) / 2)
        
        

        










