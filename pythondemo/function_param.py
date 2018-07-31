# def fun(s1,s2,count):
#     s = s1 + s2
#     print(s * count)

# #位置參數
# fun("Hello ", "World ", 3)
# #關鍵字參數
# fun(count=2, s1="Hello ",s2="World ")

# def fun(s1, s2="World ", count=1): 
#     s = s1 + s2
#     print(s * count)


# fun("Hello ")
# fun("Hello ", "Fiona ")
# fun("Hello ", "Steve ", 3)
# fun("Hello ", count=3)

# def count(s1,*add_all): 
#     print(s1)   
#     print(add_all)
#     # count = 0
#     # for ele in add_all:
#     #     count += ele
#     # print(count)

# count(1)
# count(1,2)
# count(1,2,3)
# count(1,2,3,4)
# count(1,2,3,4,5)

# def info(**all_dict):
#     print(all_dict)

# info(name="Tom")
# info(name="Tom",age=30,email="Tom@gmail.com")

def fun1(start, *args, **kwargs):
    print("start=", start)
    print("位置參數=", args)
    print("關鍵字參數=", kwargs)

fun1(1,2,3,a=4,b=5)




