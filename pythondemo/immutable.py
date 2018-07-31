#python 所有的東西都是物件 id、type、value(可變的 mutable vs 不可變的 immutable)
# a = "abc"
# b = "abc"
# print(id(a))
# print(id(b))
# # print(type(a))
# 如果是可變的，id不會改變
# 如果是不可變的，id會改變
# a = "xyz"
# print(id(a))
# print(id(b))

# print(b[0])
# b[0] = "k"  # TypeError: 'str' object does not support item assignment

# x = ["a","b","c"]
# y = x
# print(id(x))
# print(id(y))
# print(x)
# print(y)

# 如果是可變的，id不會改變
# 如果是不可變的，id會改變
# y[0] = "k"
# print(id(x))
# print(id(y))

b = True
print(id(b))
b = False
print(id(b))

# 可變的
# list、set、dict

# 不可變的
# str、bool、int、float、tuple、frozenset

