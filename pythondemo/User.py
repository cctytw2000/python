import uuid
#建立類別
class User():
   def __init__(self,first,last):
       self.first_name = first
       self.last_name = last
       self.email = first + "." + last + "@company.com"

   def sayHi(self):
       print("Hello All")

   def fullname(self):
       print("My Name is {} {}".format(self.first_name, self.last_name))


#建立一個類別繼承User類別的功能
class Member(User):
    def __init__(self, first, last, age):
        super().__init__(first,last)
        self.age = age
        self.id = ""

    def sayHi(self):
        super().sayHi()
        print("我的年紀是 {}".format(self.age))

    def register(self):
        self.id = uuid.uuid1()

memberA = Member("Jack","Wu", 30)
memberA.sayHi()
memberA.fullname()
print(memberA.email)
print(memberA.age)
memberA.register()
print(memberA.id)

# userA = User("Eric","A")
# print(userA.email)
# userA.sayHi()
# userA.fullname()

# userB = User("Mary","B")
# userB.fullname()

# userC = User()



#產生物件
# userA = User()
# userB = User()

# def sayHi(fn,ln):
#     print("Hello " + fn + ln)

# print(User)
# print(userA)
# userA.first = "Tom"
# userA.last = "A"
# userA.sayHi = sayHi


# userA.sayHi(userA.first,userA.last)

# userB.first = "Jack"
# print(userB.last)

