# str1 = "Hello "
# str2 = 'World'
# greeting = str1 + str2
# print(greeting)
# print(greeting * 3)

language = "python"
# print(len(language))   #len("string")回傳幾個字元  6
# # letter = language[2]
# letter = language[-2]
# print(letter)          #o
# index = 0
# while index < len(language):
#     letter = language[index]
#     print(index, letter)
#     index += 1

# str[start:end[:step]]
#取回start開始到end-1之間的字串
#step回傳一個字元，往前移到幾個位置
str1 = "Hello World"
print(str1[0:5]) #Hello
print(str1[:3])  #Hel
print(str1[6:])  #World
print(str1[::2])  #????