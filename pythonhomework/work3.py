# 3.	用*畫出下列圖型

# Enter the number of rows：10
#        ^
#       ^^^
#      ^^^^^
#     ^^^^^^^
#    ^^^^^^^^^
#   ^^^^^^^^^^^
#  ^^^^^^^^^^^^^
j = -1

i = int(input("請輸入數字:"))
for k in range(1, i):
    j = j+2
    print(" "*(i-k)+"*"*j)
print(" "*(i-1)+"*")
print(" "*(i-1)+"*")
