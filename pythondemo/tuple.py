# my_tuple = ()
# my_tuple = (20)
# my_tuple = (20,)
# print(type(my_tuple))

# my_tuple = ("Tom", 30, "Tom@gmail.com") 
# print(my_tuple)
my_tuple = ("a","b","c","d","e","f")
# print(my_tuple[3])  #d
# print(my_tuple[-3]) #d
# print(my_tuple[2:5]) #(c,d,e)

# for ele in my_tuple:
#     print(ele)

#不能這樣寫
# my_tuple[1] = "x"
# print(my_tuple[1])

my_tuple += ("a","b","c")
# print(my_tuple * 2)
# print(my_tuple[1] > my_tuple[2])
# print("x" in my_tuple)
# print("x" not in my_tuple)
# print(my_tuple.index("b"))  #1
# print(my_tuple.count("b"))  #2
print(max(my_tuple))
print(min(my_tuple))

