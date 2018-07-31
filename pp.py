class student :
    count = 0
    def __init__(self,name,grade):
        student.count+=1
s1 = student("eric",90)
s2 = student("tom",86)
print("全部的學生數="+str(student.count))