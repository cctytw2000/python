# a = "the zen of python"
# # print(a.capitalize())
# # print(a.title())
# b = a.title()
# print(b)
# print(b.swapcase())
# print()
# print(a.count("Th"))
# print(a.rfind("h"))
# print(a)
# print(a.strip(" T,n "))
# print(a.lstrip(" "))
# b = ["THEASDDSGDFG"]

# print(b)
# print(b.istitle())


# a=["a","b","c",1,2,3]
# print(a[3])   #1
# print(a[-1])  #3
# print(a[3:5]) #1  2
# print(a[:4])  # a b c 1 
# print(a[5:])  # 3


# a=[1,2]
# # a = a + [3,4]   #1 2 3 4
# # print(a)
# # a.append("b")   #1 2 3 4 b 
# # print(a)      
# # b=["c","d"]     #1 2 3 4 b c d
# # a.extend(b)
# # print(a)        
# # a.insert(3,3.5) #1 2 3   3.5    4 b c d
# # print(a)
# # a.insert(5,"a")   #1 2 3   3.5   4 a b c d
# # print(a)
# # a[0:5] = "lisa",1.74
# # print(a)
# # a[0] = "一"
# # print(a)
# # a[0:2] = "lisa",1.74
# # print(a)
# # x=["a","b","c"]
# # y = x

# # print(y)
# # print(id(y))
# # x[0] = 1
# # print(x)
# # print(id(x))
# a,b = list("abc"),list("def")
# print(a,b)
# str1 = " hellow "
# print(len(str1))
# print(str1.split("l"))
# a="123"
# b="456"
# c = a + b
# print(c)
# d="789"
# e=c+d
# print(e)
# a = [1,2,3,4,5,6,7,8,9]
# b = []
# for i in a:
#     b.append(i)
    
#     print(b)
# a = [1,2,3,4,5,6,7,8,9]
# b = [i for i in a if i % 2 ==0]
# print(b)
# t = ("a","b","c","d","e")
# d = ("f",)
# # print(type(d))
# # # print(t[3])
# # # t[1] = "z"
# # # print(t[1])
# # print(t.count("c"))

# c = t + d
# print("x" not in c)
# my_set = {"tom",30,"tom@yahoo.com.tw"}
# my_set.add("a")
# my_set.update("b","c")
# print(type(my_set))
# print(my_set)
# a = {2,4,6,8,10,12}
# b = {3,6,9,12,15,18}
# print(a | b)
# print(a & b)
# print(a - b)
# print(a ^ b)
# dict = {"name":"john","age":30}
# print(type(dict))
# print(dict)
# print(dict["name"])
# dict["age"] = 40
# dict["email"] = "john@yahoo.com.tw"
# print(dict)
# del dict["email"]
# print(dict)
# print("name" in dict)
# print("email" in dict)
# for k,y in dict.items():
#     print(k,y)
# print(dict.get("name"))
# for l in dict.values():
#    print(l)
# ===========================================================    
# def celsius(degreeC):
#     degreeF = degreeC * 1.8 +32
#     return  degreeF
# text = celsius(100)
# print(text)
# def fahrenheit(degreeA):
#     degreeB = (degreeA - 32) / 1.8
#     return degreeB 
# abc = fahrenheit(212)
# print(abc)
# def text():
#     global var
#     var = 10
#     print(var)
# var = 15
# text()
# print(var)
#========================================================
# def fun(s1,s2="world",count=1):
#     s = s1 + s2
#     print(s * count)

# fun("hellow",count=1)
# fun("hi","jack",5)
# fun("hi","jack",2)
# fun("hi",count=5)
#========================================================
# def count(*add_all):
#     print(add_all)
#     count = 0
#     for i in add_all:
#         count += i
#     return count
# print(count(1,2,3,4,5,))   
#========================================================
# def info(**add_dict):
#     print(add_dict)
# info(name="john",age="30")
#========================================================
# def fun1(start,*args,**kwargs):
#     print("start=",start)       
#     print("*args=",args)
#     print("**kwargs=",kwargs)
# fun1(1,2,3,a=4,b=5)
#========================================================
# def g(x):
#     return 3 * x + 1
# print(g(5))

# g = lambda x : 3 * x +1
 
# print(g(5))  
# fullname = lambda fn,ln : fn.strip().title()+" "+ln.strip().title()
# print(fullname(" eagle","wu"))
# class f():
#     pass
# a = f()
# print(f)
# print(a)
class user_1():
   def __init__(self,first,last):
       self.first = first
       self.last  = last
       self.fullname = first + last
       self.email = first + last + "@yahoo.com.tw"
       return 
user1=user_1("john","yeh")
print(user1.fullname)
print(user1.first+user1.last)
print(user1.email)       