# def my_function(x):
#     return 3 * x + 1

# print(my_function(2))

# my_function = lambda x : 3 * x + 1
# print(my_function(2))

# fullname = lambda fn,ln: fn.strip().title() + " " + ln.strip().title()

def fullname(fn, ln):
    """說明
    fullname 
    參數:fn、ln
    回傳:去掉空白轉成第一個英文字母大寫fn + ln的結果   

    """
    return fn.strip().title() + " " + ln.strip().title()

# print(fullname("  eagle"," wu "))
print(help(fullname))
