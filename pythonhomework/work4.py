# 4.	列出1到1000中不能被2整除也不能被3整除的數字

math = list(range(1, 1001))

print([i for i in math if i % 2 >= 1 and i % 3 >= 1])
