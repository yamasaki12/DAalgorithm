class Student:
    def __init__(self, name, preference):
        self.preference = preference
        self.name = name
        self.rejectcount = 0

    def tempPref(self):
        return self.preference[self.rejectcount]
    

class School:
    def __init__(self, name, capacity, preference):
        self.name = name
        self.preference = preference
        self.capacity = capacity
        self.temporaryList = []

def matching(students, schools):
    poolList = students
    differdAccept = schools

    def choice(student, school):
        if school.capacity > len(school.temporaryList):
            index = school.preference.index(student.name)
            i = 1
            while len(school.preference) > i:
                if school.temporaryList == [] or index < school.preference.index(school.temporaryList[-i].name):
                    school.temporaryList.append(student)
                    break
                else:
                    i += 1
            return None, school
        elif school.preference.index(student.name) < school.preference.index(school.temporaryList[-1].name):
            rejectstudent = school.temporaryList[-1]
            rejectstudent.rejectcount += 1
            del school.temporaryList[-1]
            i = 1
            while len(school.preference) > i:
                if school.temporaryList == [] or index < school.preference.index(school.temporaryList[-i].name):
                    school.temporaryList.append(student)
                    break
                else:
                    i += 1
            return rejectstudent, school
        else:
            rejectstudent = student
            rejectstudent.rejectcount += 1
            return rejectstudent, school

    while len(poolList)>0:
        school = next(school for school in differdAccept if school.name == poolList[0].tempPref())  
        index = schools.index(school) 
        select = choice(poolList[0], school)
        if select[0] == None:
            del poolList[0]
            differdAccept[index] = school
        else:
            del poolList[0]
            poolList.append(select[0]) 
            differdAccept[index] = school
    
    matching = {} 
    for school in differdAccept:
        i = 0
        while len(school.temporaryList) > i:
            school.temporaryList[i] = school.temporaryList[i].name
            i += 1
        matching[school.name] = school.temporaryList
    return matching
    
