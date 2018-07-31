import random
name = input("請輸入名子:")
year = int(input("請問你/妳是哪一年出生的(西元):"))
age = 2018 - year
bf = input("請輸入性別(男OR女):")
abc = ""
tall = int(input("請輸入身高:"))
fat = int(input("請輸入體重:"))
if bf == "男":
    abc = abc + "你"
else:
    abc = abc + "妳"
if year % 4 >= 1:
    print("{}是平年出生的".format(abc))
elif year % 4 == 0 and year % 100 >= 1:
    print("{}是閏年出生的".format(abc))
elif year % 100 == 0 and year % 400 >= 1:
    print("{}是平年出生的".format(abc))
else:
    print("{}是閏年出生的".format(abc))
print("{0}的年紀為:{1}".format(abc, age))
if bf == "男":
    print("{}帥哥\n你好".format(name))
else:
    print("{}美女\n妳好".format(name))

bmi = fat / (tall / 100) ** 2
if (bmi < 18.5):
    print("{3}的身高:{0:.1f},{3}的體重:{1:.1F}{3}的bmi:{2:.1f},屬於\t紙片人".format(
        tall, fat, bmi, abc))
elif (bmi <= 18.5 and bmi < 24):
    print("{3}的身高:{0:.1f},{3}的體重:{1:.1F}{3}的bmi:{2:.1f},屬於\t勝人".format(
        tall, fat, bmi, abc))
elif (bmi <= 24 and bmi < 27):
    print("{3}的身高:{0:.1f},{3}的體重:{1:.1F}{3}的bmi:{2:.1f},屬於\t社會人".format(
        tall, fat, bmi, abc))
elif (bmi <= 30 and bmi < 35):
    print("{3}的身高:{0:.1f},{3}的體重:{1:.1F}{3}的bmi:{2:.1f},屬於\t沒運動人".format(
        tall, fat, bmi, abc))
else:
    print("{3}的身高:{0:.1f},{3}的體重:{1:.1F}{3}的bmi:{2:.1f},屬於\t神人".format(
        tall, fat, bmi, abc))


print("{0}今天的幸運數字為:{1}".format(abc, lucky))
