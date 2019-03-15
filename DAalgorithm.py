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
    
    def sortstudent(self, student):
        # 受け入れた提案学生を選好順に並び替え
        priority = self.preference.index(student.name)
        # 仮配属が0名の場合に備え、ひとまずリストの先頭に追加。
        self.temporaryList.insert(0, student)
        for tempstudent in self.temporaryList[::-1]:
            index = self.preference.index(tempstudent.name)
            if self.preference.index(tempstudent.name) < priority:
                self.temporaryList.insert(index, student)
                del self.temporaryList[0]
                break
        return self

    # 提案してきた学生を受け入れるかどうかを決定するメソッド
    def choice(self, student):
        # 定員以下の場合、学校は受け入れ、現在の受け入れリストを学校の選好順に並べる。
        if self.capacity > len(self.temporaryList):
            return None, self.sortstudent(student)
        # 定員を上回る場合、提案学生とリストの最下位の学生の選好順位を比較し、受け入れかどうかを決定。
        # 受け入れの場合は選好順に並び替え
        # rejectされた学生は、poolListに戻される。
        elif self.preference.index(student.name) < self.preference.index(self.temporaryList[-1].name):
            rejectstudent = self.temporaryList[-1]
            rejectstudent.rejectcount += 1
            del self.temporaryList[-1]
            return rejectstudent, self.sortstudent(student)
        # rejectの場合
        else:
            rejectstudent = student
            rejectstudent.rejectcount += 1
            return rejectstudent, self
    
    
# one to many DA algorithm   
def matching(students, schools):
    poolList = students
    differdAccept = schools
    
    # poolListが空になる（全員の配属が決定）まで提案と諾否の決定を続ける。
    while len(poolList)>0:
        school = next(school for school in differdAccept if school.name == poolList[0].tempPref()) 
        index = schools.index(school) 
        select = school.choice(poolList[0])
        if select[0] == None:
            del poolList[0]
            differdAccept[index] = school
        else:
            del poolList[0]
            poolList.append(select[0]) 
            differdAccept[index] = school

    # 最終結果は配属学生を辞書で表示
    matching = {} 
    for school in differdAccept:
        result = []
        for student in school.temporaryList:
            result.append(student.name)
        matching[school.name] = result
    
    return matching
   
