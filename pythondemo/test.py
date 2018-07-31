# import random   #匯入模組

# # random.randint(a,b)
# # 回傳一個整數i a<=i<=b
# print(random.randint(1,10))

# x = ["a","b","c"]
# y = x
# # z = x[:]
# z = list(x)

# print(x)
# print(id(x))
# print(y)
# print(id(y))
# print(z)
# print(id(z))
# y[2] = "d"
# print(x)
# print(id(x))
# print(y)
# print(id(y))
# print(z)
# print(id(z))

# list1 = [1,2,2,3,3,3]

list1 = ["a","b","c","d","a","c","a","d"]
a = {}
for i in list1:
    if list1.count(i) >= 1:
        a[i] = list1.count(i)
print(a)







