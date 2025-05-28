from collections import defaultdict
from itertools import combinations
import json
from affinity_controller import AffinityController
import os

class GroupingController:
    
    def __init__(self,group_size):

        self.group_size = group_size
        #student list containing votes for each other.
        self.student_matrix_path = os.path.join("backend","controller","student_list.json")
        self.affinity_matrix_path = os.path.join("backend","controller","student_affinity.json")

    #Load the json file with the student votes.
    def load_student_vote_list(self):
        with open(self.student_matrix_path, "r") as f:
            data = json.load(f)
        
        student_list = data["students"]  
        #create dict object for the student votes.
        student_vote_dict = dict(item for s in student_list for item in s.items())  
        
        return student_vote_dict  

        
    # Build the dict of affinity for each students.
    def build_affinity_matrix(self):
        #retrieves each students.
        students = list(self.load_student_vote_list().keys())
        student_vote_dict = self.load_student_vote_list()

        #build empty dict object.
        affinity_dict = defaultdict(dict)

        #Loop to create combinations between students votes (without duplicate)
        for student_1, student_2 in combinations(students,2 ):

            try:
                vote_1 = student_vote_dict[student_1][student_2]
                vote_2 = student_vote_dict[student_2][student_1]

                affinity = AffinityController(student_1,student_2,vote_1,vote_2).get_affinity()
               
                affinity_dict[student_1][student_2] = affinity
                affinity_dict[student_2][student_1] = affinity

            #in the cas where a students didn't vote for another.
            except KeyError:
                continue
            
        return dict(affinity_dict)
    
    #write the affinity matrix in a json file named (student_affinity)
    def write_affinity_matrix_in_json(self):
        affinity_matrix = self.build_affinity_matrix()

        with open(os.path.join("backend","controller","student_affinity.json"), "w") as f:
            json.dump(affinity_matrix, f)
    
    def get_affinity_matrix_path(self):
        return self.affinity_matrix_path

    def get_affinity_matrix(self):
        with open(self.affinity_matrix_path,"r") as f:
            data = json.load(f)

        return data
    
    # build group using greedy algorithm
    def build_groups(self):
        
        affinity_matrix = self.get_affinity_matrix()
        students = list(affinity_matrix.keys())
        groups = []
        non_assing_students = set(students)
        
        #iterate until the most of student have a group
        while len(non_assing_students) >= self.group_size:
            current_group = []
            
            #if the current group is empty
            if not current_group:
                #best student => best avg affinity with non assigned students 
                best_student = max(non_assing_students, 
                                    key=lambda e: self.avg_affinity(e, non_assing_students, affinity_matrix))
                current_group.append(best_student)
                non_assing_students.remove(best_student)
            
            # add other student to the group 
            while len(current_group) < self.group_size and non_assing_students:
                
                best_student = None
                best_affinity = -1 # we compare it to group_affinity -> -1 in the case where group_affinity is 0  
                
                #find the student in non assign student which have the most affinity with the others
                for student in non_assing_students:
                    group_affinity = self.affinity_with_group(student, current_group, affinity_matrix)
                    if group_affinity > best_affinity:
                        best_affinity = group_affinity
                        best_student = student
                #Add the student to the group
                if best_student:
                    current_group.append(best_student)
                    non_assing_students.remove(best_student)

            #add the current group to all the groups list
            groups.append(current_group)
        
        # in the case where there is still non asign students
        if non_assing_students:
            # add them to the last group if still space or create new group
            if len(non_assing_students) >= self.group_size // 2:
                groups.append(list(non_assing_students))

            elif groups:
                remaining_students = list(non_assing_students)
                for i, student in enumerate(remaining_students):
                    groups[i % len(groups)].append(student)
        
        return groups

    #Calculate average affinity between one student and all the other student
    def avg_affinity(self,student, other_students, matrix):
        #in the case where other_student list is empty
        if len(other_students) <= 1:
            return 0
        # total = sum of the affinity of the sutdent with all other student except himself.
        total = sum(matrix[student].get(other, 0) 
                for other in other_students if other != student)
        
        # avg of the total (length of other student list - 1 ( without him))
        return total / (len(other_students) - 1)

    def affinity_with_group(self,student, group, matrix):
        #calculate affinity of a student with a goup
        return sum(matrix[student].get(membre, 0) for membre in group)

    def evaluate_group_score(self,groups, matrix):
        #evaluate groups affinity score
        result = []
        total_affinity = 0
        
        for i, group in enumerate(groups):
            group_affinity = 0
            nb_pairs = 0
            
            # calculate group affinity
            for j in range(len(group)):
                for k in range(j + 1, len(group)):
                    affinity = matrix[group[j]].get(group[k], 0)
                    group_affinity += affinity
                    nb_pairs += 1
            
            avg_affinity = group_affinity / nb_pairs if nb_pairs > 0 else 0 #division by 0 is impossible.
            total_affinity += group_affinity
            
          
        
        return result, total_affinity , avg_affinity


    


if __name__ == "__main__":
  
    gc = GroupingController(3)
    print(gc.build_groups())
        
    # def create_groups(self)
   
    #def greedy_grouping(self)
    #def calculate_group_scores(self)

