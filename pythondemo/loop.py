# range(stop)
# range(start,stop)
# range(start,stop, step)

# print(range(100))
# print(list(range(10,100,5)))

# for x in range(10): #range(10) = [0,1,2,3,4,5,6,7,8,9]
#     print("I Love Python{}".format(x))
#     # print("Hello",end=",")

# sum = 0
# for number in range(1,101):
#     sum += number
# print("1+2+3+...+99+100={}".format(sum))

#while
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#continue break
# for i in range(10):  #[0,1,2,3,4,5,6,7,8,9]
#     if i % 2 == 0:
#         continue
#     print(i)

while 1:
    text = input("輸入q中斷程式")
    if text == "q":
        print("bye")
        break
    print(text)