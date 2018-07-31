list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = []
# for i in list1:
#     list2.append(i**2)

# list2 = [i**2 for i in list1]
# print(list2)

# for i in list1:
#     if i % 2 == 0:
#         list2.append(i)

list2 = [i for i in list1 if i % 2 == 0]
print(list2)
