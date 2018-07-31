class student:
    count = 0
    def __init__(self,name,grade):
        self.name = name
        self.__grade = grade
        student.count += 1


s1 = student("mary", 90)
s2 = student("john", 90)
s3= student("jack", 90)
s4 = student("eric", 90)
print("客戶人數:{}".format(student.count))

# print("s1.name="+s1.name)
# print("s1.grade="+str(s1.__grade))
