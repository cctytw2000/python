# 6.	將下列的email讀取出來
# data = "From:Lenyo Lee (Sales ROW)< Lenyo@jetbrains.com>"
data = "From:Lenyo Lee (Sales ROW)< Lenyo@jetbrains.com>"
data1 = data.split(" ")
data2 = data1[4]

print(data2.rstrip(">"))

